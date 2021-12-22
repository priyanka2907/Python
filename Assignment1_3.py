
def Add(value1,value2):
    ans=value1+value2;
    return ans;
    

def main():
    no1=0;
    no2=0;
    
    print("Enter Firts Number:")
    no1=int(input());
    no2=int(input());
    
    ret=Add(no1,no2);
    
    print("Addition of given number's is: ",ret)
    

if __name__ == "__main__":
    main()
    
############Output#######
#C:\Users\Abhi\Desktop\Python\Assignment1>python assignment1_3.py
#Enter Firts Number:
#10
#11
#Addition of given number's is:  21

#C:\Users\Abhi\Desktop\Python\Assignment1>    