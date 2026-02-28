import tkinter as tk
from tkinter import ttk
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InterattivaTk:
    """GUI Tkinter + Matplotlib: slider, checkbox, reset, save, legenda dinamica."""

    def __init__(self, root):
        self.root = root
        self.root.title("Esercizio 4 — Tkinter + Matplotlib")

        # --- Stato / dati ---
        self.x = np.linspace(0, 10, 800)
        self.amp_init = 1.0
        self.freq_init = 1.0

        # --- Figura Matplotlib (OO, senza pyplot) ---
        self.fig = Figure(figsize=(7, 4))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("GUI interattiva")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

        self.line_sin, = self.ax.plot(self.x, np.sin(self.x), label="sin")
        self.line_cos, = self.ax.plot(self.x, np.cos(self.x), label="cos")
        self.ax.legend(loc="upper right")

        # --- Canvas ---
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.canvas.draw()

        # --- Controlli ---
        self.amp_var = tk.DoubleVar(value=self.amp_init)
        self.freq_var = tk.DoubleVar(value=self.freq_init)
        self.show_cos_var = tk.BooleanVar(value=True)

        ttk.Label(root, text="Ampiezza").grid(row=1, column=0, sticky="w", padx=10)
        self.amp_scale = ttk.Scale(root, from_=0.1, to=5.0, variable=self.amp_var, command=self.update_plot)
        self.amp_scale.grid(row=1, column=1, sticky="ew", padx=10)

        ttk.Label(root, text="Frequenza").grid(row=2, column=0, sticky="w", padx=10)
        self.freq_scale = ttk.Scale(root, from_=0.1, to=10.0, variable=self.freq_var, command=self.update_plot)
        self.freq_scale.grid(row=2, column=1, sticky="ew", padx=10)

        self.cos_check = ttk.Checkbutton(root, text="Mostra cos", variable=self.show_cos_var, command=self.update_plot)
        self.cos_check.grid(row=1, column=2, padx=10, sticky="w")

        self.btn_reset = ttk.Button(root, text="Reset", command=self.reset)
        self.btn_reset.grid(row=1, column=3, padx=10, sticky="ew")

        self.btn_save = ttk.Button(root, text="Salva PNG", command=self.save_png)
        self.btn_save.grid(row=2, column=3, padx=10, sticky="ew")

        # Layout resize
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        self.update_plot()

    def update_plot(self, _event=None):
        """Aggiorna curve e legenda in base ai controlli GUI."""
        amp = float(self.amp_var.get())
        freq = float(self.freq_var.get())

        self.line_sin.set_ydata(amp * np.sin(freq * self.x))
        self.line_cos.set_ydata(amp * np.cos(freq * self.x))

        self.line_cos.set_visible(bool(self.show_cos_var.get()))

        self.ax.legend(loc="upper right")
        self.ax.relim()
        self.ax.autoscale_view()

        self.canvas.draw_idle()

    def reset(self):
        """Ripristina controlli e grafico ai valori iniziali."""
        self.amp_var.set(self.amp_init)
        self.freq_var.set(self.freq_init)
        self.show_cos_var.set(True)
        self.update_plot()

    def save_png(self):
        """Salva lo stato corrente del grafico in PNG."""
        self.fig.savefig("esercizio_4_gui_tkinter.png", dpi=150, bbox_inches="tight")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterattivaTk(root)
    root.mainloop()








import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

x = np.linspace(0, 10, 500)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.30)

line, = ax.plot(x, np.sin(x))
ax.set_title("Slider + Reset")

ax_amp = plt.axes([0.25, 0.15, 0.65, 0.03])
s_amp = Slider(ax_amp, "Ampiezza", 0.1, 5.0, valinit=1.0)

def update(_):
    """Ridisegna la sinusoide con la nuova ampiezza."""
    line.set_ydata(s_amp.val * np.sin(x))
    fig.canvas.draw_idle()

s_amp.on_changed(update)

ax_btn = plt.axes([0.80, 0.03, 0.12, 0.05])
btn = Button(ax_btn, "Reset")

def on_reset(_event):
    """Riporta lo slider al valore iniziale."""
    s_amp.reset()

btn.on_clicked(on_reset)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

x = np.linspace(0, 10, 500)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

line_sin, = ax.plot(x, np.sin(x), label="sin")
line_cos, = ax.plot(x, np.cos(x), label="cos")
ax.legend(loc="upper right")
ax.set_title("Slider + CheckButtons")

ax_amp = plt.axes([0.25, 0.10, 0.65, 0.03])
s_amp = Slider(ax_amp, "Ampiezza", 0.1, 5.0, valinit=1.0)

def update(_):
    """Aggiorna entrambe le curve (se visibili) con la nuova ampiezza."""
    amp = s_amp.val
    line_sin.set_ydata(amp * np.sin(x))
    line_cos.set_ydata(amp * np.cos(x))
    fig.canvas.draw_idle()

s_amp.on_changed(update)

ax_chk = plt.axes([0.03, 0.55, 0.18, 0.15])
chk = CheckButtons(ax_chk, ["sin", "cos"], [True, True])

def toggle(label):
    """Mostra/nasconde la curva corrispondente alla label cliccata."""
    target = line_sin if label == "sin" else line_cos
    target.set_visible(not target.get_visible())
    ax.legend(loc="upper right")
    fig.canvas.draw_idle()

chk.on_clicked(toggle)

plt.show()


