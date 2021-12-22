#5.Write a program which accept one number for user and check whether number is prime or not. 
#Input : 5 Output : It is Prime Number


def main():
    print("Enter a number to check whether number is prime or not?");
    no = int(input());
    
    i = 2;
    ans=None;
    
    for i in range(2,no-1,1):
        if(no % i == 0):
            ans = True ;
        
        i= i+1;
      
    if(ans == True):
        print(no ," is a Non-Prime Number");
        
    else:
        print(no," is a Prime Number");


if __name__ == "__main__":
    main();
    
######### ###################### OUPUT ################# ##############

#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_5.py
#Enter a number to check whether number is prime or not?
#11
#11  is a Prime Number

#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_5.py
#Enter a number to check whether number is prime or not?
#15
#15  is a Non-Prime Number

#C:\Users\Abhi\Desktop\Python\Assignment2>