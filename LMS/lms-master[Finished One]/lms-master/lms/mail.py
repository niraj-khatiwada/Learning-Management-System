from django.core.mail import send_mail
from django.conf import settings
from .constants import COLLEGE_NAME

class Mail:
    email_from = settings.EMAIL_HOST

    def __init__(self,subject=COLLEGE_NAME+' LMS system',message = None,recipient_list=None):
        try:
            print("---------------------trying for mail -----------------")
            send_mail(subject,message,self.email_from,recipient_list)
        except:
            return "Error occured"