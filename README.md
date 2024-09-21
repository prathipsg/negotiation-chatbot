# negotiation-chatbot

## Description
This project is a negotiation chatbot that simulates a negotiation process between a customer and a supplier. It leverages pre-trained AI models to handle conversational aspects and provides pricing logic to simulate real-world negotiation scenarios.

## Features
- Initiates negotiation for a product price.
- Allows users to propose offers, which the chatbot can accept, reject, or counteroffer.
- Implements basic pricing logic with discount offers.
- Integrates with Hugging Face models (e.g., GPT-2) for AI-generated responses.

## Requirements
- Python 3.x
- Flask
- Transformers library from Hugging Face

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
2.Install the required packages:
pip install -r requirements.txt
3.Add your Hugging Face API key in api_key.py

Usage
Run the Flask app:
python app.py

Use Postman or any API testing tool to interact with the chatbot:

Endpoint: http://127.0.0.1:5000/negotiate
Method: POST
Body (JSON):
{
  "offer": <your_offer>
}
