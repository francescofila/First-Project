"""
Esercizio 1:
- 3 serie temporali con trend diversi + rumore (NumPy)
- DataFrame Pandas
- Media mobile e deviazione standard (7 e 14 giorni)
- Unico grafico con linee, marker e bande di deviazione
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# --- helper: banda ±STD robusta con DateTimeIndex ---
def fill_band(ax, x_dt, center, spread, alpha=0.12, color=None, label=None):
    """
    ax: Axes
    x_dt: DatetimeIndex o array di datetime
    center: Series/array (es. MA)
    spread: Series/array (es. STD)
    """
    center = pd.Series(center, index=x_dt)
    spread = pd.Series(spread, index=x_dt)

    mask = center.notna() & spread.notna()
    if not mask.any():
        return

    x_num = mdates.date2num(x_dt[mask].to_pydatetime())
    y1 = (center - spread)[mask].to_numpy()
    y2 = (center + spread)[mask].to_numpy()

    ax.fill_between(x_num, y1, y2, alpha=alpha, color=color, label=label)
    ax.xaxis_date()


def build_esercizio_1(rng, start="2025-01-01", n=120, windows=(7, 14)):
    dates = pd.date_range(start, periods=n, freq="D")
    t = np.arange(n)

    # Tre trend diversi (più “realistico” e controllato)
    s_up   = 60 + 0.20*t + rng.normal(0, 2.0, n)
    s_wave = 40 + 5*np.sin(2*np.pi*t/30) + rng.normal(0, 2.5, n)
    s_down = 50 - 0.15*t + rng.normal(0, 3.0, n)

    df = pd.DataFrame({"Up": s_up, "Wave": s_wave, "Down": s_down}, index=dates)

    for col in df.columns:
        for w in windows:
            df[f"{col}_MA{w}"] = df[col].rolling(w).mean()
            df[f"{col}_STD{w}"] = df[col].rolling(w).std()

    return df


def build_esercizio_2_classe(rng, start="2025-01-01", n=90):
    dates = pd.date_range(start, periods=n, freq="D")

    # Versione “classe”: trend lineari via linspace + rumore
    s1 = np.linspace(50, 100, n) + rng.normal(0, 5, n)
    s2 = np.linspace(20, 60, n)  + rng.normal(0, 8, n)
    s3 = 80 + 10*np.sin(np.linspace(0, 6*np.pi, n)) + rng.normal(0, 3, n)

    df = pd.DataFrame({"S1": s1, "S2": s2, "S3": s3}, index=dates)

    # Tipico in classe: min_periods=1 (niente NaN iniziali, ma primi punti “fragili”)
    df["S1_MA7"] = df["S1"].rolling(7, min_periods=1).mean()
    df["S1_STD7"] = df["S1"].rolling(7, min_periods=1).std()

    df["S2_MA7"] = df["S2"].rolling(7, min_periods=1).mean()
    df["S2_STD7"] = df["S2"].rolling(7, min_periods=1).std()

    df["S3_MA7"] = df["S3"].rolling(7, min_periods=1).mean()
    df["S3_STD7"] = df["S3"].rolling(7, min_periods=1).std()

    return df


def main():
    rng = np.random.default_rng(42)

    df1 = build_esercizio_1(rng)
    df2 = build_esercizio_2_classe(rng)

    fig, axes = plt.subplots(2, 1, figsize=(13, 9), sharex=False)

    # --------------------
    # Pannello A: ESERCIZIO 1 (mio, meglio)
    # --------------------
    ax = axes[0]
    windows = (7, 14)

    for col in ["Up", "Wave", "Down"]:
        # raw leggero
        line = ax.plot(df1.index, df1[col], alpha=0.25, marker="o", markevery=10, label=f"{col} raw")[0]
        c = line.get_color()

        # MA + bande per 7 e 14
        for w in windows:
            ma = df1[f"{col}_MA{w}"]
            std = df1[f"{col}_STD{w}"]
            ax.plot(df1.index, ma, label=f"{col} MA{w}")
            fill_band(ax, df1.index, ma, std, alpha=0.10, color=c)

    ax.set_title("Esercizio 1 — raw + MA7/MA14 + bande ±STD (più rigoroso)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Valore")
    ax.grid(True, alpha=0.3)
    ax.legend(ncols=3, fontsize=8)

    # --------------------
    # Pannello B: ESERCIZIO 2 (classe)
    # --------------------
    ax = axes[1]
    for col in ["S1", "S2", "S3"]:
        # in classe spesso si plottano solo MA7 (qui facciamo uguale)
        ma = df2[f"{col}_MA7"]
        std = df2[f"{col}_STD7"]
        line = ax.plot(df2.index, ma, label=f"{col} MA7")[0]
        fill_band(ax, df2.index, ma, std, alpha=0.18, color=line.get_color())

    ax.set_title("Esercizio 2 (classe) — MA7 + banda ±STD7 (min_periods=1)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Valore")
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()




# ===== 
# Esercizio 2
# =======    


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    rng = np.random.default_rng(42)

    n= 90
    dates = pd.date_range("2025-01-01", periods=n, freq="D")
    t= np.arange(n)

    products = {}
    for i in range(5):
        base = 80 + 10*i
        trend = 0.15*(i+1)*t
        season = 8*np.sin(2*np.pi*t/14 + i)     # piccola stagionalità
        noise = rng.normal(0, 6 + i, n)
        products[f"Prod_{i+1}"] = base + trend + season + noise

    df = pd.DataFrame(products, index=dates)

    weekly = df.resample("W").sum()
    wow = weekly.pct_change() * 100  # % settimana-su-settimana

    fig, ax = plt.subplots(figsize=(12, 6))
    weekly.plot(ax=ax, marker="o")

    ax.set(title= "Vendite settimanali per prodotto (con picchi annotati)",
           xlabel= "Settimana", ylabel="Vendite (somma)")
    ax.grid(True, alpha=0.3)

    # Annotazioni sui picchi
    for col in weekly.columns:
        peak_idx = weekly[col].idxmax()
        peak_val = weekly[col].max()

        ax.scatter([peak_idx], [peak_val], marker="x")
        ax.annotate(f"{col} picco\n{peak_val:.0f}",
                    xy=(peak_idx, peak_val),
                    xytext=(0, 10),
                    textcoords="offset points",
                    ha="center",
                    fontsize=8)

    plt.show()

if __name__ == "__main__":
    main()



# ===== 
# Esercizio 3
# =======   

"""
- Genera 6 variabili
- Correlazione
- Heatmap + annotazioni numeriche + marker soglia (> 0.8) + colorbar
Nota: inseriamo una correlazione forte “pilotata” per avere casi interessanti.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    rng = np.random.default_rng(42)

    n = 500
    A = rng.normal(0, 1, n)
    B = rng.normal(0, 1, n)
    C = rng.normal(0, 1, n)
    D = rng.normal(0, 1, n)

    # Correlazioni “costruite” (per rendere visibile la soglia > 0.8)
    E = -0.85*B + rng.normal(0, 0.3, n)
    F =  0.90*A + rng.normal(0, 0.25, n)


    df = pd.DataFrame({"A":A, "B":B, "C":C, "D":D, "E":E, "F":F })

    print(df)

    corr = df.corr()

    print(corr)


    fig, ax = plt.subplots(figsize=(8,6))
    im= ax.imshow(corr.values, vmin=-1, vmax=1)


    ax.set_xticks(range(corr.shape[1]), corr.columns)
    ax.set_yticks(range(corr.shape[0]), corr.index)
    ax.set_title("Heatmap correlazioni (con soglia |r| > 0.8)")

    # Numeri e marker soglia
    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            val = corr.values[i, j]
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=8)

            if i != j and abs(val) > 0.8:
                ax.scatter([j], [i], marker="o", facecolors="none", edgecolors="black", s=180)

    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="r")
    plt.tight_layout()
    plt.show()


