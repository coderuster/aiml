import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df = pd.read_csv('data.csv')
df.head()


X = df.drop('diabetes', axis=1).values
y = df['diabetes'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
print(X_train)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy: {accuracy:.2%}")

test_person = np.array([[80, 100]])
test_person_diabetes = model.predict(test_person)
if test_person_diabetes[0] == 1:
    print("Diabetes positive")
else:
    print("Diabetes negative")
