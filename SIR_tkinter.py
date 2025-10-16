import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# ------------------------------
# SIR Model (Euler Integration)
# ------------------------------
def sir_model(S, I, R, beta, gamma, dt):
    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I
    return S + dS * dt, I + dI * dt, R + dR * dt

def run_simulation(beta, gamma, I0, days=160, dt=0.01):
    S0 = 1 - I0
    R0 = 0
    t = np.arange(0, days, dt)
    S, I, R = np.zeros_like(t), np.zeros_like(t), np.zeros_like(t)
    S[0], I[0], R[0] = S0, I0, R0

    for i in range(1, len(t)):
        S[i], I[i], R[i] = sir_model(S[i-1], I[i-1], R[i-1], beta, gamma, dt)

    return t, S, I, R

# ------------------------------
# Tkinter GUI
# ------------------------------
class SIRApp:
    def __init__(self, root):
        self.root = root
        root.title("SIR Model Visualization")

        self.beta = tk.DoubleVar(value=0.3)
        self.gamma = tk.DoubleVar(value=0.1)
        self.I0 = tk.DoubleVar(value=0.01)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        slider_frame = ttk.Frame(root)
        slider_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.create_slider(slider_frame, "β (Infection rate)", self.beta, 0.0, 0.6)
        self.create_slider(slider_frame, "γ (Recovery rate)", self.gamma, 0.0, 0.3)
        self.create_slider(slider_frame, "I₀ (Initial infected fraction)", self.I0, 0.0, 0.1)

        self.update_plot()

    def create_slider(self, parent, label, variable, min_val, max_val):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=5)
        ttk.Label(frame, text=label).pack(side=tk.LEFT, padx=5)
        slider = ttk.Scale(
            frame, from_=min_val, to=max_val, variable=variable,
            command=lambda v: self.update_plot()
        )
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Label(frame, textvariable=variable, width=6).pack(side=tk.RIGHT, padx=5)

    def update_plot(self):
        beta = self.beta.get()
        gamma = self.gamma.get()
        I0 = self.I0.get()
        t, S, I, R = run_simulation(beta, gamma, I0)

        self.ax.clear()
        self.ax.plot(t, S, label="Susceptible (S)")
        self.ax.plot(t, I, label="Infected (I)")
        self.ax.plot(t, R, label="Recovered (R)")
        self.ax.set_xlabel("Time (days)")
        self.ax.set_ylabel("Fraction of population")
        self.ax.set_title(f"SIR Model (β={beta:.2f}, γ={gamma:.2f}, I₀={I0:.3f})")
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()

# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SIRApp(root)
    root.mainloop()
