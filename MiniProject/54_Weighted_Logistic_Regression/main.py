import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download and extract data
# wget -q file_from_website.zip
# unzip -qq file.zip

# Load the dataset into a DataFrame
data = pd.read_csv('wdbc.data')

# Extract feature columns excluding the first two columns
features = data.iloc[:, [index for index, column in enumerate(data.columns) if index not in [0,1]]]

# Extract the target column (2nd column) and map 'M' to 1 and 'B' to 0
target = data.iloc[:,1]
target = target.map({'M':1,"B":0})

# Convert DataFrame to numpy arrays
features_array = features.to_numpy()
target_array = target.to_numpy().reshape(-1, 1)

# Split the dataset into training and testing subsets (80% training, 20% testing)
features_train, features_test, target_train, target_test = train_test_split(features_array, target_array, test_size=0.20, random_state=42)

# Initialize two logistic regression models with different class weights
model_1 = LogisticRegression(C=1.0, class_weight={0:15,1:0.2}, dual=False, fit_intercept=True,
                  intercept_scaling=1, l1_ratio=None, max_iter=100, n_jobs=None, penalty='l2',
                  random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                  warm_start=False)

model_2 = LogisticRegression(C=1.0, class_weight={0:0.1,1:650}, dual=False, fit_intercept=True,
                  intercept_scaling=1, l1_ratio=None, max_iter=100, n_jobs=None, penalty='l2',
                  random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                  warm_start=False)

# Train the models using the training data
model_1.fit(features_train, target_train)
model_2.fit(features_train, target_train)

# Predict the target for the test set using the trained models
predictions_1 = model_1.predict(features_test)
predictions_2 = model_2.predict(features_test)

# Compute accuracy for both models on the test set
accuracy_model_1 = accuracy_score(target_test, predictions_1)
accuracy_model_2 = accuracy_score(target_test, predictions_2)

# Display the accuracy results for both models
print(f"Accuracy for model_1: {accuracy_model_1 * 100:.2f}%")
print(f"Accuracy for model_2: {accuracy_model_2 * 100:.2f}%")
