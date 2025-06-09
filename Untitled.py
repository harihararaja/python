import fitz  # PyMuPDF
import json
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_polling_data(raw_text):
    blocks = re.split(r'\bALL VOTERS\b', raw_text)
    records = {}
    record_id = 1

    for block in blocks:
        lines = block.strip().splitlines()
        if not lines or "[1]" not in block:
            continue

        # Extract polling station name
        loc_lines = []
        ward_start_index = 0
        for i, line in enumerate(lines):
            if "[1]" in line:
                ward_start_index = i
                break
            loc_lines.append(line.strip())

        polling_station = " ".join(loc_lines).replace("  ", " ").replace("\n", " ").strip(",")

        # Extract streets
        ward_text = " ".join(lines[ward_start_index:])
        streets = re.findall(r'\[\d+\] -\s*(.*?)(?=\[\d+\]|$)', ward_text, re.DOTALL)
        streets = [s.replace("\n", " ").replace(" ,", ",").strip(" ,") for s in streets if s.strip()]

        # Store structured data
        records[str(record_id)] = {
            "polling_station": polling_station,
            "streets": streets
        }
        record_id += 1

    return records

# Input/output paths
pdf_path = "C:\\Users\\Hari Hara Rajan\\Pictures\\p10.pdf"
json_output_path = "C:\\Users\\Hari Hara Rajan\\Pictures\\p10.json"

# Process PDF and extract structured data
pdf_text = extract_text_from_pdf(pdf_path)
structured_data = parse_polling_data(pdf_text)

# Save to JSON
with open(json_output_path, 'w', encoding='utf-8') as json_file:
    json.dump(structured_data, json_file, indent=4, ensure_ascii=False)

print(f"Structured polling data saved to: {json_output_path}")

