#3. Write a program which accept one number from user and return its factorial. 
#Input : 5 Output :5*4*3*2*1=  120


def main():
    print("Enter a Number: ");
    no = int(input());
    
    ans=1;
    
    for i in range(no,0,-1):
        ans = ans * i;
    print("The Factorial of Given no is :" ,ans);
        


if __name__ == "__main__":
    main()


################ ##################### OUTPUT ################ ##############

#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_3.py
#Enter a Number:
#5
#The Factorial of Given no is : 120

#C:\Users\Abhi\Desktop\Python\Assignment2>