from xml.parsers.expat import model

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df = pd.read_csv('AB_NYC_2019.csv')
print(df)

df.plot.scatter(x='minimum_nights', y='price', title='0.55')
plt.show()

#input("wait...")

y = df['price'].values.reshape(-1,1)
x = df['minimum_nights'].values.reshape(-1,1)


print("y: " ,y)
print("x: " ,x)
SEED = 44
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 44)

print(x_train)
print(y_train)

print(x_test)
print(y_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression

regressor.fit(x_train,y_train)

print(regressor.intercept_)

print(regressor.intercept_)

print(regressor.coef_)

def calc(slope,intercept,minimum_nights):
       return slope*hours+intercept


score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 




score = regressor.predict([[9.5]])

print(score)





