import pandas as pd
import numpy as np



# generate X and y 1000 samples
size = 1000
X = pd.DataFrame()
X['temprature_outside'] = np.random.randint(10,40, size = size)
X['air_conditioning'] = np.random.randint(0,2, size=size)
y = X.apply(lambda row: 
            row['temprature_outside'] + 10* row['air_conditioning'] 
            if row['temprature_outside'] < 25 
            else row['temprature_outside'] - 10* row['air_conditioning'], axis=1)
y = ['Hot' if v > 25 else 'Cold' for v in y]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression().fit(X_train, y_train)


print(pd.DataFrame({'temprature_outside': X_test['temprature_outside'], 
              'air_conditioning': X_test['air_conditioning'], 
              'Ground Truth': y_test, 
              'Prediction': clf.predict(X_test)})[:10])

print(clf.score(X_test, y_test))



