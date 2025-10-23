# =============================================================================
# STEP 1: IMPORTARE LE LIBRERIE NECESSARIE
# =============================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("✅ Librerie importate con successo!")

# =============================================================================
# STEP 2: CARICARE IL DATASET DA CSV
# =============================================================================

# Leggiamo il file CSV e lo carichiamo in un DataFrame pandas
df = pd.read_csv('./dataset/dati_LogisticRegression.csv')

# Visualizziamo le prime 5 righe per capire la struttura dei dati
print("📊 ANTEPRIMA DEL DATASET:")
print(df.head())

# Controlliamo le informazioni generali sul dataset
print("\n📋 INFORMAZIONI DATASET:")
print(df.info())

# Verifichiamo le statistiche descrittive
print("\n📈 STATISTICHE DESCRITTIVE:")
print(df.describe())

# =============================================================================
# STEP 3: PULIZIA E PREPARAZIONE DEI DATI
# =============================================================================

# Controlliamo se ci sono valori mancanti
print("\n🔍 VALORI MANCANTI PER COLONNA:")
print(df.isnull().sum())

# Se ci fossero valori mancanti, potremmo gestirli così:
# df = df.dropna()  # Elimina righe con valori mancanti
# Oppure:
# df = df.fillna(df.mean())  # Riempie con la media

# SPIEGAZIONE COLONNE:
# age: Età del cliente
# balance: Saldo del conto
# estimated_salary: Stipendio stimato
# credit_score: Punteggio creditizio
# tenure: Anni di relazione con la banca
# number_of_products: Numero di prodotti bancari
# has_credit_card: Possiede carta di credito (1=Si, 0=No)
# is_active_member: Membro attivo (1=Si, 0=No)
# churn: Il cliente ha abbandonato? (1=Si, 0=No) ← TARGET

# Verifichiamo il bilanciamento delle classi target
print("\n⚖️ DISTRIBUZIONE DELLA VARIABILE TARGET (churn):")
print(df['churn'].value_counts())# Valori assoluti
print("Proporzioni:")
print(df['churn'].value_counts(normalize=True)) # Valori percentuali

# =============================================================================
# STEP 4: PREPARAZIONE DEI DATI PER IL MODELLO
# =============================================================================

# Separiamo le features (variabili indipendenti) dal target (variabile dipendente)
# X = tutte le colonne tranne 'churn'
# y = solo la colonna 'churn'

X = df.drop('churn', axis=1)  # axis=1 significa che stiamo eliminando una colonna
y = df['churn']

print("\n🎯 FEATURES (X):")
print(X.head())
print(f"Dimensione di X: {X.shape}")  # (numero_righe, numero_colonne)

print("\n🎯 TARGET (y):")
print(y.head())
print(f"Dimensione di y: {y.shape}")

# Dividiamo il dataset in training set (80%) e test set (20%)
# random_state=42 garantisce risultati riproducibili
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,       # 20% dei dati per il test
    random_state=42,     # Seed per riproducibilità
    stratify=y           # Mantiene la stessa proporzione di classi in train e test
)

print(f"\n📊 DIVISIONE DATASET:")
print(f"Training set: {X_train.shape[0]} righe")
print(f"Test set: {X_test.shape[0]} righe")

# =============================================================================
# STEP 5: NORMALIZZAZIONE DELLE FEATURES
# =============================================================================

# La regressione logistica beneficia della normalizzazione dei dati
# StandardScaler sottrae la media e divide per la deviazione standard
# Questo mette tutte le feature sulla stessa scala

scaler = StandardScaler()

# Addestriamo lo scaler SOLO sul training set e trasformiamo entrambi i set
X_train_scaled = scaler.fit_transform(X_train)  # fit_transform: impara parametri e applica
X_test_scaled = scaler.transform(X_test)        # transform: applica stessa trasformazione

print("\n📏 DATI NORMALIZZATI:")
print("Prime 5 righe del training set normalizzato:")
print(X_train_scaled[:5])

# =============================================================================
# STEP 6: CREAZIONE E ADDESTRAMENTO DEL MODELLO
# =============================================================================

# Creiamo l'istanza del modello di Regressione Logistica
model = LogisticRegression(
    random_state=42,     # Seed per riproducibilità
    max_iter=1000,       # Numero massimo di iterazioni per convergenza
    C=1.0,               # Parametro di regolarizzazione (più piccolo = più regolarizzazione)
    solver='lbfgs',      # Algoritmo di ottimizzazione (buono per dataset piccoli/medi)
    penalty='l2'         # Tipo di regolarizzazione (L2 = Ridge)
)

# Addestriamo il modello sui dati di training
print("\n🚀 ADDESTRAMENTO DEL MODELLO IN CORSO...")
model.fit(X_train_scaled, y_train)
print("✅ Modello addestrato con successo!")

# =============================================================================
# STEP 7: SPIEGAZIONE DETTAGLIATA DEI PARAMETRI
# =============================================================================

print("\n🎓 SPIEGAZIONE PARAMETRI DEL MODELLO:")

