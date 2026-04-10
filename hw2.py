# H.W k onk  babe kora jaii so eta ekta niom just 
def main():
    difficulty = input("Difficult or Medium or Easy"  )
    if not(difficulty=="Difficult" or difficulty=="Medium" or difficulty=="Easy"):
        print("Enter a valid difficulty ")
        return
    player = input("Multi or Group or Single")
    if not(player=="Multi" or player=="Group" or player =="Single"):
        print("Enter a valid player")
        return
    if difficulty=="Difficult" and player=="Multi":
        print("Poker")
    elif difficulty=="Difficult" and player =="Group":
        print("mattha banga")
    elif difficulty=="Difficult" and player=="Single":
        print("klon")
    if difficulty=="Medium" and player=="Multi":
        print("shanti")
    elif difficulty=="Medium" and player=="Group":
        print("Bidda")
    elif difficulty=="medium" and player=="Single":
        print("Shoitan")
    if difficulty =="Easy" and player=="Multi":
        print("Daba")
    elif difficulty=="Easy" and player=="Group":
        print("clock")
    elif difficulty=="Easy" and player=="Single":
        print("Ron")
main()