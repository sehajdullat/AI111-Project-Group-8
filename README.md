# 🚦 AI Traffic Signal Optimization using Stochastic Modeling

## 📌 Overview

This project implements an **AI-based traffic signal control system** using concepts from **probability theory, queueing theory, and optimization**.

The system models traffic as a **stochastic (random) process** using the Poisson distribution and improves traditional traffic systems by introducing:

* ✅ Predictive decision-making (using expected arrivals λT)
* ✅ Queue-based optimization
* ✅ Emergency vehicle prioritization

---

## 🎯 Objectives

* Reduce average waiting time at intersections
* Eliminate inefficient fixed-timing signals
* Handle real-world randomness in traffic flow
* Prioritize emergency vehicles dynamically

---

## 🧠 Mathematical Concepts Used

### 1. Poisson Distribution

Used to model **random vehicle arrivals**.

```math
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
```

* λ = average arrival rate
* Models real-world randomness of traffic

---

### 2. Queueing Theory

Traffic is modeled as a queue:

```math
Q = Q + Arrivals - Departures
```

* Q → number of vehicles waiting
* μ → service rate (vehicles cleared per cycle)

---

### 3. Expected Waiting Time

```math
W = \frac{Q}{\mu}
```

* Estimates delay experienced by vehicles

---

### 4. Predictive Optimization (Innovation)

```math
Score = Q + \lambda T
```

* Q → current congestion
* λT → expected future arrivals

👉 This makes the system **predictive instead of reactive**

---

### 5. Emergency Priority

* Lanes with emergency vehicles are prioritized
* If multiple emergency lanes exist → highest emergency count is selected
* Overrides normal optimization

---

## 📂 Project Structure

```
project/
│
├── main.py          # Entry point
├── config.py        # System parameters
├── utils.py         # Mathematical functions
├── simulation.py    # Core logic (queue + decision)
├── display.py       # Output formatting
│
├── data/            # Input data (optional)
│   └── sample_data.txt
│
├── results/         # Output logs (optional)
│   └── sample_output.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

* Python 3.8+
* Libraries:

```bash
numpy
```

---

## 🔧 Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/traffic-ai-project.git
cd traffic-ai-project
```

---

### Step 2: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📥 Input

The system uses predefined parameters from `config.py`:

* λ (arrival rate per lane)
* μ (service rate)
* T (prediction horizon)
* Time steps

---

## 📤 Output

For each time step, the system displays:

* Queue length (Q)
* Number of arrivals
* Emergency vehicles
* Score (Q + λT)
* Expected waiting time
* Priority order of lanes
* Selected lane (Green signal)

---

## 📁 Data Handling

* `data/` folder → stores input configuration or datasets (if extended)
* `results/` folder → used to store simulation outputs/logs

> Currently, sample files are included for demonstration purposes.

---

## 🚑 Emergency Handling

* Each lane has a probability of emergency occurrence
* Emergency vehicles override normal decision logic
* Ensures real-world applicability and safety

---

## ⚠️ Limitations

* Assumes constant service rate (μ)
* Traffic arrivals are assumed independent
* No real-time sensor data integration

---

## 🔮 Future Improvements

* Real-time traffic detection using computer vision
* Reinforcement learning for adaptive signals
* Dynamic service rate adjustment
* Integration with smart city infrastructure

---

## 👨‍💻 Author

Group 8

---

## 📜 License

This project is developed for academic purposes.
