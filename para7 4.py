def raise_to_the_degrees(number, max_degree):
    i = 0
    for num in range(max_degree):
        yield number**i
        i += 1
res = raise_to_the_degrees(123456, 500)
print(res)
for obj in res:
    print(obj)
    print("-----")