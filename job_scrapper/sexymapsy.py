import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
print(passengers)

# Update sex column to numerical
# Map "female" to 1 and "male" to 0 in the Sex column
passengers['Sex'] = passengers['Sex'].map({'female': 1, 'male': 0})

# Fill the nan values in the age column
#print(passengers['Age'].values)
mean_age = passengers['Age'].mean()
passengers['Age'] = passengers['Age'].fillna(mean_age)

# Create a first class column let’s utilize the Pclass column, or the passenger class, as another feature. Create a new column named FirstClass that stores 1 for all passengers in first class and 0 for all other passengers.
passengers['FirstClass'] = (passengers['Pclass'] == 1).astype(int)
