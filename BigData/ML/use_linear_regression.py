from joblib import load
import pandas as pd

model = load('LinearRegression.joblib')
nuovo_dato = pd.DataFrame({'Experience': [5]}) 
predizione = model.predict(nuovo_dato)
print(f"\nPredizione per Experience=5: {predizione[0]:.2f}")