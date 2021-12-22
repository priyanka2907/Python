#7. Write a program which contains one function that accept one number from user and returns 
#true if number is divisible by 5 otherwise return false. 
#Input : 8 Output : False 
#Input : 25 Output : True

def main():
    print("Enter a number you want?");
    no=int(input());
    if(no % 5 == 0):
        print("True");
    else:
        print("False");
    


if __name__ == "__main__":
    main()
    
################# Output
#C:\Users\Abhi\Desktop\Python\Assignment1>python assignment1_7.py
#Enter a number you want?
#8
#False

#C:\Users\Abhi\Desktop\Python\Assignment1>python assignment1_7.py
#Enter a number you want?
#25
#True

#C:\Users\Abhi\Desktop\Python\Assignment1>