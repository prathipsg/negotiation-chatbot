from transformers import pipeline
from flask import Flask, request, jsonify
from negotiation_logic import negotiation_logic

# Initialize the Hugging Face model (you can choose different models)
generator = pipeline('text-generation', model='gpt2')

app = Flask(__name__)

# Function to get AI response from the Hugging Face model
def get_ai_response(prompt):
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Negotiation API!"

# Endpoint for negotiation
@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.get_json()
    user_offer = data.get('offer', 0)

    # Call negotiation logic to process the offer
    bot_logic_response = negotiation_logic(user_offer)
    
    # Add the chatbot logic response to the AI prompt
    prompt = f"A user made an offer of ${user_offer}. Respond like a professional negotiator. {bot_logic_response}"

    # Get AI-generated response
    ai_response = get_ai_response(prompt)

    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)
