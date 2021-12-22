#6. Write a program which accept one number and display below pattern. 
#Input : 5 
#Output :
 #* * * * * 
 #* * * * 
 #* * * 
 #* * 
 #* 
 
 
def main():
    print("Enter any number to display pattern: ");
    no = int(input());
    
    val=no;
    for i in range(no):
        for j in range(val):
            print("*" , end=" ");
            
        print();
        val=val-1;
            
 
 
if __name__ == "__main__":
    main();
    
######### ################ OUTPUT ################## ##########
#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_6.py
#Enter any number to display pattern:
#5
#* * * * *
#* * * *
#* * *
#* *
#*

#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_6.py
