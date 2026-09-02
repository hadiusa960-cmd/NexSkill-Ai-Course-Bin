bookset = {458 , "patroitism" , "nepolian" , 85.2}
print(bookset)
print(type(bookset))
print(len(bookset))
for i in bookset:
    print(i)
bookset.add(45)
print(bookset)
bookset.discard(458)
print(bookset)