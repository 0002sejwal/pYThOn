num = int(input("Enter the amount of numbers you want to add in the list : "))
list1 = []
output = []
for i in range(1, num+1):
    a = int(input(f"Enter the number to add on {i} position in the list : "))
    list1.append(a)


for j in list1:
    if j >= 1:
        output.append(j)

print(f"output : {output}")
