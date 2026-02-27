"""
Utility per creare o scaricare OHLCV e avere dataset pronti per grafici finanziari.

Dipendenze minime:
pip install numpy pandas matplotlib

Opzionali (per i grafici specialistici):
pip install yfinance mplfinance plotly PyQt6
"""

from __future__ import annotations
import numpy as np
import pandas as pd


def make_synth_ohlcv(n: int = 120, start: str = "2025-01-01", seed: int = 42) -> pd.DataFrame:
    """Genera OHLCV sintetico (business days), utile quando non vuoi dipendere da internet."""
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range(start=start, periods=n)

    # Random walk sul prezzo
    rets = rng.normal(loc=0.0005, scale=0.02, size=n)
    close = 100 * (1 + rets).cumprod()

    # Open = close precedente con piccolo rumore
    open_ = np.r_[close[0], close[:-1]] * (1 + rng.normal(0, 0.003, size=n))

    # High/Low coerenti
    high = np.maximum(open_, close) * (1 + rng.uniform(0.001, 0.02, size=n))
    low = np.minimum(open_, close) * (1 - rng.uniform(0.001, 0.02, size=n))

    # Volume (lognormale)
    volume = rng.lognormal(mean=14, sigma=0.35, size=n).astype(int)

    df = pd.DataFrame(
        {"Open": open_, "High": high, "Low": low, "Close": close, "Volume": volume},
        index=idx
    )
    return df


def load_ohlcv(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Prova a scaricare OHLCV da fonte pubblica (yfinance).
    Se fallisce (no internet / rate limit / lib mancante), usa dati sintetici.
    """
    try:
        import yfinance as yf  # opzionale
        raw = yf.download(ticker, start=start, end=end, auto_adjust=False, progress=False)
        raw = raw.rename(columns=str.title)
        df = raw[["Open", "High", "Low", "Close", "Volume"]].dropna()
        if df.empty:
            raise ValueError("Download OK ma dataframe vuoto.")
        return df
    except Exception:
        # fallback sintetico
        return make_synth_ohlcv(n=140, start=start, seed=7)
    

"""
Esercizio 1: OHLC chart con dati pubblici (fallback sintetico se serve).
"""
import matplotlib.pyplot as plt
import mplfinance as mpf

ticker = "AAPL"
start = "2025-01-01"
end = "2025-06-01"

df = load_ohlcv(ticker, start, end)

cols = ["Open", "High", "Low", "Close", "Volume"]

print(df[cols].dtypes)
print(df[cols].head())

# Ti dice che tipi reali ci sono dentro "Open"
print(df["Open"].map(type).value_counts().head(10))

# Quanti valori non numerici (dopo coercizione)
tmp = pd.to_numeric(df["Open"], errors="coerce")
print("Open non numerici:", tmp.isna().sum())

# 1) estrai il singolo ticker dal MultiIndex (level=1 = Ticker)
df_mpf = df.xs("Aapl", axis=1, level=1).copy()

# 2) tieni solo OHLCV e assicurati ordine
df_mpf = df_mpf[["Open", "High", "Low", "Close", "Volume"]]

import mplfinance as mpf
mpf.plot(df_mpf, type="candle", volume=True, title="AAPL")
plt.show()