# def sum_multiples(mult):
#     for m in range (1,mult):
#         print(mult/3+mult)

# sum_multiples(100)

def sum_multiples(mult):
    n = 0
    for i in range(1,mult):
        if not i % 5 or not i % 3:
            n = n + i
    print(n)

sum_multiples(100)