import pdfplumber
import pymysql
import re

def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').strip()
#########################################
# Step 1: Extract text from PDF
with pdfplumber.open(r"C:\Users\Hari Hara Rajan\TIRUVOTTIYUR.pdf") as pdf:
    full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
DISTRICT_NAME = "Tiruvallur"
DISTRICT_ID =  1 # Will fetch automatically
CONSTITUENCY_NAME = "tiruvottiyur"
CONSTITUENCY_ID = 10 # <-- You asked for this specific ID

# Step 2: Extract polling station and streets
pattern = r'"(\d+)"\s*:\s*\{\s*"polling_station"\s*:\s*"([^"]+)",\s*"streets"\s*:\s*\[(.*?)\]\s*\}'
matches = re.findall(pattern, full_text, re.DOTALL)

# Step 3: Format data into rows
data_list = []
for match in matches:
    entry_id = int(match[0])
    polling_station = clean_text(match[1])
    streets_raw = match[2]
    streets = re.findall(r'"([^"]+)"', streets_raw)

    for street in streets:
        data_list.append({
            "id": entry_id,
            "district_name":DISTRICT_NAME,
            "district_id": DISTRICT_ID,
            "constitiuency":CONSTITUENCY_NAME,
            "constituency_id": CONSTITUENCY_ID,
            "polling_station": polling_station,
            "street_name": clean_text(street)
        })


conn = pymysql.connect(host="localhost", user="root", password="", database="polling_list", charset="utf8mb4")
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS TIRUVOTTIYUR_station_data")
##########################################
cursor.execute("""
CREATE TABLE TIRUVOTTIYUR_station_data (
    id INT,
    district_name TEXT,
    district_id INT,
    constitiuency TEXT,
    constituency_id INT,
    polling_station TEXT,
    street_name TEXT
);
""")

########################################3
for item in data_list:
    cursor.execute("""
        INSERT INTO TIRUVOTTIYUR_station_data 
        (id, district_name, district_id, constitiuency, constituency_id, polling_station, street_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        item["id"],
        item["district_name"],
        item["district_id"],
        item["constitiuency"],
        item["constituency_id"],
        item["polling_station"],
        item["street_name"]
    ))



conn.commit()
conn.close()
print(" Merged data inserted into `polling_station_data` table.")
