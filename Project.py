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

import os
import subprocess

# GitHub Configuration
GITHUB_USERNAME = "TanishaSharma142"
GITHUB_REPO = "Krackhack"
GITHUB_TOKEN = "git_token"

# Specify the file to add (hardcoded for this test) 
file_to_add = Get_filename # Raw string for Windows path

# Commit message
commit_message = f"Added {Get_filename} file"


# Initialize Git
try:
    subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
    subprocess.run(["git", "remote", "remove", "origin"], check=False, capture_output=True, text=True)
    subprocess.run(["git", "remote", "add", "origin", f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"], check=True, capture_output=True, text=True)
    subprocess.run(["git", "pull", "origin", "main", "--rebase"], check=False, capture_output=True, text=True)

    # Add the HTML file
    subprocess.run(["git", "add", file_to_add], check=True, capture_output=True, text=True)

    # Commit the file
    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print("No changes to commit.")
        exit(0)

    # Push to GitHub
    subprocess.run(["git", "branch", "-M", "main"], check=True, capture_output=True, text=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True, capture_output=True, text=True)

    print(f"File index.html has been uploaded to GitHub repository {GITHUB_REPO}.")

except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e.stderr}")
except FileNotFoundError:
    print("Git command not found.  Make sure Git is installed and in your PATH.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
