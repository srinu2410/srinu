
def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_up_to(n):
    """Find all prime numbers up to n"""
    return [num for num in range(2, n + 1) if is_prime(num)]

def main():
    try:
        choice = input("1. Check if a number is prime\n2. Find all primes up to a number\nChoose (1 or 2): ")
        
        if choice == "1":
            num = int(input("Enter a number: "))
            if is_prime(num):
                print(f"{num} is a prime number ✓")
            else:
                print(f"{num} is not a prime number ✗")
        
        elif choice == "2":
            n = int(input("Enter the upper limit: "))
            primes = find_primes_up_to(n)
            print(f"Prime numbers up to {n}: {primes}")
        
        else:
            print("Invalid choice!")
    
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()