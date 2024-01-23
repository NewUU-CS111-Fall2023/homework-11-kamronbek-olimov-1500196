def euler_totient_function(a, b):
    return (a - 1) * (b - 1)

a = int(input("a = "))
b = int(input("b = "))

result = euler_totient_function(a, b)
print(result)
