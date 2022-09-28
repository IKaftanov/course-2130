def is_prime_v0(n):
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_prime_v1(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def find_primes(n):
    primes = []
    for i in range(n):
        if is_prime_v1(i):  # O(\sqrt{n})
            primes.append(i)
    return primes


def foo_inner_loops(n):
    """ time complexity = O(n^2) """
    for i in range(0, n):
        for j in range(0, n):
            pass


def foo(n):
    """ time complexity = O(n)
        O(n) + O(n) + O(n) = O(n + n + n) = O(3n) = O(n)
    """
    for _ in range(n):  # O(n)
        pass

    for _ in range(n):  # O(n)
        pass

    for _ in range(n):  # O(n)
        pass


def main():
    pass
