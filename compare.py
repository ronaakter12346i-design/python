#starting point is the important 
X  = float(input("whats the x? "))
Y = float(input("whats the Y? "))
Z = float(input("whats the Z? "))

if(X>Y and X>Z):
    print("X is geater than X,Y")
elif(Y>X and Y>Z):
    print("Y is geater than x,Z")
else:
    if(X==Y==Z==0):
        print("X,Y,Z is equal")
    else:
        print("Z is geater than X,Y")