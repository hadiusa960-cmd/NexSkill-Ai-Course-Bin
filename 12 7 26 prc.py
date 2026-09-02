import numpy as np

ids,price,longitude,lat=np.genfromtxt('data.csv',delimiter=';', usecols=(0,4,8,9), unpack=True, dtype=None,skip_header=1)


print(ids)
print(price)
print(longitude)
print(lat)

print(np.min(price))  
print(np.max(price))
print(np.mean(price))
print(np.std(price))