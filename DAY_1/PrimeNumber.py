num=int(input("Enter Number:"))
flag=0

while flag==0:
    def checkPrime(num):
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    r=checkPrime(num)
    if r==False:
        num+=1
        # checkPrime(num)
    if r==True:
        print(num)
        flag=1 

              
    
    



