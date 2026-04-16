# Election Analytics Dashboard — India
# By Padma Shree
# Project 7 of 25

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=== ELECTION ANALYTICS DASHBOARD — INDIA ===\n")

# Load the data
file_path = r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\05_resources\datasets\election_results.csv"
df = pd.read_csv(file_path)

print(f"✅ Loaded {len(df)} candidates across India\n")

# Clean column names (remove special characters)
df.columns = df.columns.str.replace('\n', ' ')

# ============================================
# PROBLEM 1: Which parties win the most seats?
# ============================================
print("=" * 50)
print("📊 PARTY PERFORMANCE ANALYSIS")
print("=" * 50)

# Filter only winners (WINNER = 1)
winners = df[df['WINNER'] == 1]
party_seats = winners['PARTY'].value_counts()

print("\n🏆 TOP 10 PARTIES BY SEATS WON:")
for i, (party, seats) in enumerate(party_seats.head(10).items(), 1):
    print(f"{i}. {party}: {seats} seats")

# Chart
plt.figure(figsize=(12, 6))
party_seats.head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Parties by Seats Won', fontsize=14)
plt.xlabel('Party')
plt.ylabel('Number of Seats')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('party_seats.png')
plt.show()

# ============================================
# PROBLEM 2: How many women won elections?
# ============================================
print("\n" + "=" * 50)
print("👩 GENDER REPRESENTATION")
print("=" * 50)

women_winners = winners[winners['GENDER'] == 'F']
women_count = len(women_winners)
total_winners = len(winners)
women_percentage = (women_count / total_winners) * 100

print(f"Total Winners: {total_winners}")
print(f"Women Winners: {women_count}")
print(f"Men Winners: {total_winners - women_count}")
print(f"Women Representation: {women_percentage:.1f}%")

# Chart
plt.figure(figsize=(6, 6))
gender_counts = [women_count, total_winners - women_count]
plt.pie(gender_counts, labels=['Women', 'Men'], autopct='%1.1f%%', colors=['pink', 'lightblue'])
plt.title('Gender Representation in Parliament', fontsize=14)
plt.savefig('gender_representation.png')
plt.show()

# ============================================
# PROBLEM 3: Which states have the most winners?
# ============================================
print("\n" + "=" * 50)
print("📍 STATE-WISE WINNERS")
print("=" * 50)

state_winners = winners['STATE'].value_counts()
print("\n🏆 TOP 10 STATES BY NUMBER OF WINNERS:")
for i, (state, count) in enumerate(state_winners.head(10).items(), 1):
    print(f"{i}. {state}: {count} seats")

# Chart
plt.figure(figsize=(12, 6))
state_winners.head(10).plot(kind='bar', color='green')
plt.title('Top 10 States by Number of Winners', fontsize=14)
plt.xlabel('State')
plt.ylabel('Number of Winners')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('state_winners.png')
plt.show()

# ============================================
# PROBLEM 4: Average age of winners vs losers
# ============================================
print("\n" + "=" * 50)
print("👤 AGE ANALYSIS")
print("=" * 50)

# Clean age column (remove non-numeric)
df['AGE'] = pd.to_numeric(df['AGE'], errors='coerce')
winners_age = winners['AGE'].dropna()
losers_age = df[df['WINNER'] == 0]['AGE'].dropna()

print(f"Average age of WINNERS: {winners_age.mean():.1f} years")
print(f"Average age of LOSERS: {losers_age.mean():.1f} years")

# Age distribution chart
plt.figure(figsize=(10, 6))
plt.hist(winners_age, bins=20, alpha=0.7, label='Winners', color='green')
plt.hist(losers_age, bins=20, alpha=0.5, label='Losers', color='red')
plt.xlabel('Age')
plt.ylabel('Number of Candidates')
plt.title('Age Distribution: Winners vs Losers', fontsize=14)
plt.legend()
plt.savefig('age_distribution.png')
plt.show()

# ============================================
# PROBLEM 5: Education level of winners
# ============================================
print("\n" + "=" * 50)
print("🎓 EDUCATION ANALYSIS OF WINNERS")
print("=" * 50)

education_counts = winners['EDUCATION'].value_counts().head(10)
print("\nTop 10 Education Levels Among Winners:")
for i, (edu, count) in enumerate(education_counts.items(), 1):
    print(f"{i}. {edu}: {count} winners")

# Chart
plt.figure(figsize=(12, 6))
education_counts.plot(kind='bar', color='purple')
plt.title('Top 10 Education Levels Among Winners', fontsize=14)
plt.xlabel('Education Level')
plt.ylabel('Number of Winners')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('education_analysis.png')
plt.show()

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 50)
print("📋 SUMMARY OF FINDINGS")
print("=" * 50)
print(f"✅ Total Candidates Analyzed: {len(df)}")
print(f"✅ Total Winners: {total_winners}")
print(f"✅ Dominant Party: {party_seats.index[0]} ({party_seats.iloc[0]} seats)")
print(f"✅ Women in Parliament: {women_percentage:.1f}%")
print(f"✅ Average Winner Age: {winners_age.mean():.1f} years")
print(f"✅ Most Common Education: {education_counts.index[0]}")

print("\n✅ PROJECT 7 COMPLETE! All charts saved.")