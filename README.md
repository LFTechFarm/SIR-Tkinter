# 🧬 SIR Model Visualizer (Tkinter + Matplotlib)

An interactive SIR (Susceptible–Infected–Recovered) epidemiological model built with Python, Tkinter, and Matplotlib.
This GUI lets you explore how infection rate (β), recovery rate (γ), and initial infected fraction (I₀) affect the spread of a disease over time.

# 📸 Features

🎚 Interactive sliders for β, γ, and I₀

📈 Real-time graph updates as parameters change

🧮 Built on the classical SIR differential equations

🧠 Great for learning or teaching epidemic modeling

🧠 Model Overview

The SIR model divides the population into three compartments:

𝑑
𝑆
𝑑
𝑡
	
=
−
𝛽
𝑆
𝐼


𝑑
𝐼
𝑑
𝑡
	
=
𝛽
𝑆
𝐼
−
𝛾
𝐼


𝑑
𝑅
𝑑
𝑡
	
=
𝛾
𝐼
dt
dS
	​

dt
dI
	​

dt
dR
	​

	​

=−βSI
=βSI−γI
=γI
	​


where:

S(t) → fraction of susceptible individuals

I(t) → fraction of infected individuals

R(t) → fraction of recovered individuals

β → infection rate
