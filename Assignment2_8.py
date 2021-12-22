#8. Write a program which accept one number and display below pattern. 
#Input : 5 
 
#Output : 
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5


def main():
    print("Enter any number to display pattern: ");
    no = int(input());
    
    val=1;
    for i in range(no):
        for j in range(val):
            print(j+1 , end=" ");
            
        print();
        val=val+1;
            
 
 
if __name__ == "__main__":
    main();
 
##################################
#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_7.py
#Enter any number to display pattern:
#5

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

#C:\Users\Abhi\Desktop\Python\Assignment2>