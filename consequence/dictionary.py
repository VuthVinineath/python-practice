# dictionary is like an object or json obj. it has key and value
stu = {
    "A": [90, 80, 100, 50],
    "B": [30, 50, 100, 40],
    "C": [70, 30, 20, 40]
}
print(stu)
print(stu["A"])
print(stu["A"], stu["B"])
stu["D"] = [30, 40, 50, 60]
print(stu)
print(stu.items())

for k, v in stu.items():
    print(k)
    print(v)
