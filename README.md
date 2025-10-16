# 🧬 SIR Model Visualizer (Tkinter + Matplotlib)

An interactive **SIR (Susceptible–Infected–Recovered)** epidemiological model built with **Python**, **Tkinter**, and **Matplotlib**.  
This GUI lets you explore how the infection rate (**β**), recovery rate (**γ**), and initial infected fraction (**I₀**) affect the spread of a disease over time.

---

## 📸 Features
- 🎚 **Interactive sliders** for β, γ, and I₀  
- 📈 **Real-time graph updates** as parameters change  
- 🧮 Based on the **classical SIR differential equations**  
- 🧠 Great for learning or teaching epidemic modeling  

---

## 🧠 Model Overview

The SIR model divides the population into three compartments:

$$
\begin{aligned}
\frac{dS}{dt} &= -\beta S I \\
\frac{dI}{dt} &= \beta S I - \gamma I \\
\frac{dR}{dt} &= \gamma I
\end{aligned}
$$

Where:

- **S(t)** → fraction of susceptible individuals  
- **I(t)** → fraction of infected individuals  
- **R(t)** → fraction of recovered individuals  
- **β** → infection rate  
- **γ** → recovery rate  

---
## Overview results

<img width="748" height="690" alt="image" src="https://github.com/user-attachments/assets/fcc99d5b-0618-49cc-9099-75ffa44753e3" />

