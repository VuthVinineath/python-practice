x = int(input("Please input value: "))
if x >= 0 and x <= 5:
    print("Baby")
elif x > 5 and x <= 10:
    print("Kid")
elif x > 10 and x <= 18:
    print("Young")
elif x > 18 and x <= 30:
    print("adult")
else:
    print("old")
