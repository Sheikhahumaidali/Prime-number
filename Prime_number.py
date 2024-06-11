def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # other even numbers are not prime
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def get_prime_numbers(limit):
    """Get prime numbers up to a specified limit."""
    prime_numbers = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

if __name__ == "__main__":
    limit = 50  # Change this limit as needed
    primes = get_prime_numbers(limit)
    print(f"Prime numbers up to {limit}: {primes}")
  
