import json
import requests

def search_json(file_path, query:str,page=1, page_size=5):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load JSON file assuming it's a list of strings
    
    query_words = query.lower().split()
    results = [line for line in data if all(word in line.lower() for word in query_words)]

    total_results = len(results)

    if not results:
        return {"error": "No results found"}
    if total_results > 1:
        return {"error": "No results found"}

    
    total_pages = (total_results + page_size - 1) // page_size  # Calculate total pages
    
    if page < 1 or page > total_pages:
        return {"error": "Invalid pagination", "total_pages": total_pages}
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_results = results[start_index:end_index]
    
    has_next_page = page < total_pages
    
    return {
        "results": paginated_results,
        "page": page,
        "total_pages": total_pages,
        "has_next_page": has_next_page
    }
    


# file_path = 'lines.json'  
# query = "100 STARVATION"
# matched_lines = search_json(file_path, query)
# print(matched_lines)

def search_pdf(key,type,query,page):
    url = "https://api.wetrocloud.com/v1/pure-query/"
    headers = {
        "Authorization": f"Token {key}",
    }
    file_path = 'lines.json' 
    matched_lines = search_json(file_path, query,page)
    print(matched_lines)

    data = {
        "request_query": f"A User is searching for this ({type}:{query}); Here is the result {json.dumps(matched_lines)}, Response to the User using natural language",
        "json_schema_rules": [
            "NOTE THAT Each line represent a record of a listings, License Number, Property Address, Expiration Date, Property Management Company, Property Owner Name IN THAT EXACT ORDER", 
            "IF RESULT IS EMPTY, LET THE USER KNOW THE SEARCH WAS INVALID",
            "IF RESULT IS AN ERROR, LET THE USER KNOW THE ERROR",
            "IF RESULT HAS A NEXT PAGE, LET THE USER KNOW THAT INFORMATION TOO",
            # "Take note of the address to determine the actual basic amenities it must have to be a valid legal", 
            # "DO NOT include any other text or information, just the check list", 
            # "Create rules based on the information provided in an airbnb listing",
            # "OMIT ANY RULE THAT CAN NOT BE VERIFIED WITH THE INFORMATION PROVIDED IN A PUBLIC AIRBNB LISTING !!!"
        ]
    }
    print(data)
    response = requests.post(url, headers=headers, json=data)
    print(response)
    print("Generate Rules Response:")
    print(response.json())
    return response.json()['response']
