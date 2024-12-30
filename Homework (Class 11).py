#Number of digits in entered number
number = int(input("Enter a number: ")) 

if number < 0:
    number = -number  

count = 0 
while number > 0:
    number //= 10  
    count += 1  
print("The number of digits is:", count)