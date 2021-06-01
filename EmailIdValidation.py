import re

def isValidEmail(email):
         regex = "^[A-Z0-9._+-]+@[A-Z0-9]+.[A-Z]{2,}$"
         if len(email) > 7:
             if re.match(regex, email, re.IGNORECASE) is not None:
                 return True
     

if isValidEmail("netsetos@gmail.com"):
	print("Valid Email Address")
else:
	print("Invalid Email Address")
