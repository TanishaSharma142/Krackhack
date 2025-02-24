import requests

Get_prompt = input("Enter a prompt: ")

Get_filename = input("Enter a filename: ")
# API URL
url = "https://api-lr.agent.ai/v1/agent/fcz57vi7mq5e3ipl/webhook/eecc404b" 

# Headers
headers = {
    "Content-Type": "application/json"
}

# Data payload
data = {
    "user_input": Get_prompt 
}
# Send POST request
response = requests.post(url, headers=headers, json=data)

# Print response
print("Status Code:", response.status_code)
print("Response:", response.json())

response_data = response.json()

if response_data["status"] == 200:  # Check for status code 200
    html_code = response_data["response"]["code"]  # Access the code correctly
    print(html_code) 

    # Optionally, save the code to a file:
    with open(Get_filename, "w") as f: 
        f.write(html_code)
    print("HTML code saved to ", Get_filename)
else:
    print("Error:", response_data.get("message", "Unknown error")) 
