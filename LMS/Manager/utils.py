import string
import random
from django.core.mail import send_mail
from django.conf import settings

def randomPassword(len):
    password = ""
    key = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
    for i in range(len):
        password = password + random.choice(key)
    return password

class EmailAuto():
    def __init__(self,recipient_list, html_message):
        mail = send_mail(subject='LMS Account Created', message = "", from_email= settings.EMAIL_HOST , recipient_list= recipient_list, fail_silently=False, html_message=html_message)
