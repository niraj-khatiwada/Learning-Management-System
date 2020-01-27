from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import string

def validate_username(value):
    if not (string.ascii_letters+string.digits) and '_' and '.' and '-' in value:
        raise ValidationError(_('Username can have "numbers letters _ - ." only')) 
    return value
