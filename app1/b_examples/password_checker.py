password = input("Enter the password : ")
# To check if the password contains minimum of 8 characters ,one number and one uppercase character
result = {}
if len(password) > 8:
    result['length'] = True

else:
    result['length'] = False

result['upper'] = False
for i in password:
    if i.isupper():
        result['upper'] = True

result['digit'] = False
for i in password:
    if i.isdigit():
        result['digit'] = True

print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")