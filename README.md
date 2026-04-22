# 🏦 Indian Banking Sector Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)  
*An interactive dashboard for analyzing the Indian banking industry (2013–2023)*

![Dashboard Preview](https://via.placeholder.com/800x400?text=BankSight+Pro+Dashboard)

## 📊 Overview

This project provides a comprehensive analytics platform for the Indian banking sector. It visualises key metrics such as **deposits**, **credit**, **NPAs** (Non‑Performing Assets), and **profits** across three categories:

- 🏛️ **Public Sector Banks** (PSBs)
- 📈 **Private Sector Banks**
- 🌍 **Foreign Banks**

The dashboard covers the period **2013–2023** and includes built‑in data editing, year‑comparison tools, and a premium fintech‑style money rain animation on successful data saves.

## ✨ Features

- **Interactive Dashboard** – KPIs, year cards, and sector distribution.
- **Trends & Charts** – Line, bar, pie, scatter, and area charts with multi‑metric comparisons.
- **Sector Deep Dive** – Isolate any banking sector and analyse its performance and market share.
- **Year Comparison** – Compare 2 or 3 years side by side, view percentage changes, and visualise trends.
- **Data Management** – Edit data inline, upload new CSV files, reset to defaults, and export to CSV/Excel/JSON.
- **Premium UI** – Glassmorphism, gradient backgrounds, animated metrics, and a custom money rain effect (replaces `st.balloons`).
- **Responsive** – Works on desktop and tablets.

## 🛠️ Tech Stack

- **Python** 3.9+
- **Streamlit** – Interactive web app framework
- **Pandas** – Data manipulation
- **Plotly** – Interactive visualisations
- **NumPy** – Numerical operations

## 📁 Data Structure

The dataset contains the following columns (all monetary values in ₹ Crore):

| Column               | Description                          |
|----------------------|--------------------------------------|
| Year                 | 2013 – 2023                          |
| PSB_Deposits         | Public Sector Bank deposits          |
| PSB_Credit           | Public Sector Bank credit            |
| PSB_NPA              | Public Sector Bank NPA (%)           |
| PSB_Profit           | Public Sector Bank profit            |
| Private_Deposits     | Private Sector Bank deposits         |
| Private_Credit       | Private Sector Bank credit           |
| Private_NPA          | Private Sector Bank NPA (%)          |
| Private_Profit       | Private Sector Bank profit           |
| Foreign_Deposits     | Foreign Bank deposits                |
| Foreign_Credit       | Foreign Bank credit                  |
| Foreign_NPA          | Foreign Bank NPA (%)                 |
| Foreign_Profit       | Foreign Bank profit                  |
| GDP_Growth           | India’s GDP growth rate (%)          |

*Total columns (Deposits, Credit, NPA, Profit) are automatically calculated.*

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/banking-analytics-dashboard.git
   cd banking-analytics-dashboard
