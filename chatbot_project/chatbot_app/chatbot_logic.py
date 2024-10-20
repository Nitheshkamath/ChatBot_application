import spacy
import random

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Extract intent and relevant information
def extract_intent_and_entity(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)

    # Check for intents based on user input
    if "weather" in user_input:
        location = [ent.text for ent in doc.ents if ent.label_ == "GPE"]  # GPE stands for geographical locations
        return "weather", location
    elif "reset password" in user_input or "services" in user_input:
        return "faq", None
    elif "hi" in user_input or "hello" in user_input or "your name" in user_input:
        return "greeting", None
    elif "how are you" in user_input or "what's up" in user_input:
        return "chit-chat", None
    else:
        return "fallback", None  # For unrecognized input

# Generate chatbot response based on detected intent
def generate_response(intent, entity=None):
    responses = {
        "weather": [
            "The weather in {location} is sunny with 25°C.",
            "Currently, it's 25°C and sunny in {location}.",
            "Expect sunny weather and 25°C in {location} today.",
            "In {location}, you can enjoy a sunny day at 25°C.",
            "It's a beautiful day in {location} with temperatures around 25°C."
        ],
        "faq": [
            "To reset your password, go to the account settings page.",
            "You can reset your password by following the instructions in the account settings.",
            "Need to reset your password? Just head to your account settings.",
            "For password recovery, visit your account settings page.",
            "To change your password, simply navigate to account settings."
        ],
        "greeting": [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Greetings! How may I be of service?",
            "Hello! What do you need assistance with today?",
            "Hi! I'm here to help, how can I assist you?"
        ],
        "chit-chat": [
            "I'm just a bot, but I'm doing great! How about you?",
            "I'm here and ready to chat! How are you doing?",
            "Doing well! What's on your mind?",
            "I’m just a bot, but I’m happy to chat with you! How are you?",
            "I'm functioning optimally! What about you?"
        ],
        "fallback": [
            "I'm sorry, I didn't quite catch that. Can you please rephrase?",
            "Could you clarify that? I didn't understand your request.",
            "I’m not sure I follow. Can you say that differently?",
            "Sorry, I didn't quite get that. Could you elaborate?",
            "Hmm, that seems unclear to me. Can you rephrase?"
        ]
    }

    # Choose a random response from the list
    if intent in responses:
        if intent == "weather" and entity:
            return random.choice(responses[intent]).format(location=entity[0])
        return random.choice(responses[intent])
    return "I'm not able to assist with that right now."
