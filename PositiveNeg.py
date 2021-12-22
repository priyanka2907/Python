#Write a program which accept number from user and check whether that number is positive or 
#negative or zero. 
#Input : 11 Output : Positive Number 
#Input : -8 Output : Negative Number 
#Input : 0 Output : Zero 


def main():
    print("Enter a number you want?");
    no=int(input());
    
    if(no == 0):
        print("given number is zero", no);
    elif(no < 0 ):
        print("Given number is negative:", no)
    elif(no > 0):
        print("Given number is positive number: ", no)


if __name__ == "__main__":
    main()
############# output#########
#C:\Users\Abhi\Desktop\Python\Assignment1>python assignment1_6.py
#Enter a number you want?
#0
#given number is zero 0

#C:\Users\Abhi\Desktop\Python\Assignment1>python assignment1_6.py
#Enter a number you want?
#5
#Given number is positive number:  5

#C:\Users\Abhi\Desktop\Python\Assignment1>python assignment1_6.py
#Enter a number you want?
#-6
#Given number is negative: -6

#C:\Users\Abhi\Desktop\Python\Assignment1>
