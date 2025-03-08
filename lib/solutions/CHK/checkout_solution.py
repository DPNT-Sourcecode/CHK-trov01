import math


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)]}
    valid_inputs = ('A', 'B', 'C', 'D', 'E')
    multiple_offers = {'E': ('B', 2)}
    frequency_map = {}
    for s in skus:
        if s not in valid_inputs:
            return -1
        if s in frequency_map:
            frequency_map[s] += 1
        else:
            frequency_map[s] = 1

    total = 0

    for s in frequency_map:
        count = frequency_map[s]
        if s in multiple_offers:
            s_free, qty = multiple_offers[s]
            if s_free in frequency_map:
                frequency_map[s_free] = max(0, frequency_map[s_free] - math.floor(count / qty))

        if s in offers:
            for offer_quantity, offer_price in offers[s]:
                total += math.floor(count / offer_quantity) * offer_price
                count = count % offer_quantity
            frequency_map[s] = count

    total += sum(frequency_map[s] * prices[s] for s in frequency_map)
    return total

#
# print(checkout("E"))
# print(checkout("EEBB"))
# print(checkout("AAAAA"))
# print(checkout("EE"))
# print(checkout("ABCDE"))
# print(checkout("AAAA"))
# print(checkout("AAAABBB"))





