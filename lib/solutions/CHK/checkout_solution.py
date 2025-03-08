import math


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {'A': [(5, 200), (3, 130)], 'B': (2, 45)}
    valid_inputs = ('A', 'B', 'C', 'D')
    multiple_offers = {'E': ('B', 2)}
    frequency_map = {}
    for s in skus:
        if s not in valid_inputs:
            return -1
        if s in frequency_map:
            frequency_map[s] += 1
        else:
            frequency_map[s] = 1

    sum = 0

    for s, count in frequency_map.items():
        if s not in multiple_offers and s not  in offers:
            sum += count * prices[s]

            else:
                sum += math.floor(count / offers[s][0]) * offers[s][1]
                sum += (count % offers[s][0]) * prices[s]
    return sum

# print(checkout("AAc"))
# print(checkout("AAAB"))
# print(checkout("ABBBBBBAB"))
# print(checkout("AABCD"))
# print(checkout("ABCD"))
# print(checkout("AAAA"))
# print(checkout("AAAABBB"))
