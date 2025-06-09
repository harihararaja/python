
import json
json_file_path ="C:\\Users\\Hari Hara Rajan\\Pictures\\p10.json"
with open(json_file_path, 'rb') as file:
    data = json.load(file)
    json_str = json.dumps(data, indent=2)
   # json_str_with_space = json_str.replace("},    \"", "},\n\n    \"")
   
print(json_str)
