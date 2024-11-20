#Python Armstrong Number Program

#3-digit numbers:

n = int(input("Enter a 3 digit number: "))

sum = 0

x = n 

while n > 0:
    sum += (n%10)*(n%10)*(n%10)
    n //= 10 

if x == sum:
    print(x,"is an Armstrong number")

else:
    print(x,"is not an Armstrong number")
    
#4-digit numbers:

a = int(input("Enter a 4 digit number: "))

mus = 0

b = a

while a > 0:
    mus += (a%10)*(a%10)*(a%10)*(a%10)
    a //= 10 

if b == mus:
    print(b,"is an Armstrong number")

else:
    print(b,"is not an Armstrong number")