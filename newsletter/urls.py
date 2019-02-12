from django.urls import path

from .views import subscribe,unSubscribe,confirmSubscribe,confirmUnSubscribe

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/',unSubscribe, name="unsubscribe"),
    path('confirm-subscribe/<str:key>/',confirmSubscribe, name="confirm-subscribe"),
    path('confirm-unsubscribe/<str:key>/',confirmUnSubscribe, name="confirm-unsubscribe"),
]