# =============================================================================
# MULTIPLE LINEAR REGRESSION FOR HOUSE PRICE PREDICTION
# Simplified version without numpy and matplotlib
# =============================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =============================================================================
# STEP 1: LOAD AND EXPLORE THE DATASET
# =============================================================================
print("\n" + "=" * 70)
print("STEP 1: LOADING AND EXPLORING THE DATASET")
print("=" * 70)

# Load the dataset from CSV file
df = pd.read_csv('./dataset/dati_multiple_regression.csv')

print("\nBasic statistics for numerical columns:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# =============================================================================
# STEP 2: PREPARE DATA FOR MODELING
# =============================================================================
print("\n" + "=" * 70)
print("STEP 2: PREPARING DATA FOR MULTIPLE LINEAR REGRESSION")
print("=" * 70)

"""
MULTIPLE LINEAR REGRESSION EXPLANATION:
----------------------------------------
Multiple Linear Regression uses several features (independent variables)
to predict a target (dependent variable).

In our case:
- FEATURES (what we use to make predictions):
  * house_size_sqft
  * bedrooms
  * bathrooms
  * house_age_years
  * distance_to_city_miles

- TARGET (what we want to predict):
  * price_dollars

The regression model will find the best mathematical relationship:
Price = b0 + b1×size + b2×bedrooms + b3×bathrooms + b4×age + b5×distance
"""

# Select features (X) and target (y)
features = ['house_size_sqft', 'bedrooms', 'bathrooms', 'house_age_years', 'distance_to_city_miles']
X = df[features]  # Independent variables
y = df['price_dollars']  # Dependent variable (what we want to predict)


# Split data into training and testing sets
# We use 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
)


# =============================================================================
# STEP 3: CREATE AND TRAIN THE REGRESSION MODEL
# =============================================================================
print("\n" + "=" * 70)
print("STEP 3: TRAINING THE MULTIPLE LINEAR REGRESSION MODEL")
print("=" * 70)

# Create the Linear Regression model
model = LinearRegression()

print("Training the model...")
# Train the model using our training data
model.fit(X_train, y_train)

print("✓ Model training completed!")

# Display the model coefficients
print("\nMODEL COEFFICIENTS (What the model learned):")
print(f"Intercept (base price): ${model.intercept_:,.2f}")
print("\nFeature coefficients (how each feature affects price):")
for feature, coefficient in zip(features, model.coef_):
    effect = "increases" if coefficient > 0 else "decreases"
    print(f"  {feature:25} : ${coefficient:,.2f} (price {effect} by this amount per unit)")

# Explain what coefficients mean
print("\nINTERPRETING COEFFICIENTS:")
print("• POSITIVE coefficient: When this feature increases, price INCREASES")
print("• NEGATIVE coefficient: When this feature increases, price DECREASES")
print("• The number shows how much price changes for each 1-unit change in the feature")

# =============================================================================
# STEP 4: EVALUATE MODEL PERFORMANCE
# =============================================================================
print("\n" + "=" * 70)
print("STEP 4: EVALUATING MODEL PERFORMANCE")
print("=" * 70)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5  # Square root of MSE
r2 = r2_score(y_test, y_pred)

print("MODEL PERFORMANCE ON TEST DATA:")
print(f"Mean Absolute Error (MAE)    : ${mae:,.2f}")
print(f"Mean Squared Error (MSE)     : ${mse:,.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"R-squared (R²)               : {r2:.4f}")

# Explain what each metric means
print("\nWHAT THESE METRICS MEAN:")
print("• MAE: Average absolute difference between predicted and actual prices")
print("• RMSE: Similar to MAE, but gives more weight to large errors")
print("• R²: Percentage of price variation explained by the model (0-1 scale)")

print(f"\nThe model explains {r2*100:.1f}% of the variation in house prices")
print(f"Average prediction error: ${mae:,.2f}")

