number = int(input("Nhap vao n : "))
mydict = {}

for x in range(1, number + 1):
    mydict[x] = x * x

print("\nDictionary = ", mydict)

fullname = str(input("Nhap vao ho ten: "))
print(len(fullname))

mydict = {}
for x in range(1, len(fullname) + 1):
    mydict[x] = x * x

print("\nDictionary = ", mydict)