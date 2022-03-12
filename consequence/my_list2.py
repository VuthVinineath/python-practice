main_lst = []
while True:
    x1 = input("Name : ")
    x2 = input("Sex: ")
    x3 = input("Age: ")
    x4 = input("Income: ")
    lst = [x1, x2, x3, x4]
    main_lst.append(lst)
    x = input("Do you want to continue? yes/no: ")
    if x == "yes":
        break
print(main_lst)
