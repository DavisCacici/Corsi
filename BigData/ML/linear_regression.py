# Import library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from joblib import dump

# 1. Load data from csv
df = pd.read_csv('./dataset/dati_regression.csv') 

# 2. Explor data
print("Prime righe del dataset:")
print(df.head())
print("\nInformazioni sul dataset:")
print(df.info())
print("\nStatistiche descrittive:")
print(df.describe())

# 3. Prepare Data
X = df[['Experience']]  # feature
y = df['Salary']        # target

# 4. Divide in training and test set 
# 80% training set and 20% test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)
# Save model
dump(model, "first_model.joblib")
# Load model
# model = load('first_model.joblib')
# 6. Predict on test set
y_pred = model.predict(X_test)

# 7. Valuate model
print("\n=== VALUTAZIONE DEL MODELLO ===")
"""
The coefficient represents the change in the dependent variable 
for each one-unit increase in the independent variable. 
In this case, it shows how much the salary increases for each additional year of experience.
"""
print(f"Coefficiente (pendenza): {model.coef_[0]:.2f}")
"""
The intercept represents the value of the dependent variable (salary) 
when the independent variable (experience) is zero. 
It's the point where the regression line crosses the Y-axis.
"""
print(f"Intercetta: {model.intercept_:.2f}")
"""
R-squared (R²) measures how well the model fits the data. 
It ranges from 0 to 1, where 1 indicates a perfect fit.
"""
print(f"R-quadro (R²): {r2_score(y_test, y_pred):.2f}")
"""
MAE measures the average magnitude of errors between predicted and actual values. 
It's easy to interpret because it's in the same units as the target variable.
"""
print(f"Errore medio assoluto (MAE): {mean_absolute_error(y_test, y_pred):.2f}")
"""
MSE calculates the average of squared errors, 
penalizing larger errors more heavily. 
In squared units of the target variable.
"""
print(f"Errore quadratico medio (MSE): {mean_squared_error(y_test, y_pred):.2f}")

# 8. Create DataFrame for comparison prediction vs real data
results = pd.DataFrame({
    'Valore Reale': y_test,
    'Predetto': y_pred,
    'Differenza': y_test - y_pred
})
print("\nConfronto predizioni vs valori reali:")
print(results.head())

# 9. Example of prediction on new data
# nuovo_dato = pd.DataFrame({'Experience': [5]}) 
# predizione = model.predict(nuovo_dato)
# print(f"\nPredizione per Experience=5: {predizione[0]:.2f}")