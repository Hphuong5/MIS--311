# ╔══════════════════════════════════════════════════════════════════════════╗
# ║   MIS 311 – Student Exam Performance                                    ║
# ║   Exploratory Data Analysis — Full Code (Google Colab)                  ║
# ║   Dataset : 13_Student_Exam_Performance.xlsx                            ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────────────────────────
# CELL 1 │ Install & Import Libraries
# ──────────────────────────────────────────────────────────────────────────────
# !pip install openpyxl --quiet   # bỏ dấu # nếu chưa có openpyxl

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from scipy import stats

# Style chung
plt.rcParams.update({
    "font.family":  "DejaVu Sans",
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "axes.titlesize":     14,
    "axes.titleweight":   "bold",
    "axes.labelsize":     11,
    "xtick.labelsize":    10,
    "ytick.labelsize":    10,
    "figure.dpi":         130,
})

print("✅ Libraries loaded")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 2 │ Load Dataset
# ──────────────────────────────────────────────────────────────────────────────
# ── Cách 1: Upload file lên Colab rồi đọc ────────────────────────────────────
from google.colab import files

print("📂 Hãy upload file 13_Student_Exam_Performance.xlsx")
uploaded = files.upload()                          # chọn file từ máy tính
FILE = list(uploaded.keys())[0]                    # lấy tên file vừa upload

# ── Cách 2: Nếu file đã có sẵn trên Drive thì dùng dòng này thay thế ─────────
# from google.colab import drive
# drive.mount('/content/drive')
# FILE = '/content/drive/MyDrive/13_Student_Exam_Performance.xlsx'

df = pd.read_excel(FILE)
print(f"✅ Dataset loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
df.head()


# ──────────────────────────────────────────────────────────────────────────────
# CELL 3 │ Data Overview
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 55)
print("   DATA OVERVIEW")
print("=" * 55)
print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]}")
print(f"\nData Types:")
print(df.dtypes.value_counts().to_string())
print(f"\nColumn list:")
for col in df.columns:
    print(f"  • {col}")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 4 │ Data Cleaning — Missing Values & Duplicates
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 55)
print("   DATA CLEANING")
print("=" * 55)

# 4a. Missing values
missing = df.isnull().sum()
print(f"\n[Missing Values]")
if missing.sum() == 0:
    print("  ✅ 0 missing values across all columns")
else:
    print(missing[missing > 0])

# 4b. Duplicate rows
dup_full = df.duplicated().sum()
dup_id   = df.duplicated(subset="student_id").sum()
print(f"\n[Duplicate Rows]")
print(f"  Full-row duplicates  : {dup_full}")
print(f"  Duplicate student_id : {dup_id}")

if dup_full == 0 and dup_id == 0:
    print("  ✅ Dataset is clean — no action required")

# 4c. Basic dtype check
print(f"\n[Value Ranges — Quick Check]")
num_cols = df.select_dtypes(include="number").columns.tolist()
print(df[num_cols].agg(["min", "max"]).T.to_string())


# ──────────────────────────────────────────────────────────────────────────────
# CELL 5 │ Descriptive Statistics
# ──────────────────────────────────────────────────────────────────────────────
key_cols = [
    "age", "study_hours_per_day", "attendance_rate",
    "sleep_hours", "social_media_hours",
    "assignment_completion_rate", "final_exam_score", "previous_gpa"
]

desc = df[key_cols].describe().T
desc.columns = ["Count", "Mean", "Std", "Min", "25%", "Median", "75%", "Max"]
desc.index.name = "Variable"

print("=" * 55)
print("   DESCRIPTIVE STATISTICS")
print("=" * 55)
print(desc.round(2).to_string())


# ──────────────────────────────────────────────────────────────────────────────
# CELL 6 │ PivotTable 1 — Performance by Gender
# ──────────────────────────────────────────────────────────────────────────────
pivot_gender = (
    df.groupby("gender")
    .agg(
        Count              = ("student_id",       "count"),
        Avg_Final_Score    = ("final_exam_score",  "mean"),
        Avg_Math           = ("math_score",        "mean"),
        Avg_Reading        = ("reading_score",     "mean"),
        Avg_Attendance_Pct = ("attendance_rate",   "mean"),
        Pass_Rate_Pct      = ("pass_fail",         lambda x: (x == "Pass").mean() * 100),
    )
    .round(2)
)

print("=" * 55)
print("   PIVOTTABLE 1 — Performance by Gender")
print("=" * 55)
print(pivot_gender.to_string())


# ──────────────────────────────────────────────────────────────────────────────
# CELL 7 │ PivotTable 2 — Performance by Study Hours
# ──────────────────────────────────────────────────────────────────────────────
bins   = [0, 1, 2, 3, 4, 5, 6, 8]
labels = ["0–1h", "1–2h", "2–3h", "3–4h", "4–5h", "5–6h", "6h+"]
df["study_bin"] = pd.cut(df["study_hours_per_day"], bins=bins, labels=labels)

