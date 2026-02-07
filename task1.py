# Sum of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print("The sum is:", result)

# Odd or Even checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
    

#Factorial calculator
a=int(input("Enter a number: "))
factorial=1
for i in range(1,a+1):
    factorial*=i
print(factorial)

# Fibonacci sequence
n=int(input("Enter a number: "))
fib_series = [0, 1]
for i in range(2, n):
    next_term = fib_series[-1] + fib_series[-2]
    fib_series.append(next_term)
print("Fibonacci series up to",n,"terms: ",fib_series)

# String reverse
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

# Palindrome checker
string = input("Enter a string: ")
if string == string[::-1]:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
    
    
# Leap year checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print(year," is a Leap year")
else:
        print(year," is not a Leap year")
        
        
# Armostrong number checker
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")                