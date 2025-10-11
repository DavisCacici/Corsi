import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Creiamo un esempio pratico con feature su scale diverse
print("🔍 ESEMPIO PRATICO CON FEATURE SU SCALE DIVERSE:")

# Dataset di esempio: età (20-60) vs stipendio (30,000-100,000)
data_esempio = {
    'age': [25, 30, 35, 40, 45, 50, 55, 60],
    'salary': [30000, 45000, 60000, 75000, 90000, 80000, 95000, 100000]
}

df_esempio = pd.DataFrame(data_esempio)
print("\n📊 DATASET ORIGINALE:")
print(df_esempio)
print(f"\nMedia - Age: {df_esempio['age'].mean():.2f}, Salary: {df_esempio['salary'].mean():.2f}")
print(f"Deviazione Standard - Age: {df_esempio['age'].std():.2f}, Salary: {df_esempio['salary'].std():.2f}")

# =============================================================================
# STEP 1: CREAZIONE DELLO SCALER
# =============================================================================

scaler = StandardScaler()
print(f"\n🎯 CREATO STANDARDSCALER: {scaler}")

# Spiegazione: StandardScaler() crea un "trasformatore" vuoto
# Non ha ancora imparato nulla sui dati, è come un insegnante senza esperienza

# =============================================================================
# STEP 2: FIT_TRANSFORM SUL TRAINING SET
# =============================================================================

# Simuliamo un training set (primi 6 samples)
X_train_esempio = df_esempio.head(6)
print(f"\n🎓 TRAINING SET (primi 6 samples):")
print(X_train_esempio)

# FIT_TRANSFORM: due operazioni in una!
X_train_scaled = scaler.fit_transform(X_train_esempio)

print(f"\n🔥 COSA SUCCEDE CON FIT_TRANSFORM:")

# Calcoliamo manualmente per capire
mean_age = X_train_esempio['age'].mean()
std_age = X_train_esempio['age'].std()
mean_salary = X_train_esempio['salary'].mean()
std_salary = X_train_esempio['salary'].std()

print(f"📊 PARAMETRI IMPARATI DAL TRAINING SET:")
print(f"Age - Media: {mean_age:.2f}, Dev.Std: {std_age:.2f}")
print(f"Salary - Media: {mean_salary:.2f}, Dev.Std: {std_salary:.2f}")

# Trasformazione manuale del primo sample
primo_sample = X_train_esempio.iloc[0]
age_scaled_manual = (primo_sample['age'] - mean_age) / std_age
salary_scaled_manual = (primo_sample['salary'] - mean_salary) / std_salary

print(f"\n🧮 TRASFORMAZIONE MANUALE DEL PRIMO SAMPLE:")
print(f"Age originale: {primo_sample['age']} → Scaled: {age_scaled_manual:.4f}")
print(f"Salary originale: {primo_sample['salary']} → Scaled: {salary_scaled_manual:.4f}")

print(f"\n✅ RISULTATO FIT_TRANSFORM:")
print(X_train_scaled)

# =============================================================================
# STEP 3: TRANSFORM SUL TEST SET
# =============================================================================

# Simuliamo un test set (ultimi 2 samples)
X_test_esempio = df_esempio.tail(2)
print(f"\n🧪 TEST SET (ultimi 2 samples):")
print(X_test_esempio)

# TRANSFORM: usa i parametri già imparati dal training set!
X_test_scaled = scaler.transform(X_test_esempio)

print(f"\n🔧 COSA SUCCEDE CON TRANSFORM:")
print("USA GLI STESSI PARAMETRI DEL TRAINING SET!")

# Trasformazione manuale del primo sample del test set
primo_test = X_test_esempio.iloc[0]
age_test_scaled = (primo_test['age'] - mean_age) / std_age  # Stessa media del training!
salary_test_scaled = (primo_test['salary'] - mean_salary) / std_salary  # Stessa dev.std del training!

print(f"\n🧮 TRASFORMAZIONE MANUALE DEL TEST SET:")
print(f"Age test: {primo_test['age']} → Scaled: {age_test_scaled:.4f}")
print(f"Salary test: {primo_test['salary']} → Scaled: {salary_test_scaled:.4f}")

print(f"\n✅ RISULTATO TRANSFORM SUL TEST SET:")
print(X_test_scaled)

