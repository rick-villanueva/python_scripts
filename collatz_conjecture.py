def collatz_conjecture(n):
    numbers = [n]
    
    if n <= 1:
        return [ ]
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = (n*3) + 1 
            
        numbers.append(n)
        
    print(numbers)

def collatz_counter(n):
    numbers = [n]
    
    if n <= 1:
        return [ ]
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = (n*3) + 1 
            
        numbers.append(n)
    
    print(len(numbers))

#logic
while True:
    x = input("Enter a number:")
    collatz_conjecture(int(x))
    collatz_counter(int(x))
    
    y = input("Another number?: y/n ")
    if y == "y":
        continue
    else:
        print("Thanks for using collatz conjecture generator")
        break