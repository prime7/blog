from django.shortcuts import render,get_object_or_404,redirect
from .forms import EmailSubscribeForm,EmailUnSubscribeForm
from .models import Subscribers
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = EmailSubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['user_email']
            obj = Subscribers.objects.create(user_email = email)
            current_site = get_current_site(request)
            link = str(current_site)+"/confirm/"+str(obj.confirmKey)
            html_message = loader.render_to_string('newsletter/email_subscribe_msg.html',
				{
					'object' : obj,
                    'link' : link,
                    'current_site':current_site,
				}
			)

            subject = 'Confirmation Email'
            message = link
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None,html_message=html_message)

    else:
        form = EmailSubscribeForm()
    return render(request, 'newsletter/subscribe.html',{'form': form})

def unSubscribe(request):
    if request.method == 'POST':
        form = EmailUnSubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['user_email']
            obj = get_object_or_404(Subscribers,user_email = email)
            current_site = get_current_site(request)
            link = str(current_site)+"/confirm/"+str(obj.confirmKey)
            html_message = loader.render_to_string('newsletter/email_unsubscribe_msg.html',
				{
					'object' : obj,
                    'link' : link,
                    'current_site':current_site,
				}
			)

            subject = 'Confirmation Email'
            message = link
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None,html_message=html_message)

    else:
        form = EmailUnSubscribeForm()
    return render(request, 'newsletter/unsubscribe.html',{'form': form})


def confirmSubscribe(request,key = None):
    instance = get_object_or_404(Subscribers,confirmKey = key)
    instance.confirmed = True
    instance.save()
    return render(request, "newsletter/confirm_redirect.html",{})

def confirmUnSubscribe(request, key=None):
	instance = get_object_or_404(Subscribers, confirmKey=key)
	instance.delete()
	return render(request, "newsletter/confirm_unsubscribe.html",{})