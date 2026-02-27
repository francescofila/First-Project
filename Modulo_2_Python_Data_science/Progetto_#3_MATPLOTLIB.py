from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")

# inserisco le colonne richieste dalla traccia
REQUIRED_COLS = [
    "Order Date", "Ship Date", "Category", "Sub-Category",
    "Sales", "Profit", "Region", "State", "Quantity"
]


# ---------------------------
# FASE 1A — Generazione dataset (date semplici, poca pulizia)
# ---------------------------

def generate_dataset(n: int = 1200, seed: int = 42, null_rate: float = 0.02, dup_rate: float = 0.03) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # creo 9 stati + 3 aree coerenti
    state_to_region = {
        "Italia": "Europa Meridionale",
        "Spagna": "Europa Meridionale",
        "Portogallo": "Europa Meridionale",
        "Francia": "Europa Occidentale",
        "Belgio": "Europa Occidentale",
        "Paesi Bassi": "Europa Occidentale",
        "Germania": "Europa Centrale",
        "Austria": "Europa Centrale",
        "Svizzera": "Europa Centrale",
    }
    states = np.array(list(state_to_region.keys()))

    # creo 3 categorie + 3 sotto-categorie per categoria
    categories = ["Arredamento", "Cancelleria", "Tecnologia"]
    subcats = {
        "Arredamento": ["Sedie", "Tavoli", "Illuminazione"],
        "Cancelleria": ["Carta", "Raccoglitori", "Archiviazione"],
        "Tecnologia": ["Smartphone", "Accessori tech", "PC e laptop"],
    }

    # Date: le genero già in formato ISO string (semplice da convertire)
    start = pd.Timestamp("2022-01-01")
    end = pd.Timestamp("2025-12-31")
    days = (end - start).days + 1

    order_dt = start + pd.to_timedelta(rng.integers(0, days, size=n), unit="D")
    ship_dt = order_dt + pd.to_timedelta(rng.integers(1, 8, size=n), unit="D")  # 1–7 giorni dopo

    # Convertiamo a stringhe ISO (per poi “ripulire” con pd.to_datetime)
    order_str = pd.Series(order_dt).dt.strftime("%Y-%m-%d")
    ship_str = pd.Series(ship_dt).dt.strftime("%Y-%m-%d")

    # Campi categorici
    state = rng.choice(states, size=n)
    region = pd.Series(state).map(state_to_region).to_numpy()

    category = rng.choice(categories, size=n, p=[0.33, 0.34, 0.33])
    sub_category = np.empty(n, dtype=object)
    for c in categories:
        mask = category == c
        sub_category[mask] = rng.choice(subcats[c], size=mask.sum())

    quantity = rng.integers(1, 9, size=n)

    # Sales/Profit: semplici e plausibili
    base_price = {"Arredamento": 120.0, "Cancelleria": 25.0, "Tecnologia": 220.0}
    base = np.vectorize(base_price.get)(category)

    sales = (base * quantity) * (1 + rng.normal(0, 0.20, size=n))
    sales = np.clip(sales, 2.0, None)

    profit = sales * rng.normal(0.12, 0.10, size=n)
    loss_mask = rng.random(n) < 0.12
    profit[loss_mask] *= -rng.uniform(0.2, 1.0, size=loss_mask.sum())

    df = pd.DataFrame({
        "Order Date": order_str,
        "Ship Date": ship_str,
        "Category": category,
        "Sub-Category": sub_category,
        "Sales": np.round(sales, 2),
        "Profit": np.round(profit, 2),
        "Region": region,
        "State": state,
        "Quantity": quantity
    })

    # Un po’ di NULL (per esercizio pulizia)
    if null_rate > 0:
        core_cols = ["Order Date", "Ship Date", "Category", "Sub-Category", "State", "Sales", "Profit"]
        for col in core_cols:
            m = rng.random(n) < null_rate
            df.loc[m, col] = np.nan

    # Duplicati (per esercizio pulizia)
    if dup_rate > 0:
        k = max(1, int(n * dup_rate))
        dup_idx = rng.integers(0, n, size=k)
        df = pd.concat([df, df.iloc[dup_idx]], ignore_index=True)

    return df


