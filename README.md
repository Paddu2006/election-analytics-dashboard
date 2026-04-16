# Election Analytics Dashboard — India

Analysis of 2,263 candidates from Indian General Elections — uncovering patterns in party performance, gender representation, state-wise winners, age demographics, and education levels of elected representatives.

**By Padma Shree** | Data Science Journey

---

## 📊 The Problem

Indian elections generate massive amounts of data — but the insights remain buried. Citizens vote without knowing:
- Which parties truly dominate which states
- How many women actually win elections
- Whether age or education affects winning chances
- Which states have the most competitive seats

This project transforms raw election data into clear, actionable insights.

---

## 🔍 Key Findings

| Category | Finding |
|----------|---------|
| **Dominant Party** | BJP — 303 seats (56% of total) |
| **Second Place** | INC — 52 seats |
| **Women Winners** | 0% in this dataset (data quality issue) |
| **Top State** | Uttar Pradesh — 80 seats |
| **Karnataka (My State)** | 28 seats — 7th nationally |
| **Average Winner Age** | 54.4 years |
| **Average Loser Age** | 51.5 years |
| **Most Common Education** | Post Graduate (134 winners) |

---

## 📈 Charts Generated

| Chart | What It Shows |
|-------|----------------|
| `party_seats.png` | Top 10 parties by seats won |
| `gender_representation.png` | Women vs Men in Parliament |
| `state_winners.png` | Top 10 states by number of winners |
| `age_distribution.png` | Age comparison — winners vs losers |
| `education_analysis.png` | Education levels of winners |

---

## 🛠️ Tech Stack

- Python 3.13
- Pandas — Data loading and manipulation
- Matplotlib — Data visualization
- NumPy — Numerical operations

---

## 📂 Dataset

**Source:** Kaggle — Indian General Elections 2019

**Rows analyzed:** 2,263 candidates

**Columns:** 18 including STATE, PARTY, WINNER, GENDER, AGE, EDUCATION, VOTES

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Paddu2006/election-analytics-dashboard.git

# Install dependencies
pip install pandas matplotlib numpy

# Run the analysis
python election_analysis.py
