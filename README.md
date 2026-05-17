# MIS-311
# 📊 Student Exam Performance — Exploratory Data Analysis

> **MIS 311 – Introduction to Business Analytics**
> - Eastern International University (EIU)
> - Nguyen Hoang Phuong 
---

<img width="1024" height="1024" alt="large-exam-hall-stockcake" src="https://github.com/user-attachments/assets/29135107-86bf-4f16-9c18-de8c5a02ca21" />

## 📌 Project Overview

This project performs an **Exploratory Data Analysis (EDA)** on a dataset of 10,000 secondary-school students to identify the key factors that influence final examination performance. The analysis employs two complementary tools: Microsoft Excel for structured PivotTable analysis and descriptive statistics, and Python (pandas, matplotlib, seaborn, scipy) for advanced visualisations including correlation heatmaps, regression scatter plots, box plots, and grade distribution charts.

---

## 🔍 Context for the data
Student academic performance is a central concern for educational institutions worldwide. While raw intelligence is often assumed to be the primary driver of exam success, a growing body of research suggests that behavioural factors such as study habits, sleep patterns, and digital media consumption play an equally important role. This case study uses a structured dataset to test that hypothesis and surface evidence-based guidance for educators and students.

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
<img width="940" height="140" alt="image" src="https://github.com/user-attachments/assets/c34bfdab-c52e-4b96-a776-cb1c239aa3dd" />

### PivotTable Analysis (Excel)
**Pivot Table 1 — Academic outcomes by gender**
 
| Gender | Students | Avg Final Score | Median Score | Pass Count | Fail Count | Pass Rate | Grade A (%) |
|--------|----------|----------------|--------------|------------|------------|-----------|-------------|
| Female | 4,987 | 49.80 | 49.65 | 2,504 | 2,483 | 50.2% | 5.1% |
| Male | 5,013 | 49.56 | 49.42 | 2,498 | 2,515 | 49.8% | 4.9% |
| **Total** | **10,000** | **49.68** | **49.55** | **5,002** | **4,998** | **50.0%** | **5.0%** |
 
> Gender has almost no impact — the difference in average score between female and male is only **0.24 points**.
 
---
 
**Pivot Table 2 — Academic outcomes by study hours per day**
 
| Study Hours/Day | Students | Avg Final Score | Pass Rate | Grade A (%) | Grade F (%) |
|-----------------|----------|----------------|-----------|-------------|-------------|
| 0 – 1 hr | 1,210 | 36.0 | 6.4% | 0.0% | 68.2% |
| 1 – 2 hrs | 1,850 | 42.1 | 24.7% | 0.3% | 44.6% |
| 2 – 3 hrs | 2,040 | 47.3 | 42.5% | 1.1% | 28.4% |
| 3 – 4 hrs | 1,930 | 52.8 | 63.2% | 2.8% | 13.6% |
| 4 – 5 hrs | 1,620 | 58.4 | 79.8% | 6.3% | 4.2% |
| 5 – 6 hrs | 890 | 63.9 | 91.5% | 11.7% | 0.9% |
| **6+ hrs** | **460** | **69.6** | **100%** | **19.2%** | **0.0%** |
 
> Each extra hour of study ≈ **+5.93 points** on the final exam (r = 0.576).
 

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
<img width="1487" height="1352" alt="figA_heatmap" src="https://github.com/user-attachments/assets/c7c1d609-c1de-44a1-bd18-ef80b3c00fd1" />

`previous_gpa`, `reading_score`, and `writing_score` are the strongest predictors. `social_media_hours` shows a weak negative correlation (r = −0.25).

### Figure B — Scatter Plot: Study Hours vs Final Exam Score
<img width="1936" height="765" alt="figB_scatter" src="https://github.com/user-attachments/assets/07b849df-15d1-4868-ad1f-5efbfce45f15" />

Clear positive trend confirmed with a regression line overlay.

### Figure C — Box Plot: Score by Family Background
<img width="1936" height="741" alt="figC_boxplot" src="https://github.com/user-attachments/assets/638568a4-d085-4c70-8e61-90b4deb0b5fc" />

Scores are nearly identical across all socioeconomic groups → family background has minimal impact.

### Figure D — Stacked Bar Chart: Grade Distribution by Study Hours

<img width="1336" height="735" alt="figD_grade_dist" src="https://github.com/user-attachments/assets/ca0571c1-4adf-4e18-8cbb-892900131a2c" />
As study hours increase, the share of A/B/C grades rises sharply and the failure rate drops.

---

## 🔍 Key Findings Summary

- 📚 **Study hours** is the #1 controllable factor — 6+ hours/day = 100% pass rate
- ⚠️ **49.68 average score** means ~half the class is at the pass/fail boundary
- 📱 **Social media** has a mild negative effect (−2 points per extra hour)
- 🏠 **Family background & gender** have almost no impact on results — outcomes are driven by **individual behaviour**
- 📉 `previous_gpa` (r ≈ 0.89) is the strongest predictor statistically, but it reflects the past **study habits are what students can change now**
  
->  Gender, parental education level, and family income demonstrate minimal to negligible impact on final exam scores. What matters most is the amount of time dedicated to studying and the extent to which distractions such as social media are managed. These conclusions are consistent across both Excel PivotTables and Python visualisations, lending them strong internal validity.
---
 
## 🐍 Why Python over Excel?
 
Excel is a great starting point — it's fast for quick lookups, pivot tables, and sharing with non-technical audiences. But for a dataset with **10,000 rows and 23 columns**, Python is clearly the better choice.

In this project, Excel was useful for a quick data overview and pivot tables. But Python handled everything else — the correlation heatmap, scatter plot, box plot, and stacked bar chart — in a way that is faster, more flexible, and easy to update whenever the data changes. For any analysis beyond a few hundred rows, Python is simply the more practical tool.
 
| | Excel | Python (pandas + seaborn) |
|---|---|---|
| **Speed** | Slows down on large files | Handles millions of rows instantly |
| **Reproducibility** | Manual steps are hard to repeat exactly | Code runs the same way every time |
| **Visualisation** | Basic charts, limited customisation | Full control over colour, style, layout |
| **Correlation analysis** | One formula at a time (`CORREL`) | Full matrix in one line: `df.corr()` |
| **Automation** | Copy-paste heavy | One script processes everything |
| **Version control** | Hard to track `.xlsx` changes on GitHub | `.ipynb` files diff cleanly on GitHub 

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
├── 13_Student_Exam_Performance.xlsx   ← Raw dataset (10,000 students, 23 columns)
├── eda.py                             ← Python EDA script (local run)
├── MIS311_EDA_Colab.py                ← Python EDA script (Google Colab version)
├── requirements.txt                   ← Python dependencies
├── output_figures/
│   ├── fig1_gender.png                ← Pivot chart: outcomes by gender
│   ├── fig2_study_hours.png           ← Pivot chart: outcomes by study hours
│   ├── fig3_histogram.png             ← Score distribution histogram
│   ├── figA_heatmap.png               ← Correlation heatmap
│   ├── figB_scatter.png               ← Scatter plot: study hours vs score
│   ├── figC_boxplot.png               ← Box plot: score by family background
│   └── figD_grade_dist.png            ← Stacked bar: grade distribution
└── README.md  ← You are here
```
---

## 👤 Author

**Nguyen Hoang Phuong**
MIS 311, Introduction to Business Analytics
Eastern International University
