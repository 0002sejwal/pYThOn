def frequent(string):  # string = {'r','a','j','a','t'}
    dicti = dict()  # { 'a' : 2, 'r' : 1 , 'j' : 1 , 't' : 1}
    for i in string:
        if i not in dicti:
            dicti[i] = 1
        else:
            dicti[i] += 1
    sorted_list = sorted(dicti, key=dicti.get, reverse=True)
    for r in sorted_list:
        print(r, dicti[r])
    # return sorted_list


name = input("Enter the name to check frequency of characters : ").lower()
frequent(name)
