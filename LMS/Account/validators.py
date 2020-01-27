from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy 
import string

def validate_username(username):
    for i in username:
        if not i in string.ascii_letters and not i in string.digits and i != '-' and i != '_' and i != '.':
            raise ValidationError(ugettext_lazy('Username can have "Numbers A-Z a-z _ - ." only'))
    return username
