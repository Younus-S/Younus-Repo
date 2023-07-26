User={"Name":"abc",
        "Age":25}
print(User)

if User["Age"]<18:
    print("Minor")
elif User["Age"]>=18:
    print("Adult")