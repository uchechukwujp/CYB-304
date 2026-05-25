import xml.etree.ElementTree as ET
import pandas as pd
import os

# ─────────────────────────────────────────────
# PART A: XML — Extensible Markup Language
# ─────────────────────────────────────────────

xml_data = """<student>
    <name>Ada</name>
    <department>Cybersecurity</department>
    <level>300</level>
</student>"""

# Parse XML string
root = ET.fromstring(xml_data)
print("=== XML Parsed Data ===")
print(f"Name:       {root.find('name').text}")         # Ada
print(f"Department: {root.find('department').text}")   # Cybersecurity
print(f"Level:      {root.find('level').text}")        # 300

# Save XML to file and read it back
tree = ET.ElementTree(root)
tree.write("student.xml")
print("\nstudent.xml saved.\n")

# Real-world use: Banking systems, enterprise apps

# ─────────────────────────────────────────────
# PART B: Data Ingestion Workflow
# ─────────────────────────────────────────────

# Batch Ingestion — data imported periodically (e.g., monthly payroll)
print("=== Batch Ingestion ===")

# Create students.csv if it doesn't already exist
if not os.path.exists("students.csv"):
    sample_csv = "Name,Score,Department\nJohn,78,Cybersecurity\nMary,85,Computer Science\nAyo,90,Cybersecurity\nAda,,Computer Science"
    with open("students.csv", "w") as f:
        f.write(sample_csv)

# Data cleaning pipeline
data = pd.read_csv("students.csv")
print("Missing values per column:")
print(data.isnull().sum())

cleaned = data.dropna()                         # Remove rows with missing values
cleaned.to_csv("cleaned.csv", index=False)      # Save cleaned file

print(f"\nOriginal rows : {len(data)}")
print(f"Cleaned rows  : {len(cleaned)}")
print("cleaned.csv saved.\n")

# Real-Time Ingestion — continuous streaming (e.g., ATM transactions)
print("=== Simulated Real-Time Ingestion ===")
import time

transactions = [
    {"id": 1, "amount": 5000, "type": "withdrawal"},
    {"id": 2, "amount": 20000, "type": "deposit"},
    {"id": 3, "amount": 1500, "type": "withdrawal"},
]

for txn in transactions:
    print(f"[LIVE] Processing transaction {txn['id']}: ₦{txn['amount']:,} — {txn['type'].upper()}")
    time.sleep(0.5)   # Simulates real-time delay

print("\nAll transactions processed.")