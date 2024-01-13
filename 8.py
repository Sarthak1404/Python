# reverse a string
str = input("Enter string") #  string variable  
print ("The original string  is : ",str)   
reverse_string = ""  # Empty String  
count = len(str) # Find length of a string and save in count variable  
while count > 0:   
    reverse_string += str[ count - 1 ] # save the value of str[count-1] in reverseString  
    count = count - 1 # decrement index  
print ("The reversed string is : ",reverse_string)# reversed string  -