#cannot be mutuable, repeated, 
a=(3,4,5,6,7,8)
print(a[3])   #index
print(len(a))  #length

print(a[1:5])

b=(3,3,45,6,6)
# y=b+[4] tuple is unmutuable
c=(4,5,7,8)

sum=b+c  # This is the way which is indirect way to change value in tuple
print(sum)