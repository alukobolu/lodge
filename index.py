import requests
import json

def categorize(key,resource, user_profile):
    url = "https://api.wetrocloud.com/v1/category/"
    headers = {
        "Authorization": f"Token {key}",
    }
    jsonres ={
        "isValid":"boolean",
        "likelihood":"%",
        "reasonExplanation":"string"
    }
    data = {
        "resource": f"Here are the rules and requirements for the user profile: {resource}",
        "type": "text",
        "json_schema": jsonres,
        "json_schema_rules": f"Validate the user profile {user_profile}"
    }

    response = requests.post(url, headers=headers, json=data)
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


def generate_rules(key,resource, user_profile):
    url = "https://api.wetrocloud.com/v1/category/"
    headers = {
        "Authorization": f"Token {key}",
    }
    jsonres ={
        "isValid":"boolean",
        "likelihood":"%",
        "reasonExplanation":"string"
    }
    data = {
        "resource": f"Here are the rules and requirements for the user profile: {resource}",
        "type": "text",
        "json_schema": jsonres,
        "json_schema_rules": f"Validate the user profile {user_profile}"
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()['response']


    main()