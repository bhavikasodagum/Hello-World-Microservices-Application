import requests

# Define the endpoints
hello_url = "http://localhost:8080/hello"
world_url = "http://localhost:8083/world"

try:
    # Make requests to the services
    hello_response = requests.get(hello_url)
    world_response = requests.get(world_url)

    # Check if both requests were successful
    if hello_response.status_code == 200 and world_response.status_code == 200:
        # Combine and print the responses
        combined_message = f"{hello_response.text} {world_response.text}"
        print(combined_message)
    else:
        print("Failed to retrieve responses from one or both services.")
        print(f"Hello Service Status Code: {hello_response.status_code}")
        print(f"World Service Status Code: {world_response.status_code}")

except requests.RequestException as e:
    print(f"An error occurred: {e}")
