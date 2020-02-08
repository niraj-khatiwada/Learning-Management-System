from account.models import Account

def suspend_user(user_id):
    try:
        u = Account.objects.get(id=user_id)
        u.is_suspended = True
        u.save()
        return True
    except:
        return False

def unsuspend_user(user_id):
    try:
        u = Account.objects.get(id=user_id)
        u.is_suspended = False
        u.save()
        return True
    except:
        return False