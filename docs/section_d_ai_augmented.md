# Section D — AI-Augmented Learning

## Step 1 — Exact Prompt Used

Write a Python 3 program for a Food Delivery platform that fetches the first 5 records from
https://jsonplaceholder.typicode.com/posts?_limit=5 and treats them as mock restaurants,
printing each record's id and title. Apply a tiered commission to a hardcoded list of 6 order
amounts using map() and a lambda: 10% for amounts up to Rs 200, 15% for Rs 201–Rs 500, and
20% above Rs 500. Print each original amount alongside its calculated commission. Handle any
API status code other than 200 by printing a descriptive error message and stopping execution
without an unhandled exception. Save the 5 fetched records to data/processed/records.json using
json.dump() inside a with open() context manager, with indent=2.

## AI's Original Code

```python
import json
import requests

url = "https://jsonplaceholder.typicode.com/posts?_limit=5"

response = requests.get(url)
data = response.json()

amounts = [150, 200, 250, 400, 600, 1000]

def commission(amount):
    if amount <= 200:
        return amount * 0.10
    elif amount <= 500:
        return amount * 0.15
    return amount * 0.20

fees = list(map(lambda x: commission(x), amounts))

for amount, fee in zip(amounts, fees):
    print(amount, fee)

with open("records.json", "w") as file:
    json.dump(data, file)
```

## Corrected Version

```python
import json
from pathlib import Path

import requests

url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
output_file = Path("data/processed/records.json")

try:
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(
            f"API request failed with HTTP {response.status_code}. "
            "Stopping without crashing."
        )
    else:
        data = response.json()

        print("MOCK RESTAURANTS")
        for record in data:
            print(f"{record['id']}: {record['title']}")

        amounts = [150, 200, 250, 400, 600, 1000]

        def commission(amount):
            if amount <= 200:
                return amount * 0.10
            elif amount <= 500:
                return amount * 0.15
            return amount * 0.20

        fees = list(map(lambda x: commission(x), amounts))

        print("\nCOMMISSION RESULTS")
        for amount, fee in zip(amounts, fees):
            print(f"Rs {amount:.2f} -> Rs {fee:.2f}")

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        print(f"Saved records to {output_file}")

except requests.RequestException as exc:
    print(f"Network error: {exc}")
except (ValueError, KeyError) as exc:
    print(f"Invalid API response: {exc}")
```

## Step 2 — Test & Debug Note

The AI version called `.json()` immediately without checking `response.status_code`, so an API
failure could cause the program to process an error response as if it were valid data. It also
saved the output to `records.json` in the current directory instead of the required
`data/processed/records.json`, and it omitted `indent=2`. I fixed the status-code check, added
timeout/error handling, created the required output directory, used the required output path,
and added `indent=2` so the JSON is readable.
