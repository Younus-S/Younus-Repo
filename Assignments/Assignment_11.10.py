# def print_triangle(inte):
#     if inte > 0:
#         for t in "triangle":
#             print(inte*"*")
#             inte += 1
        

#         for t in "triangle":
#             print(inte*"*")
#             inte -=1

print_triangle(1)

def print_triangle(number):
    if number > 0:
        for n in range (1,number+1):
            print(n*"*")
            n += 1

print_triangle(5)