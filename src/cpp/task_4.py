def superPow(a, b):
    if not b:
        return 1

    a %= 1337
    result = 1

    for digit in b:
        result = (pow(result, 10, 1337) * pow(a, digit, 1337)) % 1337

    return result

a = int(input("a = "))

b = list(map(int, input("b = ").split()))

result = superPow(a, b)
print(result)
