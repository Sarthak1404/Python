# fibonacci series
num_terms=int(input("Enter the number of terms"))
a=0
b=1
print(a)
print(b)
for i in range (1,num_terms-1):
    c=a+b
    print(c)
    a=b
    b=c
