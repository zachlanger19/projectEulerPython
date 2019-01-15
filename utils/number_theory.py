from functools import reduce
from numpy import array, prod

from utils.prime import Prime
from utils.random_functions import RandomFunctions


class NumberTheory:
    collatz_distances = {1: 1}

    @staticmethod
    def collatz_distance(value):
        if value in NumberTheory.collatz_distances:
            return NumberTheory.collatz_distances[value]
        new_value = value // 2 if value % 2 == 0 else 3 * value + 1
        new_distance = NumberTheory.collatz_distance(new_value) + 1
        NumberTheory.collatz_distances[new_value] = new_distance
        return new_distance

    @staticmethod
    def number_of_divisors(value):
        pd = Prime.prime_division(value)
        exps = [0] * len(pd)

        def min_func(values, options, index):
            return 0

        def max_func(values, options, index):
            return values[index][1]

        divisor_codes = RandomFunctions.recursive_options(pd, exps, min_func, max_func)
        primes = array(pd).transpose()[0]
        codes = array(divisor_codes)
        temp = primes ** codes
        temp2 = list(map(lambda x: prod(x), temp))
        temp2.sort()
        print(len(temp2))

    @staticmethod
    def get_divisors(value):
        pd = Prime.prime_division(value)
        exps = [0] * len(pd)

        def min_func(values, options, index):
            return 0

        def max_func(values, options, index):
            return values[index][1]

        exps_combo = RandomFunctions.recursive_options(pd, exps, min_func, max_func)
        primes = array(pd).transpose()[0]
        exps_combo = array(exps_combo)
        combos = primes ** exps_combo
        divisors = list(map(lambda x: prod(x), combos))
        divisors.sort()
        return divisors