pivot_study = (
    df.groupby("study_bin", observed=True)
    .agg(
        Count           = ("student_id",       "count"),
        Avg_Final_Score = ("final_exam_score",  "mean"),
        Avg_Math        = ("math_score",        "mean"),
        Avg_Attendance  = ("attendance_rate",   "mean"),
        Avg_Study_Hrs   = ("study_hours_per_day","mean"),
        Pass_Rate_Pct   = ("pass_fail",         lambda x: (x == "Pass").mean() * 100),
    )
    .round(2)
)

print("=" * 55)
print("   PIVOTTABLE 2 — Performance by Study Hours/Day")
print("=" * 55)
print(pivot_study.to_string())


# ──────────────────────────────────────────────────────────────────────────────
# CELL 8 │ Correlation Table
# ──────────────────────────────────────────────────────────────────────────────
corr_cols = [
    "previous_gpa", "study_hours_per_day", "assignment_completion_rate",
    "attendance_rate", "participation_score", "sleep_hours",
    "social_media_hours", "final_exam_score"
]

corr_with_score = (
    df[corr_cols]
    .corr()["final_exam_score"]
    .drop("final_exam_score")
    .sort_values(ascending=False)
    .rename("Correlation (r)")
)

print("=" * 55)
print("   CORRELATION WITH final_exam_score")
print("=" * 55)
print(corr_with_score.round(3).to_string())


# ──────────────────────────────────────────────────────────────────────────────
# CELL 9 │ FIGURE 1 — Avg Final Score by Gender (Bar Chart — Excel style)
# ──────────────────────────────────────────────────────────────────────────────
genders = pivot_gender.index.tolist()
scores  = pivot_gender["Avg_Final_Score"].tolist()
pass_rt = pivot_gender["Pass_Rate_Pct"].tolist()
colors  = ["#2E75B6", "#E97132"]

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(genders, scores, color=colors, width=0.45, edgecolor="white", linewidth=1.5)

for bar, score, pr in zip(bars, scores, pass_rt):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"{score:.1f}\n(Pass: {pr:.1f}%)",
            ha="center", va="bottom", fontsize=10, fontweight="bold")

ax.set_ylim(0, 65)
ax.set_ylabel("Average Final Exam Score")
ax.set_xlabel("Gender")
ax.set_title("Average Final Exam Score by Gender")
ax.yaxis.set_major_locator(mticker.MultipleLocator(10))
plt.tight_layout()
plt.savefig("fig1_gender.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure 1 saved → fig1_gender.png")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 10 │ FIGURE 2 — Score & Pass Rate by Study Hours (Dual-axis)
# ──────────────────────────────────────────────────────────────────────────────
study_labels = pivot_study.index.tolist()
avg_scores   = pivot_study["Avg_Final_Score"].tolist()
pass_rates   = pivot_study["Pass_Rate_Pct"].tolist()

fig, ax1 = plt.subplots(figsize=(9, 5))
ax2 = ax1.twinx()

bars = ax1.bar(study_labels, avg_scores, color="#2980B9", alpha=0.85,
               width=0.55, edgecolor="white", label="Avg Exam Score")
ax2.plot(study_labels, pass_rates, color="#E74C3C", marker="o",
         linewidth=2.2, markersize=7, label="Pass Rate (%)")

for bar, score in zip(bars, avg_scores):
    ax1.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.8,
             f"{score:.1f}",
             ha="center", va="bottom", fontsize=9, fontweight="bold", color="#1B3A5C")

for x, pr in enumerate(pass_rates):
    ax2.text(x, pr + 2.5, f"{pr:.1f}%",
             ha="center", va="bottom", fontsize=9, color="#C0392B", fontweight="bold")

ax1.set_xlabel("Study Hours Per Day")
ax1.set_ylabel("Average Final Exam Score", color="#2980B9")
ax2.set_ylabel("Pass Rate (%)", color="#E74C3C")
ax1.set_ylim(0, 85)
ax2.set_ylim(0, 115)
ax1.set_title("Average Final Exam Score & Pass Rate by Study Hours Per Day")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.tight_layout()
plt.savefig("fig2_study_hours.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure 2 saved → fig2_study_hours.png")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 11 │ FIGURE 3 — Distribution of Final Exam Scores (Histogram)
# ──────────────────────────────────────────────────────────────────────────────
grade_colors = {
    "F (<50)":   "#E74C3C",
    "D (50–59)": "#E67E22",
    "C (60–69)": "#F1C40F",
    "B (70–79)": "#2ECC71",
    "A (80+)":   "#27AE60",
}

