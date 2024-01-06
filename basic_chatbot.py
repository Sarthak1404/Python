# Import the random module
import random

# Define a dictionary of responses for different intents
responses = {
  "greet": ["Hello, I am a chatbot.", "Hi, nice to meet you.", "Greetings, how are you?"],
  "name": ["My name is Chatbot.", "You can call me Chatbot.", "I go by the name Chatbot."],
  "age": ["I am as old as you want me to be.", "Age is just a number for me.", "I don't have a specific age."],
  "bye": ["Goodbye, have a nice day.", "See you later, take care.", "Bye, hope to talk to you again."],
  "weather": ["The weather today is sunny and warm.", "It's cloudy and rainy right now.", "There is a chance of snow later."],
  "joke": ["What do you call a fish that wears a bowtie? Sofishticated.", "How do you make a tissue dance? You put a little boogie in it.", "Why did the chicken go to the seance? To get to the other side."],
  "fact": ["Did you know that the longest word in English is pneumonoultramicroscopicsilicovolcanoconiosis?", "Did you know that the unicorn is the national animal of Scotland?", "Did you know that octopuses have three hearts?"],
  "feedback": ["Thank you for your feedback. We appreciate your opinion.", "We are sorry to hear that you are not satisfied. Please let us know how we can improve.", "We are glad that you enjoyed our service. Please share your experience with others."],
  "hobby": ["That's a nice hobby. How long have you been doing it?", "That sounds interesting. What do you like most about it?", "That's cool. I wish I could do that too."]
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
  elif "weather" in message or "how is" in message or "what's" in message:
    return "weather"
  elif "joke" in message or "tell me" in message or "make me laugh" in message:
    return "joke"
  elif "fact" in message or "tell me something" in message or "did you know" in message:
    return "fact"
  elif "feedback" in message or "I think" in message or "I feel" in message:
    return "feedback"
  elif "hobby" in message or "I like" in message or "I enjoy" in message:
    return "hobby"
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
