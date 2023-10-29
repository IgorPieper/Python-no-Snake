import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

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
features_train, features_test, target_train, target_test = train_test_split(features_array, target_array,
                                                                            test_size=0.20, random_state=42)

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

# Precision calculation, recall and F1
precision_model_1 = precision_score(target_test, predictions_1)
recall_model_1 = recall_score(target_test, predictions_1)
f1_model_1 = f1_score(target_test, predictions_1)

precision_model_2 = precision_score(target_test, predictions_2)
recall_model_2 = recall_score(target_test, predictions_2)
f1_model_2 = f1_score(target_test, predictions_2)

# Answers
print(f"Precyzja dla model_1: {precision_model_1:.2f}")
print(f"Recall dla model_1: {recall_model_1:.2f}")
print(f"F1 dla model_1: {f1_model_1:.2f}\n")

print(f"Precyzja dla model_2: {precision_model_2:.2f}")
print(f"Recall dla model_2: {recall_model_2:.2f}")
print(f"F1 dla model_2: {f1_model_2:.2f}\n")

# Precision and recall comparison
if precision_model_1 > precision_model_2:
    print("Model_1 ma wyższą precyzję.")
else:
    print("Model_2 ma wyższą precyzję.")

if recall_model_1 > recall_model_2:
    print("Model_1 ma wyższy recall.")
else:
    print("Model_2 ma wyższy recall.")
