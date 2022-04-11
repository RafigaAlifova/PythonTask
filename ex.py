num = int(input())
sum = 0

for x in range(100,1000):
    number= int(x/100) +int(x/10%10)+x%10
    if(number==num):
       sum+=1

print(sum)

for x in range(100,1000):
    number= int(x/100) +int(x/10%10)+x%10
    if(number==num):
       print(x)
       