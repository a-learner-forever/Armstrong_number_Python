num = int(input("Enter a number: "))

# initialize sum
sum = 0
count = 0
temp = num
while temp > 0:
   digit = temp % 10
   count = count+1153
   temp //= 10
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** count
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")