if __name__== "__main__":
    main()



# ===== 
# Esercizio 3
# =======   


"""
- Dati sintetici: vendite, temperatura, ordini
- 1 figura con: line plot (trend+anomalie), scatter, heatmap correlazioni
- Salvataggio PNG (alta risoluzione) + PDF
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    rng = np.random.default_rng(42)

    n = 90
    dates = pd.date_range("2025-01-01", periods=n, freq="D")
    t = np.arange(n)

    temp = 10 + 8*np.sin(2*np.pi*t/30) + rng.normal(0, 1.2, n)
    orders = 80 + 3*temp + rng.normal(0, 8, n)
    sales = 200 + 1.5*t + 2*orders + rng.normal(0, 30, n)

    # Anomalie volutamente inserite
    sales[20] += 250
    sales[60] -= 220

    df = pd.DataFrame({"sales": sales, "temp": temp, "orders": orders}, index=dates)
    df["sales_ma7"] = df["sales"].rolling(7).mean()

    # Semplice detection anomalie con z-score
    z = (df["sales"] - df["sales"].mean()) / df["sales"].std()
    anomalies = df.loc[z.abs() > 2]

    fig = plt.figure(figsize=(12, 7))
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1.4])

    # (1) Line plot: trend + anomalie
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(df.index, df["sales"], label="Sales", alpha=0.5)
    ax1.plot(df.index, df["sales_ma7"], label="MA7")

    if not anomalies.empty:
        ax1.scatter(anomalies.index, anomalies["sales"], marker="x", label="Anomalie")
        for d, v in anomalies["sales"].items():
            ax1.annotate("anomalia", xy=(d, v), xytext=(0, 8),
                         textcoords="offset points", ha="center", fontsize=8)

    ax1.set_title("Vendite giornaliere: trend + anomalie")
    ax1.legend()

    # (2) Scatter: temperatura vs ordini
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.scatter(df["temp"], df["orders"])
    ax2.set_title("Temperatura vs Ordini")
    ax2.set_xlabel("Temp")
    ax2.set_ylabel("Ordini")

    # (3) Heatmap: correlazioni
    ax3 = fig.add_subplot(gs[1, 1])
    corr = df[["sales", "temp", "orders"]].corr()
    im = ax3.imshow(corr.values, vmin=-1, vmax=1)

    ax3.set_xticks(range(corr.shape[1]), corr.columns, rotation=45, ha="right")
    ax3.set_yticks(range(corr.shape[0]), corr.index)
    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            ax3.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=8)

    fig.colorbar(im, ax=ax3, fraction=0.046, pad=0.04, label="r")
    ax3.set_title("Heatmap correlazioni")

    fig.tight_layout()

    # Salvataggio
    fig.savefig("esercizio4_combo.png", dpi=300)
    fig.savefig("esercizio4_combo.pdf")

    plt.show()

if __name__ == "__main__":
    main()