

class RandomFunctions:
    @staticmethod
    def recursive_options(values, options, min_func, max_func, index=0):
        if index == len(values):
            return [options]

        results = []
        for option in range(min_func(values, options, index), max_func(values, options, index) + 1):
            new_options = options.copy()
            new_options[index] = option
            results.extend(RandomFunctions.recursive_options(values, new_options, min_func, max_func, index + 1))

        return results


# import numpy as np
# from utils.prime import Prime
# pd = Prime.prime_division(5040)
# powers = [0] * len(pd)
# def min_func(values, options, index):
#     return 0
# def max_func(values, options, index):
#     return values[index][1]
# divisor_codes = RandomFunctions.recursive_options(pd, powers, min_func, max_func)
# primes = np.array(pd).transpose()[0]
# codes = np.array(divisor_codes)
# temp = primes ** codes
# temp2 = list(map(lambda x: np.prod(x), temp))
# temp2.sort()
# print(len(temp2))

