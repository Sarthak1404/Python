# pallindrome
num_check=int(input("Enter a number:"))
temp=num_check
rev=0
while(num_check!=0):
    dig=num_check%10
    rev=rev*10+dig
    num_check=num_check//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")