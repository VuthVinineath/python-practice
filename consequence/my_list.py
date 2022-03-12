from ast import While


lst = ["student 1", "student 2", "student 3"]
print("======== Before change ========\n")
print(lst[0])
print("======== After change =========\n")
lst[0] = "student A"
print(lst[0])
print("-------- sort ---------\n")
lst.sort()
print(lst)
print("------- reverse sort --------------\n")
lst.sort(reverse=True)
print(lst)
print("------- add more list ----------\n")
lst.append("Student 5")
print(lst)
print("------ delete element from list ------\n")
del lst[3]
print(lst)
print("-----------------------------------------------------------------------------------")
lst1 = ["student 9"]
main_lst = lst1 + lst
print(main_lst)
