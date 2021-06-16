fn= input("Enter Filename: ")
myDict={"py":"python","java":"java","txt":"text","doc":"document","c":"c","cpp":"c++/c plus plus"}
f = fn.split(".")
print ("Extension of the file is : " + myDict[f[-1]])
