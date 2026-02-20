# 🌞 AI-Powered Solar Energy Recommendation & Sustainability Analyzer

## 📌 Project Overview

This project is a **Machine Learning–based Decision Support System** designed to help individual households evaluate whether installing solar panels is technically feasible, financially beneficial, and environmentally impactful.

The system works **fully offline**, uses **no paid APIs**, and provides personalized solar adoption insights using data-driven modeling.

---

## 🎯 Objectives

The application helps users:

- 🔋 Predict expected solar energy generation using Machine Learning
- 📏 Recommend the optimal solar system size for their home
- 💰 Forecast long-term financial savings (10-year simulation)
- 🌍 Estimate CO₂ reduction and environmental benefits
- 📊 Generate a sustainability score
- 🖥️ Visualize insights through an interactive dashboard

---

## 🌍 Alignment With UN Sustainable Development Goals

- **SDG 7 — Affordable & Clean Energy**
- **SDG 13 — Climate Action**

---

## 🧠 Problem Statement

Most households lack access to:

- Personalized solar feasibility analysis
- Accurate savings prediction
- Environmental impact estimation
- Guidance on choosing the correct system size

Existing tools are often expensive, complex, or rely on external services.

This project creates a **free, explainable, AI-powered alternative**.

---

## 🏗️ System Architecture

```
User Inputs
   ↓
Data Processing Layer
   ↓
ML Prediction Engine
   ↓
Recommendation Engine
   ↓
Financial Simulation
   ↓
Carbon Impact Calculator
   ↓
Sustainability Scoring
   ↓
Visualization Dashboard (Streamlit UI)
```

---

## ⚙️ Core Functional Modules

### 🔹 Module A — Solar Energy Prediction (ML Core)

Predicts how much electricity a solar system will generate.

**Inputs:**

- Average sunlight hours
- Roof size (sq ft)
- System capacity (kW)
- Temperature (optional)

**Model Used:** Random Forest Regressor

**Output Example:**

```
Estimated Monthly Solar Generation: 430 kWh
```

---

### 🔹 Module B — Installation Recommendation Engine

Suggests the best solar setup using rule-based logic + clustering.

**Logic Example:**

```
Usage < 200 kWh → 1kW System
200–500 kWh → 3kW System
>500 kWh → 5kW System
```

---

### 🔹 Module C — Financial Savings Forecast

Simulates ROI over 10 years.

**Assumptions:**

- Electricity inflation: 5% / year
- Solar degradation: 0.5% / year
- Tariff: ₹7/kWh (configurable)

**Output Example:**

```
Break-Even: Year 4
10-Year Net Savings: ₹4.2 Lakhs
```

---

### 🔹 Module D — Carbon Impact Calculator

Converts solar energy into environmental impact.

**Standard Factor Used:**

```
1 kWh Grid Electricity = 0.82 kg CO₂
```

**Output Example:**

```
Annual CO₂ Reduction: 1.3 Tons
Equivalent Trees Planted: 62
```

---

### 🔹 Module E — Sustainability Score Engine

Calculates a composite eco-score.

**Formula:**

```
Score =
(Solar Contribution × 50)
+ (CO₂ Reduction × 30)
+ (Energy Independence × 20)
```

**Output Example:**

```
Green Score: 79 / 100
Rating: Sustainable Home
```

---

## 🖥️ User Interface

Built with **Streamlit** for rapid, Python-native dashboards.

### Pages:

1️⃣ User Input Panel
2️⃣ AI Recommendation Dashboard
3️⃣ Financial Forecast Visualization
4️⃣ Environmental Impact Dashboard
5️⃣ Sustainability Scorecard

---

## 🛠️ Technology Stack

| Layer            | Technology      |
| ---------------- | --------------- |
| Programming      | Python          |
| Machine Learning | Scikit-learn    |
| Data Processing  | Pandas, NumPy   |
| Visualization    | Plotly          |
| UI Framework     | Streamlit       |
| Model Storage    | Joblib          |
| Version Control  | Git + GitHub    |
| Deployment       | Streamlit Cloud |

---

## 📂 Project Structure

```
solar-ai/
│
├── data/
│   └── solar_data.csv
│
├── models/
│   └── energy_model.pkl
│
├── utils/
│   ├── predictor.py
│   ├── recommendation.py
│   ├── finance.py
│   ├── carbon.py
│   └── scoring.py
│
├── app/
│   └── streamlit_app.py
│
├── train_model.py
└── requirements.txt
```

---

## 🔄 Workflow

1️⃣ User enters household details
2️⃣ ML model predicts solar output
3️⃣ System recommends installation size
4️⃣ Financial simulation calculates savings
5️⃣ Carbon module estimates environmental impact
6️⃣ Sustainability score is generated
7️⃣ Dashboard visualizes results instantly

---

## 📊 What This Project Demonstrates

- Applied Machine Learning in sustainability
- Predictive + simulation-based decision systems
- Explainable AI for real-world engineering problems
- Data-driven environmental impact analysis
- End-to-end ML application development

---

## 🚀 Status

🔧 Currently under development — building ML pipeline and analysis modules.
