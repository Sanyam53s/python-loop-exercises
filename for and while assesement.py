"""
1 #Write a program to print numbers from 1 to 100
for i in range(1, 101):
    print(i)
2 #Write a program to print all even numbers between 1 and 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        
3. #Write a program to print the sum of first n natural numbers.

n = int(input("Enter the value of n: "))
sum_n = 0
for i in range(1, n+1):
    sum_n += i
print("Sum of first", n, "natural numbers is:", sum_n)

4. #Write a program to print the multiplication table of a given number.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num,"x",i,"=",num*i)

5 # Write a program to print all elements of a list using a for loop.

my_list = [10,20,30,40,50,60]
for i in my_list:
    print(i)


 6 # Write a program to count the number of vowels in a string.

text = input("enter a string:")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count+=1
print("number of vowels:",count)

 7 #Write a program to find the largest number in a list
my_list =[10,20,30,40,50,60,70]
largest = my_list[0]
for i in my_list:
    if i>largest:
        largest = i
print("Largest number is :",largest

 8 # Program to print all prime numbers between 1 and 100
for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

9 # Program to calculate factorial of a number using for loop
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is:", fact)

10 # Program to print the reverse of a string using a for loop
text = input("Enter a string: ")
reverse = ""

for i in range(len(text) - 1, -1, 0 - 1):
    reverse += text[i]

print("Reversed string:", reverse)

11 #Write a program to print numbers from 1 to 50 using a while loop.
a = 1
while a <=50:
    print(a)
    a =a+1
"""
12 # Print all odd numbers between 1 and 50
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

13 # Calculate the sum of digits of a number
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)

14 # Reverse a number using a while loop
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

15 #Find factorial using a while loop
num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial is:", fact)

# 16 Keep taking input until user enters 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break

# 17 Find the largest digit in a number
num = int(input("Enter a number: "))
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10

print("Largest digit:", largest)

#1 18 Check whether a number is a palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == num:
    print("Palindrome")
else:
    print("Not a palindrome")

# 19  Print Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b

21 # Number Pattern (for loop example)

Pattern:

1
12
123
1234
12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

22 #Count frequency of each character in a string
text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for key, value in freq.items():
    print(key, ":", value)

23 # Print all Armstrong numbers between 1 and 1000

Armstrong number = sum of digits³ == number (for 3-digit)

for num in range(1, 1001):
    temp = num
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    
    if total == num:
        print(num)

 24 # Simulate an ATM Menu (while loop)
balance = 10000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Deposited! New Balance:", balance)

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn! New Balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Try again.")

25 # Find GCD (HCF) of two numbers using loops

Using Euclid’s method with while loop:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD is:", a)

