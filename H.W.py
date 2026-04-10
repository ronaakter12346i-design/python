# this is my first H.W from CS50 which one is depended on Game Playing

difficulty = input("Difficult or Medium or Easy" )
players = input("Multiple or Group or Single ")

if difficulty =="Difficult" and  players =="Multiple":
    print("Poker")
elif difficulty =="Medium" and players =="Multiple":
    print("vollyball")
elif  difficulty=="Easy" and players=="Multiple":
    print("Jota churi")

if difficulty == "Difficult" and players=="Group":
    print("Ready Court")
elif difficulty=="Medium" and players=="Group":
    print("seven chara")
elif difficulty=="Easy" and players=="Group":
    print("Lokochuri")

if difficulty=="Difficult"and players=="Single":
    print("Chese")
elif difficulty =="Medium" and players=="Single":
    print("Loddo")
elif difficulty=="Easy" and players=="Single":
    print("Run")






