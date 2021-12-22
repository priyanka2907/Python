# 4.Write a program which accept one number form user and return addition of its factors. 
# Input : 12 Output : 16 (1+2+3+4+6)

def main():
    print("Enter a number : ");
    no = int(input());
    i=1;
    ans=0;
    
    while(i < no ):
        if(no % i == 0):
            ans= ans + i ;
        i=i+1;
    
    print("Addition of ",  no , " factors is : ", ans);

if __name__ == "__main__":
    main()
    
######### ################# OUTPUT ########## ############

#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_4.py
#Enter a number :
#12
#Addition of  12  factors is :  16

#C:\Users\Abhi\Desktop\Python\Assignment2>