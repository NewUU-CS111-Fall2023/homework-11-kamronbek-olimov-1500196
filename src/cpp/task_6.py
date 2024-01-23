def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_greater_than_n(n):
    primes = []
    current_number = n + 1

    while len(primes) < 2:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1

    return primes

n = int(input("n = "))
result = generate_primes_greater_than_n(n)
print(f"next two prime numbers:  {result}")
