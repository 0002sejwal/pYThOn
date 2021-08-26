position = int(input("please enter the position : "))

n1, n2 = 0, 1
count = 0

if position <= 0:
    print("please enter a positive integer: ")
elif position == 1:
    # print(f"The fibbonaci series at given position is : {n2}")
    print("The fibbonaci series at given position is : ", n2)
else:
    print("The Series Will be ")
    # let position input is 8
    while count < position:
        print(n1)
        n_value = n1+n2

        # Value updation

        n1 = n2
        n2 = n_value

        count += 1
