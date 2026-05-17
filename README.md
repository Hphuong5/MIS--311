# MIS-311
Introduction to Business Analytics
# 📊 Student Exam Performance — Exploratory Data Analysis

> # 📊 Student Academic Performance — Exploratory Data Analysis (EDA)

> **MIS 311 – Introduction to Business Analytics**
> Eastern International University (EIU)
> Assignment #1 | Nguyen Hoang Phuong – IRN: 2132300068

---

## 📌 Project Overview

This project performs an **Exploratory Data Analysis (EDA)** on a dataset of 10,000 students to investigate how behavioural factors — such as study habits, social media usage, and attendance — affect final exam performance.

The goal is to uncover actionable insights that can help students and educators make better decisions to improve academic outcomes.

---

## 🗂️ Dataset Description

| Attribute | Detail |
|---|---|
| 📁 Source | MIS 311 course material, Eastern International University |
| 👥 Records | 10,000 students |
| 📐 Variables | 23 columns (13 numeric, 10 categorical) |
| 🎂 Age Range | 15 – 18 years old |
| ⚧ Gender Split | Female: 49.9% · Male: 50.1% |
| 🎯 Key Outcome | `final_exam_score`, `pass_fail`, `grade_category` |
| 🔍 Key Predictors | `study_hours_per_day`, `attendance_rate`, `social_media_hours`, `previous_gpa` |

### 📖 Variable Glossary

| Variable | Description |
|---|---|
| `study_hours_per_day` | Average hours the student studies per day |
| `attendance_rate` | % of classes attended (0–100%) |
| `social_media_hours` | Average daily hours on social media |
| `assignment_completion_rate` | % of assignments submitted on time |
| `previous_gpa` | GPA from the previous academic period (0.0–4.0) |
| `final_exam_score` | Final exam score (0–100) |
| `pass_fail` | Pass (≥ 50) or Fail (< 50) |
| `grade_category` | Letter grade: A (80+), B (70–79), C (60–69), D (50–59), F (<50) |
| `parental_education` | Parent's highest education: High School / Bachelor / Master / PhD |
| `family_income` | Household income level: Low / Medium / High |

---

## 🧹 Data Cleaning

The dataset was checked for quality issues using both **Excel** and **Python (pandas)**.

| Check | Excel Method | Python Method | Result |
|---|---|---|---|
| Missing Values | Home → Find & Select → Go To Special → Blanks | `df.isnull().sum()` | ✅ 0 missing values |
| Duplicate Rows | Data → Remove Duplicates (by `student_id`) | `df.duplicated().sum()` | ✅ 0 duplicates |

> **Conclusion:** The dataset was already clean — no further cleaning was needed.

---

## 📈 Descriptive Statistics

Calculated using Excel (`AVERAGE`, `STDEV`, `MIN`, `MAX`, `MEDIAN`) and verified with `df.describe()` in Python.

### Summary Statistics
<!-- Insert Figure 1: Summary Statistics Table here -->

### PivotTable Analysis (Excel)
- **Pivot Table 1:** Academic outcomes by **gender**
- **Pivot Table 2:** Academic outcomes by **study hours per day**

<!-- Insert Figure 2: Pivot Table – Academic Outcomes by Study Hours Per Day here -->

### Correlation Analysis

Calculated with Excel's `CORREL` function and Python's `df.corr()`.

| Variable Pair | Correlation (r) | Interpretation |
|---|---|---|
| `previous_gpa` ↔ `final_exam_score` | **r ≈ 0.89** | Very strong positive |
| `study_hours_per_day` ↔ `final_exam_score` | **r = 0.576** | Moderate positive |
| `social_media_hours` ↔ `final_exam_score` | **r = −0.25** | Weak negative |

---

## 💡 Key Insights

### Insight 1 — Most Students Are Right at the Pass/Fail Line
> The average final exam score is **49.68** (SD = 12.15), just below the passing threshold of 50. The median is 49.55. Nearly half of all students are sitting right at the boundary — meaning even a small improvement in behaviour could push many from **Fail → Pass**.

### Insight 2 — Study Hours Have a Huge Impact
> Daily study time is the **most important controllable factor**.

| Study Hours/Day | Avg Score | Pass Rate |
|---|---|---|
| 0 – 1 hour | 36.0 | 6.4% |
| 6+ hours | 69.6 | **100%** |

Each additional hour of study ≈ **+5.93 points** on the final exam.

---

## 🐍 Python Visualisations

Analysis was conducted using `pandas`, `matplotlib`, and `seaborn`.

### Figure A — Correlation Heatmap
<!-- Insert Figure A: Correlation Heatmap of Numeric Variables here -->
`previous_gpa`, `reading_score`, and `writing_score` are the strongest predictors. `social_media_hours` shows a weak negative correlation (r = −0.25).

### Figure B — Scatter Plot: Study Hours vs Final Exam Score
<!-- Insert Figure B: Scatter Plot with Regression Line here -->
Clear positive trend confirmed with a regression line overlay.

### Figure C — Box Plot: Score by Family Background
<!-- Insert Figure C: Box Plot – Parental Education & Family Income here -->
Scores are nearly identical across all socioeconomic groups → family background has minimal impact.

### Figure D — Stacked Bar Chart: Grade Distribution by Study Hours
<!-- Insert Figure D: Stacked Bar Chart here -->
As study hours increase, the share of A/B/C grades rises sharply and the failure rate drops.

---

## 🔍 Key Findings Summary

- 📚 **Study hours** is the #1 controllable factor — 6+ hours/day = 100% pass rate
- ⚠️ **49.68 average score** means ~half the class is at the pass/fail boundary
- 📱 **Social media** has a mild negative effect (−2 points per extra hour)
- 🏠 **Family background & gender** have almost no impact on results — outcomes are driven by **individual behaviour**
- 📉 `previous_gpa` (r ≈ 0.89) is the strongest predictor statistically, but it reflects the past — **study habits are what students can change now**

---

## 🛠️ Tools Used

![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-4c9be8?style=flat)

---

## 📁 Repository Structure

```
MIS311/
├── README.md               ← You are here
├── data/
│   └── student_data.csv    ← Dataset
├── notebooks/
│   └── EDA_Analysis.ipynb  ← Python EDA notebook
├── excel/
│   └── EDA_Analysis.xlsx   ← Excel analysis & PivotTables
└── report/
    └── MIS311_EDA_Report.docx ← Full written report
```

---

## 👤 Author

**Nguyen Hoang Phuong**
IRN: 2132300068
Eastern International University — MIS 311, Introduction to Business Analytics
