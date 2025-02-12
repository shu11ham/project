import random as rd


occ =0
game = ("s","p","r")
emoji = {'s':'🪨', 'p':'🧻','r':'✂️'}


while True:

    user = input("select any one from '(S/p/r)':".upper()).lower()
    comp = rd.choice(game)

    print(f"you choose: {emoji[user]}".upper())
    print(f"comp choose: {emoji[comp]}".upper())

    if user == "r" and comp == "p":
        a=print("you win".upper())

    elif user == comp:
        print("No one loose".upper())

    elif user == "p" and comp == "r":
        a=print("comp wins".upper())

    elif user == "r" and comp == "s":
        a=print("comp wins".upper())

    elif user == "s" and comp == "r":
        a=print("user wins".upper())

    elif user == "s" and comp == "p":
        a=print("comp wins".upper())

    elif user == "p" and comp == "s":
        a=print("user wins".upper())

    else:
        print("invalid input".upper())
   

    if a == "comp wins".upper():
        occ += 1
   
    con = input("do you want to continoue?(y/n):".upper()).lower() 

    if  con == "n":
        print("thank u for playing".upper())
        break



# game = ("s","p","r")

# emoji = {'s':'🪨', 'p':'🧻','r':'✂️'}


# def user_choice():
#    times = int(input("enter how many times u need to play:".upper()))
#    while True:
#      user = input("select anyone from (s/p/r):".upper()).lower()
#      if user not in game:
#         return user
#      else:
#          print("Invalid entry")
#          continue
     
# def dispaly_choices(user,comp):
#     print(f"you choose:{emoji[user]}".upper())
#     print(f"comp choose:{emoji[comp]}".upper())


# def determine_winner(user,comp):
#     if user == comp:
#         print("TIE")

#     elif ((user=="s" and comp=="r") or (user=="p" and comp=="s") or (user=="r" and comp=="p")):
#         print("you win 👌😊")

#     elif ((user=="r" and comp=="s") or (user=="s" and comp=="p") or (user=="p" and comp=="r")):
#         print("you loose 😒")



# # for i in range (times):

# def play_games():
#  while True:
#     user = user_choice()

#     comp = rd.choice(game)

#     dispaly_choices(user,comp)
#     determine_winner(user,comp)


#     con = input("want to continue?(y/n):".upper()).lower()

#     if con == "n":
#         print("thanks for playing".upper())
#         break

# play_games()






    

