#Sum of whole numbers consecutively using WHILE loop
num = int(input('Enter your number : '))
i = 0
sum = 0
while i <= num:
    sum = sum + i
    i = i + 1
print(sum)