# =============================================================================
# VISUALIZZAZIONE DELLA TRASFORMAZIONE
# =============================================================================

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))

# Prima della standardizzazione
plt.subplot(1, 3, 1)
plt.scatter(df_esempio['age'], df_esempio['salary'], color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Prima della Standardizzazione\n(Scale Diverse)')
plt.grid(True, alpha=0.3)

# Dopo la standardizzazione
plt.subplot(1, 3, 2)
# Combiniamo train e test scaled
all_scaled = np.vstack([X_train_scaled, X_test_scaled])
plt.scatter(all_scaled[:, 0], all_scaled[:, 1], color='red', alpha=0.7)
plt.xlabel('Age (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.title('Dopo la Standardizzazione\n(Stessa Scala)')
plt.grid(True, alpha=0.3)

# Confronto distribuzioni
plt.subplot(1, 3, 3)
plt.hist(df_esempio['age'], alpha=0.7, label='Age Original', bins=8)
plt.hist(df_esempio['salary']/1000, alpha=0.7, label='Salary/1000 Original', bins=8)
plt.hist(all_scaled[:, 0], alpha=0.7, label='Age Scaled', bins=8)
plt.hist(all_scaled[:, 1], alpha=0.7, label='Salary Scaled', bins=8)
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.title('Confronto Distribuzioni')
plt.legend()

plt.tight_layout()
plt.show()

# =============================================================================
# PERCHÉ È COSÌ CRITICO USARE SOLO FIT_TRANSFORM SUL TRAINING?
# =============================================================================

print("\n" + "="*70)
print("🚨 IL PERICOLO DEL DATA LEAKAGE")
print("="*70)

# Cosa succederebbe se usassimo fit_transform su tutto il dataset?
print("\n❌ SCENARIO SBAGLIATO: Fit su tutto il dataset")
scaler_sbagliato = StandardScaler()
X_tutto_scaled_sbagliato = scaler_sbagliato.fit_transform(df_esempio)

print("Parametri imparati su TUTTI i dati (train + test):")
print(f"Media Age: {scaler_sbagliato.mean_[0]:.2f}")
print(f"Media Salary: {scaler_sbagliato.mean_[1]:.2f}")

print("\n💀 PROBLEMA: Il modello ha visto i dati di test durante il training!")
print("   La valutazione sarà troppo ottimistica e non realistica")
print("   È come dare le risposte dell'esame prima della verifica!")

# Confronto con l'approccio corretto
print(f"\n✅ SCENARIO CORRETTO: Fit solo sul training")
print(f"Media Age (solo training): {mean_age:.2f}")
print(f"Media Salary (solo training): {mean_salary:.2f}")

print("\n🎯 VANTAGGIO: Valutazione realistica delle performance del modello")
print("   Il modello viene testato su dati completamente nuovi")

# =============================================================================
# COSA SUCCEDE NEI MODELLI DI MACHINE LEARNING?
# =============================================================================

print("\n" + "="*70)
print("🤖 PERCHÉ LA REGRESSIONE LOGISTICA HA BISOGNO DI SCALING?")
print("="*70)

print("""
La Regressione Logistica utilizza una funzione sigmoide:

P(y=1) = 1 / (1 + e^(-(β₀ + β₁x₁ + β₂x₂ + ...)))

📌 SENZA SCALING:
- Feature con scale grandi (es. stipendio: 30,000) dominano quelle con scale piccole (es. età: 30)
- I coefficienti β saranno distorti
- L'algoritmo di ottimizzazione converge più lentamente
- Il modello può non funzionare bene

📌 CON SCALING:
- Tutte le feature contribuiscono equamente
- I coefficienti β sono più interpretabili
- Convergenza più rapida e stabile
- Performance migliori
""")

# Dimostrazione con coefficienti
from sklearn.linear_model import LogisticRegression

# Senza scaling
model_senza_scaling = LogisticRegression()
model_senza_scaling.fit(X_train_esempio, [0, 1, 0, 1, 0, 1])  # Target fittizio

# Con scaling
model_con_scaling = LogisticRegression()
model_con_scaling.fit(X_train_scaled, [0, 1, 0, 1, 0, 1])

print(f"\n🔍 CONFRONTO COEFFICIENTI:")
print("Senza scaling - Age: {:.4f}, Salary: {:.4f}".format(
    model_senza_scaling.coef_[0][0], 
    model_senza_scaling.coef_[0][1]
))
print("Con scaling - Age: {:.4f}, Salary: {:.4f}".format(
    model_con_scaling.coef_[0][0], 
    model_con_scaling.coef_[0][1]
))

print("\n💡 Nota: Con lo scaling, i coefficienti sono più bilanciati!")

# =============================================================================
# BEST PRACTICES E TRAPPOLE COMUNI
# =============================================================================

print("\n" + "="*70)
print("⭐ BEST PRACTICES PER LO STANDARDSCALER")
print("="*70)

print("""
1. ✅ SEMPRE: fit_transform solo sul training set
2. ✅ SEMPRE: transform sul test set (usando i parametri del training)
3. ✅ RICORDA: Salva lo scaler per future predizioni
4. ✅ ATTENZIONE: Applica lo scaling dopo la divisione train/test

5. ❌ MAI: fit_transform sul test set
6. ❌ MAI: fit su tutto il dataset prima di dividere
7. ❌ MAI: Dimenticare di scalare nuove predizioni
""")

# Esempio di pipeline corretta per nuove predizioni
print("\n🔮 COME USARE LO SCALER PER NUOVE PREDIZIONI:")

# Salviamo lo scaler addestrato (importante per production!)
import joblib
joblib.dump(scaler, 'scaler_trained.pkl')

# Simuliamo un nuovo cliente
nuovo_cliente = np.array([[38, 65000]])  # Age, Salary
print(f"Nuovo cliente originale: {nuovo_cliente}")

# Carichiamo lo scaler salvato (in production)
scaler_caricato = joblib.load('scaler_trained.pkl')
nuovo_cliente_scaled = scaler_caricato.transform(nuovo_cliente)

print(f"Nuovo cliente scaled: {nuovo_cliente_scaled}")

# =============================================================================
# ALTERNATIVE A STANDARDSCALER
# =============================================================================

print("\n" + "="*70)
print("🔄 ALTERNATIVE A STANDARDSCALER")
print("="*70)

from sklearn.preprocessing import MinMaxScaler, RobustScaler

# MinMaxScaler: Scala tra 0 e 1
minmax_scaler = MinMaxScaler()
X_minmax = minmax_scaler.fit_transform(X_train_esempio)
print(f"\n📊 MinMaxScaler - Trasforma in range [0, 1]")
print(X_minmax)

# RobustScaler: Usa mediana e IQR (robusto agli outliers)
robust_scaler = RobustScaler()
X_robust = robust_scaler.fit_transform(X_train_esempio)
print(f"\n🛡️ RobustScaler - Robusto agli outliers")
print(X_robust)

print("""
🎯 QUANDO USARE CIASCUNO:

• StandardScaler: 
  - Dati normalmente distribuiti
  - Assenza di outliers estremi
  - Caso generale

• MinMaxScaler:
  - Algoritmi sensibili alla scala (es. Neural Networks)
  - Quando serve range fisso [0,1]

• RobustScaler:
  - Presenza di outliers
  - Dati non normalmente distribuiti
""")

# =============================================================================
# RIASSUMENDO: PERCHÉ QUESTA PROCEDURA È COSÌ IMPORTANTE?
# =============================================================================

print("\n" + "="  +70)
print("🎯 RIASSUMENDO: I 3 PUNTI CHIAVE")
print("="+70)

print("""
1. 🚨 EVITARE DATA LEAKAGE:
   - Il test set deve rimanere "invisibile" durante il training
   - fit_transform solo su training, transform su test

2. ⚖️ BILANCIARE LE FEATURE:
   - Feature con scale diverse ingannano gli algoritmi
   - Lo scaling dà uguale importanza a tutte le feature

3. 🚀 MIGLIORARE PERFORMANCE:
   - Convergenza più rapida degli algoritmi
   - Coefficienti più interpretabili
   - Performance più stabili
""")

print(f"\n💡 NEL NOSTRO ESEMPIO:")
print(f"   Training set: {X_train_scaled.shape} samples")
print(f"   Test set: {X_test_scaled.shape} samples")
print(f"   Entrambi scalati con gli stessi parametri del training!")

print("\n🎉 ORA HAI CAPITO PERFETTAMENTE LO STANDARDSCALER!")