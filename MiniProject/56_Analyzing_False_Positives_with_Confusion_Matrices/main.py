import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# wget -q file_from_website.zip
# unzip -qq file.zip

# Read the dataset into a pandas DataFrame
df = pd.read_csv('wdbc.data')

# Extract features (columns) excluding the first two columns
x = df.iloc[:, [j for j, c in enumerate(df.columns) if j not in [0,1]]]

# Extract target variable (2nd column) and map 'M' to 1 and 'B' to 0
y = df.iloc[:,1]
y = y.iloc[:].map({'M':1,"B":0})

# Convert DataFrame to numpy arrays
x = x.to_numpy()
y = y.to_numpy().reshape(-1, 1)

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Initialize two logistic regression classifiers with different class weights
clf_1 = LogisticRegression(C=1.0, class_weight={0:15,1:0.2}, dual=False, fit_intercept=True,
                  intercept_scaling=1, l1_ratio=None, max_iter=100, n_jobs=None, penalty='l2',
                  random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                  warm_start=False)

clf_2 = LogisticRegression(C=1.0, class_weight={0:0.1,1:650}, dual=False, fit_intercept=True,
                  intercept_scaling=1, l1_ratio=None, max_iter=100, n_jobs=None, penalty='l2',
                  random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                  warm_start=False)

# Train the classifiers on the training data
clf_1.fit(X_train,y_train)
clf_2.fit(X_train,y_train)

# Predict the target variable on the testing set using the trained classifiers
y_pred_1 = clf_1.predict(X_test)
y_pred_2 = clf_2.predict(X_test)

# Calculate confusion matrices for both classifiers
matrix_clf_1 = confusion_matrix(y_test, y_pred_1)
matrix_clf_2 = confusion_matrix(y_test, y_pred_2)

# Plot confusion matrix for clf_1
plt.figure(figsize=(8, 6))
sns.heatmap(matrix_clf_1, annot=True, cmap='Blues', fmt='g')
plt.title('Confusion Matrix for clf_1')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Plot confusion matrix for clf_2
plt.figure(figsize=(8, 6))
sns.heatmap(matrix_clf_2, annot=True, cmap='Blues', fmt='g')
plt.title('Confusion Matrix for clf_2')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Determine classifier with more false positives
fp_clf_1 = matrix_clf_1[0][1]
fp_clf_2 = matrix_clf_2[0][1]

if fp_clf_1 > fp_clf_2:
    print("Classifier clf_1 has more false positives.")
else:
    print("Classifier clf_2 has more false positives.")

