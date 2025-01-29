import pdfplumber
import json

# with pdfplumber.open("list.pdf") as pdf:
#     for page in pdf.pages:
#         print(page.extract_text())  # Check what raw text extraction gives you


import pdfplumber
import json
import re

def extract_text_from_pdf(pdf_path):
    extracted_lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_lines.extend(text.split("\n"))  # Split by line

    return extracted_lines

def parse_lines_to_json(lines):
    structured_data = []
    
    for line in lines:
        # Regex to capture structured text with License Number, Address, Expiration, Company, and Owner
        match = re.match(r"(\S+)\s+(.+?)\s+(\d{1,2}/\d{1,2}/\d{4})\s+(.+?)\s+([\w\s,&-]+)", line)
        
        if match:
            license_number, address, expiration_date, management_company, owner = match.groups()
            structured_data.append({
                "License Number": license_number.strip(),
                "Property Address": address.strip(),
                "Expiration Date": expiration_date.strip(),
                "Property Management Company": management_company.strip(),
                "Property Owner Name": owner.strip()
            })
        else:
            print(f"Skipping unrecognized line: {line}")

    return structured_data

def save_json(data, output_path="output.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"JSON saved to {output_path}")

if __name__ == "__main__":
    pdf_path = "list.pdf"  # Change to your actual PDF file path
    lines = extract_text_from_pdf(pdf_path)
    file_name = "lines.json"

    # Open the file in write mode and save the text
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(lines, file, indent=4)

    print(f"Text successfully saved in {file_name}")
    # extracted_data = parse_lines_to_json(lines)

    # if extracted_data:
    #     print(json.dumps(extracted_data, indent=4))  # Print formatted JSON output
    #     save_json(extracted_data)
    # else:
    #     print("No structured data found.")