# ---------------------------
# FASE 1B — Pulizia dati (traccia, semplice)
# ---------------------------

def clean_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Traccia:
    1) datetime
    2) null e duplicati
    3) Year
    """
    df = df.copy()

    # 0) controllo colonne 
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Mancano colonne richieste: {missing}")

    # (1) Converti date (semplice)
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # (2) null e duplicati (report minimo)
    duplicates_before = int(df.duplicated().sum())
    nulls_before = df.isna().sum().to_dict()

    df = df.drop_duplicates()

    core = ["Order Date", "Ship Date", "Category", "Sub-Category", "State", "Sales", "Profit"]
    before_dropna = len(df)
    df = df.dropna(subset=core)
    dropped_na_core = before_dropna - len(df)

    # (3) Year (aggiungo colonna al df)
    df["Year"] = df["Order Date"].dt.year.astype("Int64")

    report = {
        "duplicates_before": duplicates_before,
        "rows_after_drop_duplicates": int(before_dropna),
        "rows_dropped_na_core": int(dropped_na_core),
        "rows_final": int(len(df)),
        "nulls_before": nulls_before,
    }
    return df, report


# ---------------------------
# RUN (FASE 1)
# ---------------------------

if __name__ == "__main__":
    df_raw = generate_dataset(n=1200, seed=42, null_rate=0.02, dup_rate=0.03)
    df_clean, rep = clean_dataset(df_raw)

    print("\n--- RAW (prime 5) ---")
    print(df_raw.head())

    print("\n--- REPORT PULIZIA ---")
    print(f"Duplicati prima     : {rep['duplicates_before']}")
    print(f"Righe drop NA core  : {rep['rows_dropped_na_core']}")
    print(f"Righe finali        : {rep['rows_final']}")

    print("\n--- CLEAN (prime 5) ---")
    print(df_clean.head())

    print("\n--- dtypes (clean) ---")
    print(df_clean.dtypes)


# Faccimoa un po di feature engeneerin

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Faccio un po di feature engineering minimo.
    """
    df = df.copy()

    # 1) Lead Time: giorni tra ordine e spedizione
    df["Lead Time (days)"] = (df["Ship Date"] - df["Order Date"]).dt.days

    # 2) Profit Margin: profitto relativo (gestione divisione per zero in modo semplice)
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    df.loc[df["Sales"] <= 0, "Profit Margin"] = np.nan

    # 3) Estraggo mese: utile per trend successivi
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()

    return df

def eda_sales_profit_by_year(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Year")[["Sales", "Profit"]]
        .sum()
        .reset_index()
        .sort_values("Year")
    )


def eda_top5_subcategories(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index(name="Sales")
    )

def eda_region_averages(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Region")
        .agg(
            Avg_Sales=("Sales", "mean"),
            Avg_Profit=("Profit", "mean"),
            Avg_Profit_Margin=("Profit Margin", "mean"),
            Avg_Lead_Time=("Lead Time (days)", "mean"),
            Orders=("Sales", "size"),
        )
        .reset_index()
        .sort_values("Avg_Profit", ascending=False)
    )


if __name__ == "__main__":
    df_raw = generate_dataset(n=1200, seed=42, null_rate=0.02, dup_rate=0.03)
    df_clean, rep = clean_dataset(df_raw)

    df_feat = add_features(df_clean)

    yearly = eda_sales_profit_by_year(df_feat)
    top5 = eda_top5_subcategories(df_feat)
    region_avg = eda_region_averages(df_feat)

    pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

    print("\n--- EDA: Totale vendite e profitti per anno ---")
    print(yearly)

    print("\n--- EDA: Top 5 sottocategorie più vendute ---")
    print(top5)

    print("\n--- EDA: Medie per regione ---")
    print(region_avg)




