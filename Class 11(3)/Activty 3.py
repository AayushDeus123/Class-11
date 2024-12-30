#Finding whether the user input is an Armstrong Number or not
num = int(input('Enter a number : '))
sum = 0

temp = num
while temp > 0:
    rem = temp % 10
    sum = sum + rem**3
    temp = temp // 10
    
if num == sum:
    print('The number entered is an Armstrong Number')
else:
    print('The number entered is not an Armstrong Number')  