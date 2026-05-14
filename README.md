# MIS--301
Introduction to Business Analytics
# 📊 Student Exam Performance — Exploratory Data Analysis

> **MIS 311 · Introduction to Business Analytics · Assignment #1 Part 1**
> Eastern International University (EIU)

---

## 📌 Project Overview

This project presents a full **Exploratory Data Analysis (EDA)** on a dataset of **10,000 secondary-school students**, investigating the behavioural, demographic, and academic factors that influence final examination performance.

The analysis was conducted using two complementary tools:
- **Microsoft Excel** — PivotTables, descriptive statistics, correlation functions, and charts
- **Python** — `pandas`, `matplotlib`, `seaborn`, `scipy` for advanced visualisations and statistical modelling

---

## 🎯 Key Questions

- Does daily study time meaningfully affect exam scores and pass rates?
- Does gender play a role in academic performance?
- Does social media usage hurt exam outcomes?
- Do background factors — parental education, family income — predict performance?

---

## 📁 Repository Structure

```
📦 student-exam-performance-eda/
│
├── 📂 data/
│   └── 13_Student_Exam_Performance.xlsx     # Raw dataset (10,000 rows × 23 cols)
│
├── 📂 output_figures/                        # All generated charts
│   ├── fig1_gender.png
│   ├── fig2_study_hours.png
│   ├── fig3_histogram.png
│   ├── figA_heatmap.png
│   ├── figB_scatter.png
│   ├── figC_boxplot.png
│   └── figD_grade_dist.png
│
├── 📂 excel/
│   └── MIS311_Analysis.xlsx                  # Excel workbook (PivotTables + Charts)
│
├── eda.py                                    # Main Python analysis script
├── requirements.txt                          # Python dependencies
└── README.md
```

---

## 🗃️ Dataset

| Attribute | Detail |
|-----------|--------|
| Source | MIS 311 Course Material, EIU |
| Rows | 10,000 students |
| Columns | 23 variables |
| Target Variables | `final_exam_score`, `pass_fail`, `grade_category` |
| Data Types | 13 numeric · 10 categorical |

**Key variables:** `study_hours_per_day`, `attendance_rate`, `social_media_hours`, `assignment_completion_rate`, `previous_gpa`, `parental_education`, `family_income`

---

## 🧹 Data Cleaning

| Check | Result |
|-------|--------|
| Missing values | ✅ 0 across all 23 columns |
| Duplicate rows | ✅ 0 full-row duplicates |
| Duplicate `student_id` | ✅ 0 |

The dataset was fully clean — **no imputation or removal required.**

---

## 📊 Excel Analysis

### Descriptive Statistics
Computed using `AVERAGE`, `STDEV`, `MIN`, `MAX`, `MEDIAN`, `QUARTILE` for 8 core numeric variables.

### PivotTable 1 — Performance by Gender

| Gender | Count | Avg Final Score | Pass Rate |
|--------|-------|----------------|-----------|
| Female | 4,987 | 49.81 | 48.91% |
| Male | 5,013 | 49.56 | 48.25% |

### PivotTable 2 — Performance by Study Hours / Day

| Study Hours | Count | Avg Score | Pass Rate |
|-------------|-------|-----------|-----------|
| 0 – 1 h | 485 | 35.96 | 6.4% |
| 1 – 2 h | 1,503 | 41.15 | 17.5% |
| 2 – 3 h | 2,982 | 46.83 | 37.0% |
| 3 – 4 h | 2,959 | 52.18 | 58.7% |
| 4 – 5 h | 1,586 | 58.22 | 80.1% |
| 5 – 6 h | 425 | 63.49 | 92.7% |
| 6 h + | 60 | 69.56 | **100.0%** |

### Correlation Table (CORREL function)

| Variable | r with `final_exam_score` |
|----------|--------------------------|
| `previous_gpa` | **+0.891** |
| `study_hours_per_day` | **+0.576** |
| `assignment_completion_rate` | +0.171 |
| `attendance_rate` | +0.151 |
| `sleep_hours` | +0.028 |
| `social_media_hours` | **−0.246** |

---

## 🐍 Python Analysis

### Figures Produced

| Figure | Chart Type | Key Finding |
|--------|-----------|-------------|
| Fig 1 | Bar Chart — Score by Gender | Female ≈ Male (Δ = 0.25 pts) |
| Fig 2 | Dual-axis Column + Line | Every +1 h study ≈ +6 pts, +15% pass rate |
| Fig 3 | Histogram — Score Distribution | Near-normal, mean 49.7; 51.7% fail |
| Fig A | Correlation Heatmap | `previous_gpa` dominates; `social_media` negative |
| Fig B | Scatter + Regression | slope = **+5.93**/hr, R² = 0.332, p < 0.001 |
| Fig C | Box Plot by Group | All education/income groups nearly identical |
| Fig D | Stacked Bar — Grade by Study Hrs | F-rate collapses from 94% → 0% as hours increase |

### Running the Code

```bash
# 1. Clone the repo
git clone https://github.com/your-username/student-exam-performance-eda.git
cd student-exam-performance-eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Place dataset in root folder, then run
python eda.py
```

Output figures are saved automatically to `./output_figures/`.

### Dependencies

```
pandas >= 2.0
numpy >= 1.24
matplotlib >= 3.7
seaborn >= 0.12
scipy >= 1.10
openpyxl >= 3.1
```

---

## 💡 Key Insights

### Insight 1 — Study Hours Is the Strongest Controllable Driver

> Every additional hour of daily study is associated with **+5.93 points** on the final exam (r = 0.576, R² = 0.332, p < 0.001). Students studying 6+ hours per day achieve a **100% pass rate**; those studying under 1 hour have only a **6.4% pass rate**.

**Implication:** Academic support should prioritise building structured daily study habits. Even a one-hour increase in daily study time produces a meaningful improvement in both score and pass likelihood.

---

### Insight 2 — Gender Is Negligible; Social Media Is a Hidden Risk

> Gender accounts for a difference of just **0.25 points** in average final score — statistically negligible. However, `social_media_hours` carries a correlation of **r = −0.246** with `final_exam_score` — the most harmful measurable behavioural variable in the dataset.

**Implication:** Across both genders, excessive social media use appears to displace study time. Digital wellness interventions could raise overall pass rates without targeting any specific demographic group.

---

### Insight 3 — Background Factors Do Not Predict Performance

> Box plots across all parental education levels (High School / Bachelor / Master / PhD) and all family income groups (Low / Medium / High) show **near-identical medians and IQRs** (~41–58). Background factors are not meaningful predictors of exam outcomes in this dataset.

**Implication:** Effort and behaviour are the primary levers — not socioeconomic background.

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Microsoft Excel | PivotTables, descriptive stats, CORREL(), Charts |
| Python — `pandas` | Data loading, groupby, aggregation |
| Python — `matplotlib` | All chart rendering |
| Python — `seaborn` | Heatmap, box plots |
| Python — `scipy.stats` | Regression, p-values |

---

## 📚 References

- Eastern International University (EIU). (2025). *Student Exam Performance dataset* [Course material]. MIS 311 – Introduction to Business Analytics.
- McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
- Waskom, M. (2021). seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021.

---

<p align="center">
  <sub>MIS 311 · Eastern International University · Assignment #1 Part 1</sub>
</p>
