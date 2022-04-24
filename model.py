#creating different functions that validates the passwords and user name

def is_all_empty(chars):
    '''
    this function checks if the input is empty and returnsw True
    args:set of characters
    return type: boolean
    '''
    if len(chars) == 0:
        return True
    return False

def is_valid_password(password):
    '''
    this function checks if the password has a certain minimunm length and contains alphanumeric characters, also contains special chars
    args: password
    return type: boolean, returns true if password has one upper case, one lower case, one special char and one numeric character. 
    '''
    if len(password) < 5:
        raise ValueError("Password's length must be at least 5 characters. ")
    if type(password) != str:
        raise TypeError("Password must be a string")

    special_char = 0
    upper_case = 0
    lower_Case = 0
    num = 0

    for chars in password:
        if chars.isdigit():
            num += 1
        if chars.isupper():
            upper_case += 1
        if chars.islower():
            lower_Case += 1
        if chars in {"@", "$", "!", "^", "&", "*", "#"}:
            special_char += 1
    
    if special_char > 0 and lower_Case > 0 and upper_case > 0 and num > 0:
        return True
    return False
        







    





