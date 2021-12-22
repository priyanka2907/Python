#2. Write a program which accept one number and display below pattern. 
#Input : 5 
#Output : 
# * * * * * 
# * * * * *
# * * * * * 
# * * * * * 
 #* * * * *
 
def main():
    print("Enter a number: ");
    no = int(input());
    
    for i in range(no):
        for j in range(no):
            print(" * " ,end=" ");
        print();    



if __name__ == "__main__":
    main()

############ ################### OUTPUT ############# ##############
#C:\Users\Abhi\Desktop\Python\Assignment2>python Assignment2_2.py
#Enter a number:
#5
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *

# C:\Users\Abhi\Desktop\Python\Assignment2>
