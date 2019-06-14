# Django Blog
A blog application built with Django and hosted in digital ocean. Don't hesitate to get in touch with me regarding any problem,
help,suggestion and contribution to this project. 
Email me at tarek5701@gmail.com

# Setting up the project

```bash
git clone https://github.com/prime7/blog
```
Rename the file **.env.sample** with **.env** and fill all the credentials don't forget to make **debug=True**. I have used **postgresql** here, so make postgresql database and table and insert the database credentials accordingly.

Make a virtualenv and add the libraries by the following command after activating the virtualenv
```bash
pip install -r requirements.txt
```
Then migrate and run the server 
```bash
python manage.py migrate
python manage.py runserver
```
