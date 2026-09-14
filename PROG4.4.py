
def new_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
     return True
    else:
        return False

new_password("123","123123")