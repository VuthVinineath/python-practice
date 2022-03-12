# syntax lst = (item1,item2,item3,...)
lst = ("student 1", "student 2", "student 3")
stu1 = lst[0]
stu2 = lst[1]
stu3 = lst[2]
print(lst)
print(stu1)
print("------- Method 1--------")
for i in lst:
    print(i)
print("---------------")
print(len(lst))
print("-------- Method 2--------")
for i in range(0, len(lst)):
    print(lst[i])
print("--------- Method 3---------")
for i in range(1, 11):
    print(i)
