import pandas as pd
import json
import os

# ─────────────────────────────────────────────
# PART A: CSV — Comma-Separated Values
# ─────────────────────────────────────────────

# Create a sample students.csv if it doesn't already exist
if not os.path.exists("students.csv"):
    sample_csv = "Name,Score,Department\nJohn,78,Cybersecurity\nMary,85,Computer Science\nAyo,90,Cybersecurity\nAda,,Computer Science"
    with open("students.csv", "w") as f:
        f.write(sample_csv)
    print("students.csv created.\n")

# Load CSV
data = pd.read_csv("students.csv")
print("=== CSV Data (first 5 rows) ===")
print(data.head())
print()
print("=== Dataset Info ===")
print(data.info())

# Real-world use: Bank transaction reports, audit records

# ─────────────────────────────────────────────
# PART B: JSON — JavaScript Object Notation
# ─────────────────────────────────────────────

# Parse a JSON string
json_string = '{"name": "Ayo", "age": 22}'
parsed = json.loads(json_string)
print("\n=== Parsed JSON ===")
print(f"Name: {parsed['name']}")   # Output: Ayo
print(f"Age:  {parsed['age']}")    # Output: 22

# Write JSON to file and read it back
student_record = {"name": "Ayo", "course": "Cybersecurity", "level": 300}
with open("student.json", "w") as f:
    json.dump(student_record, f, indent=4)

with open("student.json", "r") as f:
    loaded = json.load(f)
print("\n=== JSON from File ===")
print(loaded)

# Real-world use: Social media APIs, cloud configs