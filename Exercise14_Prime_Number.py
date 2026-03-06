# Check input no. is prime or not with help of "Function".

def prime_no(n):
    is_prime = True
    for i in range (2,n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a prime no ")
    else:
        print(f"{n} is not a prime no.")
        
    
no = int(input("Enter a number = "))

prime_no(n = no)