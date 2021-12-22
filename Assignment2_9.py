#9. Write a program which accept number from user and return number of digits in that number. 
#Input : 5187934 Output : 7

def main():
    print("Enter a number");
    no = int(input());
    i=1;
    count=1
    while(i < no):
        if(no):
            no =no /10;
            count=count+1;
            i=i+1;
        else:
            i=i+1;
    print(count);
        


if __name__ == "__main__":
    main();
    
    
############# ################ OUTPUT ########## #################
#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_9.py
#Enter a number
#5187934
#7

#C:\Users\Abhi\Desktop\Python\Assignment2>
