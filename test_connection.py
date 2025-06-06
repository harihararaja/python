import pdfplumber
import pymysql
import json
import re

def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').strip()


CONSTITUENCY = "ponneri"


with pdfplumber.open(r"C:\Users\Hari Hara Rajan\ponneri.pdf") as pdf:
    full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)


pattern = r'"(\d+)"\s*:\s*\{\s*"polling_station"\s*:\s*"([^"]+)",\s*"streets"\s*:\s*\[(.*?)\]\s*\}'
matches = re.findall(pattern, full_text, re.DOTALL)

data_list = []

for match in matches:
    entry_id = int(match[0])
    polling_station = clean_text(match[1])
    streets_raw = match[2]
    streets = re.findall(r'"([^"]+)"', streets_raw)
    data_list.append({
        "id": entry_id,
        "constituency": CONSTITUENCY,
        "polling_station": polling_station,
        "streets": streets
    })


conn = pymysql.connect(host="localhost", user="root", password="", database="polling_list", charset="utf8mb4")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS polling_station (
    id INT PRIMARY KEY,
    constituency VARCHAR(100),
    name TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS streets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    polling_station_id INT,
    street_name TEXT,
    FOREIGN KEY (polling_station_id) REFERENCES polling_station(id) ON DELETE CASCADE
);
""")


for item in data_list:
    cursor.execute(
        "REPLACE INTO polling_station (id, constituency, name) VALUES (%s, %s, %s)",
        (item["id"], item["constituency"], item["polling_station"])
    )

    for street in item["streets"]:
        cursor.execute(
            "INSERT INTO streets (polling_station_id, street_name) VALUES (%s, %s)",
            (item["id"], street)
        )

conn.commit()
conn.close()

print("Data imported into 2 related tables using foreign keys.")
