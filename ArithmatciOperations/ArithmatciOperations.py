#Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
#parameters as number and perform the operation. Write on python program which call all the 
#functions from Arithmetic module by accepting the parameters from user

import Arithmetic ;
    
def main():
    print("Please enter first number :");
    no1 = int(input());
    
    print("Please Enter second number:");
    no2 = int(input());
    
    add = Arithmetic.Add(no1,no2);
    sub = Arithmetic.Sub(no1,no2);
    mult= Arithmetic.Mult(no1,no2);
    div = Arithmetic.Div(no1,no2);
    
    
    print("Addition is: ", add);
    print("Substraction is: ", sub);
    print("Multiplication is: ",mult );
    print("Division is: ",div );
   


if __name__ == "__main__":
    main()
    
############ ####################### OUTPUT############# #####################
#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_1.py
#Please enter first number :
#11
#Please Enter second number:
#10
#Addition is:  21
#Substraction is:  1
#Multiplication is:  110
#Division is:  1.1

#C:\Users\Abhi\Desktop\Python\Assignment2>