import tkinter as tk
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def create_window_filter_states(root: tk.Tk, df: pd.DataFrame) -> None:
    """
    Finestra 1:
    - Checkbox (State)
    - Bar: Sales per State
    - Bar: Sales per Category (filtrate da State)
    """
    win = tk.Toplevel(root)
    win.title("Filtro nazioni — vendite per nazione e categoria")

    df = df.copy()
    states = sorted(df["State"].dropna().unique().tolist())
    categories = sorted(df["Category"].dropna().unique().tolist())

    left = tk.Frame(win, padx=10, pady=10)
    left.pack(side=tk.LEFT, fill=tk.Y)

    right = tk.Frame(win, padx=10, pady=10)
    right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    tk.Label(left, text="Filtra nazioni (State)", font=("Helvetica", 12, "bold")).pack(anchor="w")

    state_vars = {s: tk.BooleanVar(value=True) for s in states}
    status_lbl = tk.Label(left, text="", fg="gray")
    status_lbl.pack(anchor="w", pady=(8, 0))

    fig = Figure(figsize=(10, 6), dpi=100)
    ax_state = fig.add_subplot(2, 1, 1)
    ax_cat = fig.add_subplot(2, 1, 2)

    canvas = FigureCanvasTkAgg(fig, master=right)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, right)
    toolbar.update()

    def _filtered_df():
        selected = [s for s in states if state_vars[s].get()]
        if not selected:
            return df.iloc[0:0], selected
        return df[df["State"].isin(selected)], selected

    def redraw():
        dff, selected = _filtered_df()
        status_lbl.config(text=f"Selezionate: {len(selected)}/{len(states)}")

        # Plot 1: Sales per State
        ax_state.clear()
        ax_state.set_title("Vendite per nazione (filtrate)")
        ax_state.set_ylabel("Sales (€)")

        if len(dff) == 0:
            ax_state.text(0.5, 0.5, "Nessuna nazione selezionata",
                          ha="center", va="center", transform=ax_state.transAxes)
        else:
            sales_by_state = dff.groupby("State")["Sales"].sum().reindex(selected)
            ax_state.bar(sales_by_state.index, sales_by_state.values)
            ax_state.tick_params(axis="x", rotation=20)

        # Plot 2: Sales per Category
        ax_cat.clear()
        ax_cat.set_title("Vendite per categoria (filtrate dalle nazioni)")
        ax_cat.set_ylabel("Sales (€)")

        if len(dff) == 0:
            ax_cat.text(0.5, 0.5, "Nessuna nazione selezionata",
                        ha="center", va="center", transform=ax_cat.transAxes)
        else:
            sales_by_cat = dff.groupby("Category")["Sales"].sum().reindex(categories).fillna(0)
            ax_cat.bar(sales_by_cat.index, sales_by_cat.values)
            ax_cat.tick_params(axis="x", rotation=10)

        fig.tight_layout()
        canvas.draw_idle()

    for s in states:
        tk.Checkbutton(left, text=s, variable=state_vars[s], command=redraw).pack(anchor="w")

    redraw()


def create_window_trends(root: tk.Tk, df: pd.DataFrame) -> None:
    """
    Finestra 2 (senza checkbox):
    - Linee: Sales mensili per Region
    - Linee: Profit mensili per Region
    - Heatmap: correlazione tra categorie (vendite mensili)
    """
    win = tk.Toplevel(root)
    win.title("Trend & correlazioni — vendite/profitti nel tempo")

    df = df.copy()
    regions = sorted(df["Region"].dropna().unique().tolist())
    categories = sorted(df["Category"].dropna().unique().tolist())

    # Assumo Order Date già datetime (df_clean o df_feat)
    # Se vuoi essere difensivo: df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    # e poi dropna, ma qui restiamo snelli.

    fig = Figure(figsize=(11, 8), dpi=100)
    ax_sales = fig.add_subplot(3, 1, 1)
    ax_profit = fig.add_subplot(3, 1, 2)
    ax_heat = fig.add_subplot(3, 1, 3)

    frame = tk.Frame(win, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()

    def monthly_pivot(value_col: str, group_col: str) -> pd.DataFrame:
        tmp = (
            df.groupby([pd.Grouper(key="Order Date", freq="MS"), group_col])[value_col]
            .sum()
            .unstack(group_col)
            .fillna(0)
            .sort_index()
        )
        return tmp

    def annotate_heatmap(ax, data, labels):
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels)
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", fontsize=9)

    # --- 1) Sales trend per Region ---
    ax_sales.set_title("Vendite mensili nel tempo — per macro area (Region)")
    ax_sales.set_ylabel("Sales (€)")
    sales_reg = monthly_pivot("Sales", "Region")
    for r in regions:
        if r in sales_reg.columns:
            ax_sales.plot(sales_reg.index, sales_reg[r], label=r)
    ax_sales.legend(loc="upper left")

    # --- 2) Profit trend per Region ---
    ax_profit.set_title("Profitti mensili nel tempo — per macro area (Region)")
    ax_profit.set_ylabel("Profit (€)")
    profit_reg = monthly_pivot("Profit", "Region")
    for r in regions:
        if r in profit_reg.columns:
            ax_profit.plot(profit_reg.index, profit_reg[r], label=r)
    ax_profit.legend(loc="upper left")

    # --- 3) Heatmap correlazioni categorie (Sales mensili) ---
    ax_heat.set_title("Heatmap — correlazione tra categorie (co-movimento vendite mensili)")
    ax_heat.set_xlabel("Category")
    ax_heat.set_ylabel("Category")

    sales_cat = monthly_pivot("Sales", "Category")
    corr = sales_cat.corr(method="pearson").reindex(index=categories, columns=categories)
    data = corr.values

    im = ax_heat.imshow(data, vmin=-1, vmax=1, aspect="auto")
    annotate_heatmap(ax_heat, data, categories)
    cb = fig.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.02)
    cb.set_label("Correlation")

    fig.tight_layout()
    canvas.draw_idle()