def grade_color(score):
    if score < 50:  return "#E74C3C"
    if score < 60:  return "#E67E22"
    if score < 70:  return "#F1C40F"
    if score < 80:  return "#2ECC71"
    return "#27AE60"

fig, ax = plt.subplots(figsize=(10, 5))
n, bins_h, patches = ax.hist(df["final_exam_score"], bins=40,
                              edgecolor="white", linewidth=0.6)
for patch in patches:
    patch.set_facecolor(grade_color(patch.get_x() + patch.get_width() / 2))

mean_val   = df["final_exam_score"].mean()
median_val = df["final_exam_score"].median()
ax.axvline(mean_val,   color="#1B3A5C", linestyle="--", linewidth=1.8,
           label=f"Mean = {mean_val:.1f}")
ax.axvline(median_val, color="#555555", linestyle=":",  linewidth=1.8,
           label=f"Median = {median_val:.1f}")

from matplotlib.patches import Patch
legend_patches = [Patch(color=c, label=l) for l, c in grade_colors.items()]
legend_patches += [
    plt.Line2D([0], [0], color="#1B3A5C", linestyle="--", linewidth=1.8, label=f"Mean = {mean_val:.1f}"),
    plt.Line2D([0], [0], color="#555555", linestyle=":",  linewidth=1.8, label=f"Median = {median_val:.1f}"),
]
ax.legend(handles=legend_patches, fontsize=9, ncol=2)

ax.set_xlabel("Final Exam Score")
ax.set_ylabel("Number of Students")
ax.set_title("Distribution of Final Exam Scores")
plt.tight_layout()
plt.savefig("fig3_histogram.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure 3 saved → fig3_histogram.png")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 12 │ FIGURE A — Correlation Heatmap (Python / seaborn)
# ──────────────────────────────────────────────────────────────────────────────
heatmap_cols = [
    "study_hours_per_day", "attendance_rate", "sleep_hours",
    "social_media_hours",  "assignment_completion_rate",
    "participation_score", "math_score", "reading_score",
    "writing_score",       "science_score",
    "final_exam_score",    "previous_gpa",
]

corr_matrix = df[heatmap_cols].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))   # chỉ vẽ nửa dưới

fig, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 20, as_cmap=True)
sns.heatmap(
    corr_matrix, mask=mask, cmap=cmap,
    vmax=1, vmin=-1, center=0,
    annot=True, fmt=".2f", annot_kws={"size": 8},
    linewidths=0.5, ax=ax, square=True,
)
ax.set_title("Figure A — Correlation Heatmap (Numeric Variables)", pad=16)
plt.tight_layout()
plt.savefig("figA_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure A saved → figA_heatmap.png")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 13 │ FIGURE B — Scatter Plot + Regression Line
# ──────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

PAIRS = [
    ("study_hours_per_day", "Study Hours Per Day",   "#2980B9", "#1B3A5C"),
    ("social_media_hours",  "Social Media Hours/Day", "#E74C3C", "#7B241C"),
]

for ax, (xvar, xlabel, dot_color, line_color) in zip(axes, PAIRS):
    sample = df.sample(800, random_state=42)
    ax.scatter(sample[xvar], sample["final_exam_score"],
               alpha=0.22, color=dot_color, s=18, linewidths=0)

    slope, intercept, r, p, se = stats.linregress(df[xvar], df["final_exam_score"])
    x_line = np.linspace(df[xvar].min(), df[xvar].max(), 200)
    ax.plot(x_line, slope * x_line + intercept,
            color=line_color, linewidth=2.2, label=f"y = {slope:+.2f}x + {intercept:.1f}")

    p_label = "p < 0.001" if p < 0.001 else f"p = {p:.4f}"
    ax.text(0.04, 0.93,
            f"r = {r:.3f}    R² = {r**2:.3f}\n{p_label}",
            transform=ax.transAxes, fontsize=10,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#EBF4FA",
                      edgecolor="#AED6F1", alpha=0.9))

    ax.set_xlabel(xlabel)
    ax.set_ylabel("Final Exam Score")
    ax.set_title(f"{xlabel} vs Final Exam Score")
    ax.legend(fontsize=9)

