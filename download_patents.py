import argparse
import requests
import json

def download_patents(filing_date_from, filing_date_to):
    url = "https://developer.uspto.gov/ibd-api/v1/application/publications"
    params = {
        "filingDateFromDate": filing_date_from,
        "filingDateToDate": filing_date_to
    }
    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def pretty_print(obj, indent=0):
    """Recursively prints a summary of the JSON object with controlled depth and truncation."""
    INDENTATION = "    "
    TRUNCATE_AFTER = 100  # Number of characters after which to truncate string values

    if isinstance(obj, dict):
        for key, value in obj.items():
            print(f"{INDENTATION * indent}{key}: ", end="")
            if isinstance(value, (dict, list)):
                print()
                pretty_print(value, indent + 1)
            elif isinstance(value, str) and len(value) > TRUNCATE_AFTER:
                print(f"{value[:TRUNCATE_AFTER]} ... ... ...")
            else:
                print(value)
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            print(f"{INDENTATION * indent}[{index}]: ", end="")
            if isinstance(item, (dict, list)):
                print()
                pretty_print(item, indent + 1)
            elif isinstance(item, str) and len(item) > TRUNCATE_AFTER:
                print(f"{item[:TRUNCATE_AFTER]}... ... ...")
            else:
                print(item)
    else:
        print(f"{INDENTATION * indent}{obj}")

def post_process(json_data):
    pretty_print(json_data)

def main():
    parser = argparse.ArgumentParser(description="Download patents data from the USPTO")
    parser.add_argument('--from-date', required=True, help='Filing date from in YYYY-MM-DD format')
    parser.add_argument('--to-date', required=True, help='Filing date to in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    json_data = download_patents(args.from_date, args.to_date)
    if json_data:
        post_process(json_data)
    else:
        print("Failed to download patents data. Please check your parameters and try again.")

if __name__ == "__main__":
    main()
