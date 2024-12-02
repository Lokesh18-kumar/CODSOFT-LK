# Enhanced chatbot with more predefined rules
def chatbot():
    print("Chatbot: Hi! I'm here to chat with you. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase for easier matching

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a chatbot, but I'm doing well! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm called Chatbot. Nice to meet you!")
        elif "time" in user_input:
            from datetime import datetime
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}.")
        elif "date" in user_input:
            from datetime import datetime
            print(f"Chatbot: Today's date is {datetime.now().strftime('%Y-%m-%d')}.")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but you can try a weather app!")
        elif "joke" in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif "bye" in user_input:
            print("Chatbot: Bye! It was nice talking to you.")
            break
        elif "help" in user_input:
            print("Chatbot: Sure! You can ask me about time, date, my name, or even a joke!")
        elif "favorite" in user_input and "color" in user_input:
            print("Chatbot: I like all colors equally, but blue feels calming.")
        elif "what is" in user_input:
            print("Chatbot: That's a big question! Can you be more specific?")
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! I'm happy to help.")
        else:
            print("Chatbot: I'm not sure how to respond to that. Could you try asking in a different way?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
