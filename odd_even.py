def main():

    X = int(input("whats X"))
    if is_even (X):

        print("Even")

    else:
        print("odd")
def is_even(X):
        if X%2==0:
             return True
        else:
             return False
    
main()

