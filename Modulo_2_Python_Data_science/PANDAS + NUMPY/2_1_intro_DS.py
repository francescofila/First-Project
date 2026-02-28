import pandas as pd
import matplotlib.pyplot as plt

# ----------
# 1) Dataset esempio

dati = {'Settimana':[1,2,3,4,5,6,],
        'Vendite': [250, 300, 400, 350, 450, 500]}

# -  creiamo dataset di esempio

df = pd.DataFrame(dati)

print(df)

media_vendite = df['Vendite'].mean()

print("Media Vendite: ", media_vendite)

# - creiamo un grafico a barre

plt.bar(df['Settimana'], df['Vendite'], color='orange')
plt.axhline(media_vendite, color='red', linestyle='--', label='Media')
plt.xlabel('Settimana')
plt.ylabel("Vendite")
plt.title("Vendite Settimanali")
plt.legend()
plt.show()


idx