def create_window_region_profit(root: tk.Tk, df: pd.DataFrame) -> None:
    """
    Finestra 3:
    - Boxplot: distribuzione Profit per Region
    - Heatmap: Profit medio per (Region x Month) per vedere pattern nel tempo
    """
    win = tk.Toplevel(root)
    win.title("Region ↔ Profit — distribuzione e pattern nel tempo")

    df = df.copy()
    regions = sorted(df["Region"].dropna().unique().tolist())

    # Assumo Order Date già datetime
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()

    fig = Figure(figsize=(11, 7), dpi=100)
    ax_box = fig.add_subplot(2, 1, 1)
    ax_heat = fig.add_subplot(2, 1, 2)

    frame = tk.Frame(win, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()

    # --- 1) Boxplot Profit per Region ---
    ax_box.set_title("Distribuzione del Profit per macro area (Region)")
    ax_box.set_ylabel("Profit (€)")

    data = [df.loc[df["Region"] == r, "Profit"].dropna().values for r in regions]
    ax_box.boxplot(data, labels=regions, showfliers=True)
    ax_box.axhline(0, linewidth=1)  # linea zero: mesi/ordini in perdita vs profitto
    ax_box.tick_params(axis="x", rotation=10)

    # --- 2) Heatmap Profit medio per Region x Month ---
    ax_heat.set_title("Profit medio nel tempo — Heatmap (Region × Month)")
    ax_heat.set_xlabel("Month")
    ax_heat.set_ylabel("Region")

    pivot = (
        df.pivot_table(index="Region", columns="Month", values="Profit", aggfunc="mean")
        .reindex(index=regions)
        .fillna(0)
    )

    im = ax_heat.imshow(pivot.values, aspect="auto")
    cb = fig.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.02)
    cb.set_label("Avg Profit (€)")

    ax_heat.set_yticks(range(len(pivot.index)))
    ax_heat.set_yticklabels(pivot.index)

    # tick mesi “diradati” per leggibilità (ogni 6 mesi)
    months = pivot.columns.to_list()
    step = 6 if len(months) > 24 else 3
    xticks = list(range(0, len(months), step))
    ax_heat.set_xticks(xticks)
    ax_heat.set_xticklabels([months[i].strftime("%Y-%m") for i in xticks], rotation=0)

    fig.tight_layout()
    canvas.draw_idle()


def launch_three_windows(df: pd.DataFrame) -> None:
    """
    Avvia entrambe le finestre con un solo mainloop.
    """
    root = tk.Tk()
    root.withdraw()  # nasconde la finestra “vuota” principale

    create_window_filter_states(root, df)
    create_window_trends(root, df)
    create_window_region_profit(root, df)

    root.mainloop()    

if __name__ == "__main__":
    df_raw = generate_dataset(n=1200, seed=42, null_rate=0.02, dup_rate=0.03)
    df_clean, rep = clean_dataset(df_raw)

    launch_three_windows(df_clean)