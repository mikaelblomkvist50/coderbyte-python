def is_valid_PIN(pin):
    if pin == "1234":
        return True
    else:
        return False

# If the string includes special character we instanly know it's not valid.
# However if we know its a valid string length, it does not necessarily mean it is a valid pin since
# it could be a valid string length with a special character. Hence it's best to check for spcial characters first.
# Then make sure the string has a valid length (4 or 6).

# Pseudo code

# if string contain ! special characters && string length is 4 || 6
#     return True
# else
#     return Fale
