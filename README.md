# AI Lead Generation & Ranking Demo

This repository contains a **demo prototype** for an AI-based lead generation and ranking system.

The goal of this project is to simulate how a business development team can identify, enrich, and prioritize high-quality leads using structured data and simple AI-driven scoring logic.

---

## What this demo does

* Uses a **sample Indian biotech dataset** with relevant scientific and leadership roles
* Assigns a **probability score (0–100)** to each lead based on:

  * Role and seniority
  * Company funding stage
  * Usage of in-vitro / related technologies
  * Location hubs
  * Recent scientific publications
  * Conference participation
  * Tenure in current role
* Automatically **ranks leads** based on buying intent
* Exports the final ranked list as a **CSV**, which can be consumed directly in tools like Google Sheets or Excel

---

## Tech stack

* Python
* Streamlit
* Pandas
* Plotly

---

## How to run locally

1. Install dependencies:

   ```
   pip install pandas streamlit plotly
   ```

2. Run the app:

   ```
   streamlit run app.py
   ```

3. The dashboard will open in your browser, where you can:

   * View ranked leads
   * Search and filter results
   * Download the ranked output as CSV

---

## Output

The main output of this project is a **ranked leads table**, designed to reflect what a real business development or sales team would actually use to prioritize outreach.

---

## Note

This project is a **demo prototype** created as part of an **internship evaluation assignment for Euprime**.
The data used is synthetic and for demonstration purposes only.

---

## Author

Ayush Kumar Singh
B.Tech – Artificial Intelligence & Machine Learning
