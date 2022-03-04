import json,os

# def Signup():
#     if(os.path.exists("data.json")):
#         with open("data.json","r") as f:
#             b=json.load(f)
#             mo_no=input("enter mo no:- ")
#             for a in b:
#                 if mo_no in  a.values():
#                     print("succesefull")
#                     # break
#                 else:
#                     print("not exite")
#                     # break
#             else:
#                 # c={}
#                 # c["userName"]=input("Enter your Name:- ")
#                 # c["userEmail"]=input("Enter your Email:- ")
#                 # c["userpassword"]=input("Enter your Password: ")
#                 # c["userMobile_no"]=mo_no
#                 # b.append(c)
#                 with open("data.json","w") as r:
#                         json.dump(b,r,indent=4)
#     else:
#         with open("data.json","w") as a:
#             a.write('[]')
# # Signup()

# def log_in():
#     if(os.path.exists("data.json")): 
#         with open('data.json','r') as f:
#             b=json.load(f)
#             c={}
#             c["Mo_no"]=input("Enter the Mo_no:- ")
#             c["Name"]=input("Enter the name:- ")
#             c["Email"]=input("Enter the Email:- ")
#             c["Password"]=input("Enter the password:- ")
#             b.append(c)
#             with open('data.json','w') as y:
#                 json.dump(b,y,indent=4)
#     else:
#         with open('data.json','w') as l:
#             l.write('[]')
# # log_in()

# a=int(input("1. Singup\n2. login \n"))
# if a==1:
#     Signup()
# elif a==2:
#     log_in()












