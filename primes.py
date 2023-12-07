"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")

    prime_list = []
    number = 2  # Starting from the first prime number

    while len(prime_list) < number_of_primes:
        # Check if the number is prime
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_list.append(number)
        
        number += 1

    return prime_list