# Coefficienti delle feature (importanza di ogni feature)
coefficients = model.coef_[0]
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': coefficients,
    # 'Abs_Coefficient': np.abs(coefficients)
}).sort_values('Abs_Coefficient', ascending=False)

print("\n📊 IMPORTANZA DELLE FEATURE (Coefficienti):")
print(feature_importance)

# Interpretazione dei coefficienti:
print("\n💡 COME INTERPRETARE I COEFFICIENTI:")
print("• Coefficiente POSITIVO: Aumenta la probabilità di churn (abbandono)")
print("• Coefficiente NEGATIVO: Diminuisce la probabilità di churn")
print("• Valore ASSOLUTO più alto: Feature più influente")

# Intercetta (bias)
print(f"\n📐 INTERCETTA (bias): {model.intercept_[0]:.4f}")
print("L'intercetta rappresenta la probabilità logistica di base quando tutte le feature sono 0")

# =============================================================================
# STEP 8: VALUTAZIONE DEL MODELLO
# =============================================================================

# Facciamo previsioni sul test set
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)  # Probabilità per ogni classe

print("\n📈 VALUTAZIONE DEL MODELLO:")

# 1. Accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 ACCURATEZZA: {accuracy:.4f} ({accuracy*100:.2f}%)")

# 2. Matrice di confusione
print("\n📊 MATRICE DI CONFUSIONE:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# 3. Report di classificazione dettagliato
print("\n📋 REPORT DI CLASSIFICAZIONE:")
print(classification_report(y_test, y_pred))

# =============================================================================
# STEP 9: INTERPRETAZIONE DELLE PROBABILITÀ
# =============================================================================

# La regressione logistica fornisce probabilità, non solo classificazioni
print("\n🎲 PROBABILITÀ DI PREDIZIONE (prime 5 istanze del test set):")
probabilities_df = pd.DataFrame({
    'Probabilità Classe 0 (No Churn)': y_pred_proba[:, 0],
    'Probabilità Classe 1 (Churn)': y_pred_proba[:, 1],
    'Predizione Finale': y_pred,
    'Valore Reale': y_test.values
})
print(probabilities_df.head())

# =============================================================================
# STEP 10: UTILIZZO CONCRETO DEL MODELLO
# =============================================================================

print("\n🚀 UTILIZZO PRATICO DEL MODELLO:")

# Esempio: Prevedere se un NUOVO cliente abbandonerà
nuovo_cliente = pd.DataFrame({
    'age': [45],
    'balance': [60000],
    'estimated_salary': [90000],
    'credit_score': [620],
    'tenure': [4],
    'number_of_products': [2],
    'has_credit_card': [1],
    'is_active_member': [1]
})

# Preprocessing del nuovo cliente
nuovo_cliente_scaled = scaler.transform(nuovo_cliente)

# Previsione
probabilita_churn = model.predict_proba(nuovo_cliente_scaled)[0, 1]
predizione = model.predict(nuovo_cliente_scaled)[0]

print(f"\n🔮 PREVISIONE PER NUOVO CLIENTE:")
print(f"Probabilità di abbandono: {probabilita_churn:.4f} ({probabilita_churn*100:.2f}%)")
print(f"Predizione: {'ABBADONERÀ' if predizione == 1 else 'RIMARRÀ'}")

# Soglia di decisione (default 0.5, ma possiamo modificarla)
soglia_personalizzata = 0.3  # Più sensibile ai casi di churn
predizione_soglia = (probabilita_churn > soglia_personalizzata).astype(int)

print(f"\n🎚️ CON SOGLIA PERSONALIZZATA ({soglia_personalizzata}):")
print(f"Predizione: {'ABBADONERÀ' if predizione_soglia == 1 else 'RIMARRÀ'}")

# =============================================================================
# STEP 11: QUANDO USARE E NON USARE LA REGRESSIONE LOGISTICA
# =============================================================================

print("\n" + "="*60)
print("🎯 QUANDO USARE LA REGRESSIONE LOGISTICA:")
print("="*60)
print("✅ PROBLEMI DI CLASSIFICAZIONE BINARIA")
print("✅ INTERPRETABILITÀ DEL MODELLO IMPORTANTE")
print("✅ RELAZIONI APPROSSIMATIVAMENTE LINEARI")
print("✅ DATASET DI DIMENSIONI PICCOLE/MEDIE")
print("✅ BASELINE MODEL per confrontare modelli più complessi")

print("\n" + "="*60)
print("🚫 QUANDO NON USARE LA REGRESSIONE LOGISTICA:")
print("="*60)
print("❌ PROBLEMI DI CLASSIFICAZIONE MULTI-CLASSE (più di 2 categorie)")
print("❌ RELAZIONI COMPLESSE NON LINEARI")
print("❌ DATASET MOLTO GRANDI E COMPLESSI")
print("❌ FEATURE CON INTERAZIONI COMPLESSE")
print("❌ PERFORMANCE MASSIME RICHIESTE (usare XGBoost, Neural Networks)")
