#10. Write a program which accept number from user and return addition of digits in that number. 
#Input : 5187934 Output : 37 


def main():
    print("Enter a number");
    no = int(input());
    i=1;
    count=0
    while(no!= 0):
       
        ans=no%10;
        count=count+ans;
        no =no // 10;  # // ignore floating point & / consider floating point
        #no=round(no);
           
    print("Sum of digit is :" ,count);
        

if __name__ == "__main__":
    main();

############## ################ OUTPUT ########## ############# 

#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_10.py
#Enter a number
#5187934
#Sum of digit is : 37

#C:\Users\Abhi\Desktop\Python\Assignment2>