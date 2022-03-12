s1 = int(input("Input s1: "))
s2 = int(input("Input s2: "))
s3 = int(input("Input s3: "))
avg = round((s1+s2+s3)/3)
print("Average score is : ", avg)

if avg >= 90 and avg <= 100:
    if avg >= 95 and avg <= 100:
        print("Grade A+")
    elif avg >= 93 and avg < 95:
        print("Grade A-")
    else:
        print("Grade A")
elif avg >= 80 and avg < 90:
    print("Grade B")
elif avg >= 70 and avg < 80:
    print("Grade C")
elif avg >= 60 and avg < 70:
    print("Grade D")
elif avg >= 50 and avg < 60:
    print("Grade E")
else:
    print("Grade F")
