from functools import reduce
from itertools import compress
from math import e
from math import gcd
from math import sqrt
from scipy.special import lambertw


class Prime:
    @staticmethod
    def is_prime(value):
        if value <= 3:
            return value >= 2
        if value == 5:
            return True
        if not gcd(value, 30) == 1:
            return False

        for p in range(7, int(sqrt(value)), 20):
            if value % p == 0 or \
                                    value % (p + 4) == 0 or \
                                    value % (p + 4) == 0 or \
                                    value % (p + 6) == 0 or \
                                    value % (p + 10) == 0 or \
                                    value % (p + 12) == 0 or \
                                    value % (p + 16) == 0 or \
                                    value % (p + 22) == 0 or \
                                    value % (p + 24) == 0:
                return False
        return True

    @staticmethod
    def int_from_prime_division(pd):
        return reduce((lambda acc, pv: acc * pv[0] ** pv[1]), pd, 1)

    @staticmethod
    def prime_division(value):
        if value == 0:
            raise ZeroDivisionError
        if value == 1:
            return [(1, 1)]
        if value < 0:
            value *= -1
            pv = [(-1, 1)]
        else:
            pv = []

        for prime in Prime.primes_to(int(sqrt(value))):
            count = 0
            value1, mod = divmod(value, prime)
            while mod == 0:
                value = value1
                count += 1
                value1, mod = divmod(value, prime)

            if count:
                pv.append((prime, count))

            if value1 <= prime:
                break

        if value > 1:
            pv.append((value, 1))

        return pv

    @staticmethod
    def primes_to(value):
        sieve = bytearray([True]) * (value // 2 + 1)
        for i in range(1, int(value ** 0.5) // 2 + 1):
            if sieve[i]:
                sieve[2 * i * (i + 1)::2 * i + 1] = bytearray((value // 2 - 2 * i * (i + 1)) // (2 * i + 1) + 1)
        return [2, *compress(range(3, value, 2), sieve[1:])]

    @staticmethod
    def primes_first(count):
        value = int(e ** -lambertw([-1 / count], -1)[0].real)
        primes = Prime.primes_to(value)
        if len(primes) < count:
            primes = Prime.primes_to(value * 2)
        return primes[0:count]

