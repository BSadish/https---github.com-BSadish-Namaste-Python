thisdict = {
  "brand": "ford",
  "model": "Mustang",
  "country":"America"
  
}
dict=input("Take a key value form user: ")
if dict in thisdict:
    print('The value is:', thisdict[dict])
else:
    print('That key is not in the dictionary.')
