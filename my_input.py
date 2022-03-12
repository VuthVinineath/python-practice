while True:
    name = input("Please input your name: ")
    sex = input("Please input sex: ")
    age = int(input("Please input your age: "))

    print("Student name is: ", name, " ",
          sex, "Age: ", age)
    x = input("Do you want to continue? yes/no ")
    if x == "yes":
        continue
    else:
        break
print("Out of loop")
