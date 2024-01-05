# Import the random module
import random

# Define a dictionary of responses for different intents
responses = {
  "greet": ["Hello, I am a chatbot.", "Hi, nice to meet you.", "Greetings, how are you?"],
  "name": ["My name is Chatbot.", "You can call me Chatbot.", "I go by the name Chatbot."],
  "age": ["I am as old as you want me to be.", "Age is just a number for me.", "I don't have a specific age."],
  "bye": ["Goodbye, have a nice day.", "See you later, take care.", "Bye, hope to talk to you again."]
}

# Define a function to get the intent of the user's message
def get_intent(message):
  # Convert the message to lowercase
  message = message.lower()
  # Check if the message contains any of the keywords for each intent
  if "hello" in message or "hi" in message or "hey" in message:
    return "greet"
  elif "name" in message or "who" in message:
    return "name"
  elif "age" in message or "how old" in message:
    return "age"
  elif "bye" in message or "see you" in message or "quit" in message:
    return "bye"
  else:
    return "unknown"

# Define a function to get a response for the user's message
def get_response(message):
  # Get the intent of the message
  intent = get_intent(message)
  # If the intent is known, choose a random response from the dictionary
  if intent in responses:
    return random.choice(responses[intent])
  # If the intent is unknown, say that the chatbot does not understand
  else:
    return "Sorry, I don't understand what you mean."

# Start the chatbot conversation
print("Welcome to the chatbot. Type 'quit' to exit.")
# Loop until the user types 'quit'
while True:
  # Get the user's message
  message = input("You: ")
  # If the user types 'quit', break the loop
  if message == "quit":
    break
  # Otherwise, get a response and print it
  response = get_response(message)
  print("Chatbot:", response)
