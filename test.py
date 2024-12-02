name = ("bob", "ann", "mike", "liz")
password = ("123", "pass123", "password123", "pass123")

user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123", }



u_tab = input("user name:")
if u_tab in name:
        tab = input("password: ")
        if user.get(name) == user.get(password):
            print("you are here")
        else:
            print("wrong password")
            
else:
        print("wrong user name")
   



