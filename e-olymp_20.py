n = int(input(""))
say=0
while(n>0):
    sum=0
    x=n
    while(x>0):
        sum=sum+x%10
        x=int(x/10)
    
    n=n-sum
    say+=1

print(say)