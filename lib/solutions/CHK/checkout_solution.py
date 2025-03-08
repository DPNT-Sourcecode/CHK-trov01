# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {'A': (3, 130), 'B': (2, 45)}
    valid_inputs = ('A', 'B', 'C', 'D')
    for s in skus:
        if s not in valid_inputs:
            return -1


print(checkout("AAc"))