fig.suptitle("Figure B — Scatter Plots with Regression Lines", fontsize=14,
             fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig("figB_scatter.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure B saved → figB_scatter.png")
print(f"\n   Study Hours:  slope = {stats.linregress(df['study_hours_per_day'], df['final_exam_score'])[0]:+.3f}")
print(f"   Social Media: slope = {stats.linregress(df['social_media_hours'],  df['final_exam_score'])[0]:+.3f}")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 14 │ FIGURE C — Box Plot by Parental Education & Family Income
# ──────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# ── Left: Parental Education ──────────────────────────────────────────────────
edu_order  = ["High School", "Bachelor", "Master", "PhD"]
edu_data   = [df[df["parental_education"] == g]["final_exam_score"].values
              for g in edu_order]
edu_colors = ["#3498DB", "#2ECC71", "#E67E22", "#9B59B6"]

bp1 = axes[0].boxplot(edu_data, patch_artist=True, widths=0.45,
                      medianprops=dict(color="white", linewidth=2.5),
                      whiskerprops=dict(linewidth=1.2),
                      capprops=dict(linewidth=1.2),
                      flierprops=dict(marker="o", markersize=3, alpha=0.3))
for patch, color in zip(bp1["boxes"], edu_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.78)

for i, data in enumerate(edu_data, 1):
    med = np.median(data)
    axes[0].text(i, med + 1.2, f"{med:.1f}",
                 ha="center", va="bottom", fontsize=9,
                 fontweight="bold", color="white",
                 bbox=dict(boxstyle="round,pad=0.2",
                           facecolor=edu_colors[i-1], alpha=0.85))

axes[0].set_xticks(range(1, len(edu_order) + 1))
axes[0].set_xticklabels(edu_order, fontsize=9)
axes[0].set_ylabel("Final Exam Score")
axes[0].set_title("By Parental Education Level")
axes[0].set_ylim(0, 110)

# ── Right: Family Income ──────────────────────────────────────────────────────
inc_order  = ["Low", "Medium", "High"]
inc_data   = [df[df["family_income"] == g]["final_exam_score"].values
              for g in inc_order]
inc_colors = ["#E74C3C", "#F39C12", "#27AE60"]

bp2 = axes[1].boxplot(inc_data, patch_artist=True, widths=0.45,
                      medianprops=dict(color="white", linewidth=2.5),
                      whiskerprops=dict(linewidth=1.2),
                      capprops=dict(linewidth=1.2),
                      flierprops=dict(marker="o", markersize=3, alpha=0.3))
for patch, color in zip(bp2["boxes"], inc_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.78)

for i, data in enumerate(inc_data, 1):
    med = np.median(data)
    axes[1].text(i, med + 1.2, f"{med:.1f}",
                 ha="center", va="bottom", fontsize=9,
                 fontweight="bold", color="white",
                 bbox=dict(boxstyle="round,pad=0.2",
                           facecolor=inc_colors[i-1], alpha=0.85))

axes[1].set_xticks(range(1, len(inc_order) + 1))
axes[1].set_xticklabels(inc_order)
axes[1].set_ylabel("Final Exam Score")
axes[1].set_title("By Family Income Level")
axes[1].set_ylim(0, 110)

fig.suptitle("Figure C — Score Distribution by Parental Education & Family Income",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("figC_boxplot.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure C saved → figC_boxplot.png")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 15 │ FIGURE D — Grade Distribution by Study Hours (Stacked Bar %)
# ──────────────────────────────────────────────────────────────────────────────
grade_order  = ["A", "B", "C", "D", "F"]
grade_colors = {"A": "#27AE60", "B": "#2ECC71",
                "C": "#F1C40F", "D": "#E67E22", "F": "#E74C3C"}

pivot_grade = (
    df.groupby(["study_bin", "grade_category"], observed=True)
    .size()
    .unstack(fill_value=0)
    .reindex(columns=grade_order, fill_value=0)
)
pct = pivot_grade.div(pivot_grade.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(9, 5))
bottom = np.zeros(len(pct))

for grade in grade_order:
    vals = pct[grade].values
    bars = ax.bar(pct.index, vals, bottom=bottom,
                  color=grade_colors[grade], label=f"Grade {grade}",
                  edgecolor="white", linewidth=0.7, width=0.62)
    for bar, val, bot in zip(bars, vals, bottom):
        if val >= 8:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bot + val / 2,
                    f"{val:.0f}%",
                    ha="center", va="center",
                    fontsize=8.5, color="white", fontweight="bold")
    bottom += vals

ax.set_ylim(0, 105)
ax.set_ylabel("Percentage of Students (%)")
ax.set_xlabel("Study Hours Per Day")
ax.set_title("Figure D — Grade Distribution (%) by Study Hours Per Day")
ax.legend(title="Grade", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=9)
plt.tight_layout()
plt.savefig("figD_grade_dist.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Figure D saved → figD_grade_dist.png")


# ──────────────────────────────────────────────────────────────────────────────
# CELL 16 │ Download All Figures (optional)
# ──────────────────────────────────────────────────────────────────────────────
import zipfile, os

figures = [
    "fig1_gender.png", "fig2_study_hours.png", "fig3_histogram.png",
    "figA_heatmap.png", "figB_scatter.png", "figC_boxplot.png", "figD_grade_dist.png"
]

with zipfile.ZipFile("MIS311_figures.zip", "w") as zf:
    for f in figures:
        if os.path.exists(f):
            zf.write(f)

files.download("MIS311_figures.zip")
print("✅ All figures downloaded → MIS311_figures.zip")
