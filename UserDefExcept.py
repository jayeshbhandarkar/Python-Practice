# 30) WAP to raise a User Defined Exception Class

class InvalidPwd(Exception):
    pass

def verify_pwd():
    while True:
        try:
            pswd = input("\n\n Enter Password: ")
            if pswd!="abc123":
                raise InvalidPwd
            
        except InvalidPwd:
            print("\n\n Invalid Password... Try again...")
            
        else:
            print("\n\n Valid Password")
            break
        
verify_pwd()