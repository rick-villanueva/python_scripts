#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  
        #The list starts at 3 and goes by 2s because 
        #it avoids any num divisible by 2
            if x%y == 0: #not a prime, if it finds any value of y for which x mod y is 0, then x it's not prime. 
                x += 2
                break
        else:
            primes.append(x) #prime number, if there is no y for which x mod y is 0, then it is a prime number
            x += 2
    
        
    print(primes)
    print(len(primes))
    
#Is num a prime? 
def is_prime(num): 
    x = num 
    for y in range(3,x):
        if x%y == 0:
            print("Not a prime")
    else:
        print("True")
  
#Logic 
while True:
    x = input("Enter a number:")
    count_primes(int(x))
    is_prime(int(x))
    
    y = input("Another number?: y/n ")
    if y == "y":
        continue
    else:
        print("Thanks for using prime counter")
        break