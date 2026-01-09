#This is used to test how strong a password is from user input

import string

# import os
# print(os.getcwd())


def check_common_passwords(password):
    with open("CommonPasswords.txt" ,"r") as file: # reads the file
        common = file.read().splitlines() # splitlines creates a list
        if password in common : 
            return True
        return False
            
def password_quality(password):
    score = 0
    rating = "hackable"
    
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_specialcase =any(c in string.punctuation for c in password)
    has_number = any(c.isdigit() for c in password)
    
    
    factors = [has_lowercase,has_uppercase, has_specialcase, has_number]
    score += sum(factors)
    ## half of the score is for lengh and the other half is factors
    pass_len = len(password)
    
    
    if pass_len > 3:
        rating = "Not Safe"
        score += 1
    if pass_len > 6:
        rating = " Okay"
        score += 1
    if pass_len > 10:
        rating = "Good"
        score += 1
    if pass_len > 15: 
        rating = "Amazing"
        score += 1

    return rating, score


def feedback(password):
    if check_common_passwords(password):
        return "Your password can be brute forced becauses its part of common phrases for passwords"
    
    rating, score = password_quality(password)
    
    feedback = f"Your rating is {rating}, and a password quality score is {score}/8:\n"
    length = len(password)
    
    if length < 5:
        feedback += "Your password length is too short, recommend an length of atleast 8. \n"
    if not any(c.isupper() for c in password):
        feedback += "You don't have any uppercases! Add atleast one uppercase to make your password more robust \n"
    if not any(c.islower() for c in password):
        feedback += "You don't have any lowercases! Add atleast one to increase your passwords complexity \n"
    if not any(c in string.punctuation for c in password):
        feedback += "You don't have any special letters, add some to decrease the likelness of your password being cracked \n"
    if not any(c.isdigit() for c in password):
        feedback += "You don't have any digits, add some numbers in your password to increase complexity by 9x! \n"
    return feedback

password = str(input( "Give a password \n")) # Assert this is a string
print(feedback(password))
