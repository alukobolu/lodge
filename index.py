import requests
import json

def categorize(key,address, user_profile):
    url = "https://api.wetrocloud.com/v1/category/"
    headers = {
        "Authorization": f"Token {key}",
    }
    jsonres ={
        "isValid":"boolean",
        "likelihood":"%",
        "reasonExplanation":"string"
    }
    
    resource = generate_rules(key,address)
    # resource = f"Must have a bathroom, Must have a kitchen, Must have a bedroom, Must have a living room"
    
    data = {
        "resource": f"Here are the rules for the airbnb listing: {resource}",
        "type": "text",
        "json_schema": jsonres,
        "json_schema_rules": f"Validate based on the details from you get inside the airbnb url, {user_profile}"
    }

    response = requests.post(url, headers=headers, json=data)
    print("Categorize Response:")
    print(response.json())
    return response.json()['response']

def scrape(key,website):
    url = "https://api.wetrocloud.com/v1/scrape/"
    headers = {
        "Authorization": f"Token {key}",
    }
    jsonres = {
        "listing_name":"string",
        "listing_price":"string",
        "full_listing_description":"string",
        "listing_location":"string",
        "number_of_beds":"number",
        "number_of_bathrooms":"number",
        "number_of_rooms":"number",
        "number_of_guests":"number",
        "offers":"string",
        "amenities":"string",
        "host_name":"string",
        "host_description":"string",
        "host_rating":"number",
        "neighborhood_highlights":"string",
        "house_rules":"string",
        "safety_details":"string",
        "cancellation_policy":"string",
        "check_in_time":"string",
        "check_out_time":"string",
        "cancellation_policy":"string"
    }
    jsonres2 = {
        "listing_name":"string",
        "full_listing_description":"string",
    }
    data = {
        "website": website,
        "json_schema": json.dumps(jsonres2)
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()

def generate_rules(key,address):
    url = "https://api.wetrocloud.com/v1/pure-query/"
    headers = {
        "Authorization": f"Token {key}",
    }

    data = {
        # "request_query": f"Based on this location: {address}; Create a simple set of rules to validate an airbnb short term rental on whether the user is in violation of any local laws or regulations",
        # "json_schema_rules": ["Make sure its for a short term rentals", "Give a simple check list that's concise and straight to the point","Take note of the address to determine the local laws and regulations to use", "DO NOT include any other text or information, just the check list"]
        "request_query": f"Based on this location: {address}; Bring out rules to validate airbnb listing amenities Follow this format: ONLY 3 WORDS AND 'MUST HAVE' MUST BE IN THE RULE, EG; Must have bathroom",
        "json_schema_rules": [
            "Make SIMPLE AND SHORT RULES NOT MORE THAN 5", 
            "DONT INCLUDE ANYTHING ABOUT ADDRESS, PHOTOS OR PRICES",
            "Take note of the address to determine the actual basic amenities it must have to be a valid legal", 
            "DO NOT include any other text or information, just the check list", 
            "Create rules based on the information provided in an airbnb listing",
            "OMIT ANY RULE THAT CAN NOT BE VERIFIED WITH THE INFORMATION PROVIDED IN A PUBLIC AIRBNB LISTING !!!"
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response)
    print("Generate Rules Response:")
    print(response.json())
    return response.json()['response']

