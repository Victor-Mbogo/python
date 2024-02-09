Maths = int(input("maths: "))
eng = int(input("eng: "))
phyc = int(input("phyc: "))
bio = int(input("bio: "))
hist = int(input("hist: "))

total = Maths + eng + phyc + bio + hist
mean = total / 5
print (f"average: {mean}")
if mean >= 0 and mean < 40:
    print("E")
elif mean > 40 and mean < 51:
    print("D")
elif mean >50 and mean < 61:
    print("C")
elif mean > 60 and mean < 71:
    print("B")
elif mean > 70 and mean <= 100:
    print("A")
else:
    print("invalid input")

# 0-39=E
# 40-50=D
# 51-60=C
# 61-70=B
# 70-100=A