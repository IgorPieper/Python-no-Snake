import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

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
clf_1.fit(X_train, y_train)
clf_2.fit(X_train, y_train)

# clf_1
probs_clf_1 = clf_1.predict_proba(X_test)[:, 1]

# clf_2
probs_clf_2 = clf_2.predict_proba(X_test)[:, 1]


def find_optimal_threshold(probs, true_labels):
    # Initialization of values
    best_threshold = 0
    best_f1 = 0

    # Test various potential threshold values
    for threshold in np.linspace(0, 1, 100):
        # Apply thresholding
        predictions = (probs > threshold).astype(int)

        # Calculate F1 score
        f1 = f1_score(true_labels, predictions)

        # If the new F1 score is better, update the best values
        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold

    return best_threshold, best_f1


# For clf_1
best_threshold_clf_1, best_f1_clf_1 = find_optimal_threshold(probs_clf_1, y_test)
print(f"Optimal threshold for clf_1: {best_threshold_clf_1:.3f}, F1 score: {best_f1_clf_1:.3f}")

# For clf_2
best_threshold_clf_2, best_f1_clf_2 = find_optimal_threshold(probs_clf_2, y_test)
print(f"Optimal threshold for clf_2: {best_threshold_clf_2:.3f}, F1 score: {best_f1_clf_2:.3f}")
