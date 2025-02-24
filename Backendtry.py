from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API URL
url = "https://api-lr.agent.ai/v1/agent/fcz57vi7mq5e3ipl/webhook/eecc404b"

# Headers
headers = {
    "Content-Type": "application/json"
}

@app.route('/generate_code', methods=['POST'])
def generate_code():
    try:
        # Get user input from the request
        user_input = request.json.get('user_input')

        # If no user input is provided, return an error
        if not user_input:
            return jsonify({'error': 'No user_input provided', 'status': 'error'}), 400

        # Data payload
        data = {
            "user_input": user_input
        }

        # Send POST request to the AI agent
        response = requests.post(url, headers=headers, json=data)

        # Check status code
        if response.status_code == 200:
            response_data = response.json()

            # Check if the response contains the code
            if "response" in response_data and "code" in response_data["response"]:
                html_code = response_data["response"]["code"]
                return jsonify({'code': html_code, 'status': 'success'})
            else:
                return jsonify({'error': 'Unexpected response format from AI agent', 'status': 'error'}), 500
        else:
            return jsonify({'error': f'AI agent returned status code: {response.status_code}', 'status': 'error'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

if __name__ == '__main__':
    app.run(debug=True) 