#Data collectio from APIs
import requests
import pandas as pd

# Step 1: Connect to API
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    print(f"Status Code: {response.status_code}")  # 200 = success

    if response.status_code != 200:
        raise requests.exceptions.ConnectionError("Non-200 status")

    # Step 2: Parse JSON response
    data = response.json()

    # Step 3: Convert to DataFrame
    df = pd.DataFrame(data)

    # Display key columns only (address/company are nested dicts)
    print(df[["id", "name", "username", "email", "phone", "website"]].head())

except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    print("Network unavailable. Loading sample data instead.\n")

    # Fallback sample data (same structure as the API response)
    sample_data = [
        {"id": 1, "name": "Leanne Graham", "username": "Bret",
         "email": "sincere@april.biz", "phone": "1-770-736-8031", "website": "hildegard.org"},
        {"id": 2, "name": "Ervin Howell", "username": "Antonette",
         "email": "shanna@melissa.tv", "phone": "010-692-6593", "website": "anastasia.net"},
        {"id": 3, "name": "Clementine Bauch", "username": "Samantha",
         "email": "nathan@yesenia.net", "phone": "1-463-123-4447", "website": "ramiro.info"},
    ]
    df = pd.DataFrame(sample_data)
    print(df.head())

except Exception as e:
    print(f"An error occurred: {e}")