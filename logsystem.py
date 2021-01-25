name= str(input("Whats Your Name:   "))
print("Welcome,", name)
UserNames= []
UserPass= []

def login():
  username = str(input("username   "))
  password = str(input("password   "))
  i = UserNames.index(username)
  if UserPass[i]== password and UserNames[i]== username:
    print("logged in successfully")
    isLoggedin =  True
  else:
    print("incorrect password")
    print("try again")
    isLoggedin = False
    login()

def registration():
  username = str(input("username   "))
  password = str(input("password   "))
  UserNames.append(username)
  UserPass.append(password)
  print("*********Login Now*********")
  login()

print("Please choose:")
a= int(input(" 1. Login \n 2. Register    \n"))
if(a==1):
  login()
  if(isLoggedin):
    print("Logged in")
  
elif(a==2):
  registration()

