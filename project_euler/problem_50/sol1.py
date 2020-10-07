"""
https://projecteuler.net/problem=50
Consecutive prime sum

Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


def sieve(n: int) -> list:
    """
    Sieve of Erotosthenes
    Function to return all the prime numbers up to a certain number
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    >>> sieve(3)
    [2]

    >>> sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i

    primes = [2]

    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)

    return primes


def solution() -> int:
    """
    Returns the solution of the problem
    >>> solution()
    997651
    """
    primes = sieve(1_000_000)
    length = 0
    largest = 0

    for i in range(len(primes)):
        for j in range(i + length, len(primes)):
            sol = sum(primes[i:j])
            if sol >= 1_000_000:
                break

            if sol in primes:
                length = j - i
                largest = sol

    return largest


if __name__ == "__main__":
    print(solution())
