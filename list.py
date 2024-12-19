num=[10,20,30,40,10]
print(num)
num.append(12)  #Added in the last of the list
num.insert(3,44) #Insert new value in the index 3 i.e num[3]
num.remove(10) #Removing the element
print("After removing",num)
print("Before poping:",num)
num.pop(2)
print("After Poping:",num)
num.sort()
print(num)