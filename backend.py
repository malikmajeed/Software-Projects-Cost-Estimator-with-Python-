import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv('Software_Project_Cost_Estimator_Dataset.csv')

# Display basic info
print(data.head())

# Split into features (X) and target (y)
X = data[['Lines_of_Code', 'Complexity', 'Team_Experience', 'Development_Time']]
y = data['Cost']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#------------------------------------------------------------------------------
#Visualization

# Visualize relationships
sns.pairplot(data, diag_kind='kde')
plt.show()

# Heatmap for correlations
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

