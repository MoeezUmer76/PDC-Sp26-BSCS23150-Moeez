import requests

BASE_URL = "http://127.0.0.1:8000"

# Step 1: Create a document
create_response = requests.post(
    f"{BASE_URL}/documents",
    json={
        "content": "Initial Content"
    }
)

document = create_response.json()

doc_id = document["id"]
initial_version = document["version"]

print("\nDocument Created:")
print(document)

# Simulate two users reading same version
user_a_version = initial_version
user_b_version = initial_version

# Step 2: User A updates document
user_a_response = requests.put(
    f"{BASE_URL}/documents/{doc_id}",
    json={
        "content": "Update from User A",
        "version": user_a_version
    }
)

print("\nUser A Update:")
print("Status Code:", user_a_response.status_code)
print(user_a_response.json())

# Step 3: User B tries stale update
user_b_response = requests.put(
    f"{BASE_URL}/documents/{doc_id}",
    json={
        "content": "Update from User B",
        "version": user_b_version
    }
)

print("\nUser B Update:")
print("Status Code:", user_b_response.status_code)
print(user_b_response.json())