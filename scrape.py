import firecrawl
import os
import requests
import json

def extract_pdf_details(pdf_path):
    """
    Extracts details from a PDF using firecrawl.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text or details from the PDF.
    """
    # if not os.path.exists(pdf_path):
        # raise FileNotFoundError(f"The file '{pdf_path}' does not exist.")
    
    # Initialize firecrawl's PDF reader
    firecrawl.init()  # Initialize firecrawl (if needed)
    pdf_extractor = firecrawl.PDFReader()

    try:
        # Extract text from the PDF
        extracted_text = pdf_extractor.read(pdf_path)
        print(f"Extracted text from '{pdf_path}':\n")
        print(extracted_text)
        return extracted_text
    except Exception as e:
        print(f"An error occurred while extracting details from the PDF: {e}")
        return None

def scrape():
    key = "fc-3e2a097b0e1d4d5d906e51a9ef59e182"
    url = "https://api.firecrawl.dev/v1/scrape"
    headers = {
        "Authorization": f"Bearer {key}",
    }

    json_schema = {
        "license_number": "<string>",
        "property_address": "<string>",
        "expiration_date": "<string>",
        "property_management_company": "<string>",
        "property_owner_name": "<string>",
    }

    json_schema = json.dumps(json_schema)

    data = {
        "url": "https://orderly-bucket.s3.amazonaws.com/billboard_images/b6d6f14d-0c84-497d-85b8-d42ff275c134/approved_vacation_rental_list-pages-3.pdf",
        "formats": ["extract"],
        'extract': {
            'systemPrompt': 'Always return json',
            'prompt': json_schema,
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()


import pdfplumber
import json

def extract_table_from_pdf(pdf_path):
    extracted_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_table()
            if tables:
                headers = tables[0]  # Assume first row is the header
                for row in tables[1:]:  # Skip the header row
                    data_dict = dict(zip(headers, row))
                    extracted_data.append(data_dict)

    return extracted_data

def save_json(data, output_path="output.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"JSON saved to {output_path}")

if __name__ == "__main__":
    pdf_path = "list.pdf"  # Change to your actual PDF file path
    extracted_data = extract_table_from_pdf(pdf_path)
    print(json.dumps(extracted_data, indent=4))  # Print formatted JSON output
    save_json(extracted_data)

# if __name__ == "__main__":
#     # Path to your PDF file
#     pdf_file_path = "https://orderly-bucket.s3.amazonaws.com/billboard_images/b6d6f14d-0c84-497d-85b8-d42ff275c134/approved_vacation_rental_list-pages-3.pdf"  # Replace with the path to your PDF file

#     # Call the function to extract PDF details
#     extracted_details = extract_pdf_details(pdf_file_path)

#     # scrape()

#     # If needed, you can process the extracted details further here
