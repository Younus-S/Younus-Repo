def print_triangle(inte):
    if inte > 0:
        for t in "triangle":
            print(inte*"*")
            inte += 1
        

        for t in "triangle":
            print(inte*"*")
            inte -=1

print_triangle(1)