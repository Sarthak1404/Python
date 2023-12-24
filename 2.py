# sum of all even numbers
num_start=int(input("Enter the start of the range"))
num_end=int(input("Enter the end of the range"))
sum=0

for i in range (num_start,num_end+1):
    a=num_start
    if(a%2==0):
        sum=sum+a
    else:
        sum=sum
    num_start+=1

print("Sum of all even numbers in the given range is : ",sum)