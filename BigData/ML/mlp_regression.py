import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# ✅ RELAZIONI NON LINEARI presenti nel dataset:

# 1. Temperatura vs Consumo: relazione a U (riscaldamento + raffreddamento)
# 2. Ora del giorno: pattern ciclico non lineare
# 3. Interazioni complesse: temperatura × umidità × occupazione
# 4. Pattern stagionali e giornalieri
# 5. Effetti soglia (es: sotto 0°C consumo aumenta esponenzialmente)

# Carica il dataset
df = pd.read_csv('./dataset/dati_MLPRegression.csv')

print(df.info())

# Prepara i dati per MLPRegressor
X = df.drop('consumo_energia', axis=1)
y = df['consumo_energia']

# Scala i dati (ESSENZIALE per neural networks)
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.values.reshape(-1, 1)).ravel()

# Split dei dati
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)
mlp = MLPRegressor(
    hidden_layer_sizes=(100, 50, 25),
    activation='relu',
    solver='adam',
    alpha=0.001,
    learning_rate='adaptive',
    max_iter=2000,
    early_stopping=True,
    random_state=42
)

mlp.fit(X_train, y_train)

y_pred_scaled = mlp.predict(X_test)
y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
y_test_original = scaler_y.inverse_transform(y_test.reshape(-1, 1)).ravel()

print(f"R² Score: {r2_score(y_test_original, y_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test_original, y_pred):.2f} kWh")
print(f"Accuracy: {mlp.score(X_test, y_test):.4f}")



# 📈 ESEMPI REALI dove MLPRegressor eccelle:

# 1. PREVISIONI FINANZIARIE
# - Prezzo azionari, forex, cryptocurrencies
# - Pattern temporali complessi

# 2. ENGINEERING E FISICA
# - Modellazione sistemi non-lineari
# - Simulazioni complesse

# 3. SENSOR DATA
# - Previsione qualità dell'aria
# - Analisi segnali sensori industriali

# 4. MARKETING AVANZATO
# - Previsione vendite con molte variabili
# - Customer lifetime value prediction