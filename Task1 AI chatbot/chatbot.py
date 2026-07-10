def get_response(user_input):
    text = user_input.lower().strip()

    if text in ("hi", "hello", "hey", "hii", "hola"):
        return "Hello there! How can I help you today?"

    elif text in ("your name","tell me about yourself","who are you"):
        return "I'm ChatBot, your friendly rule-based chatbot."
    
    elif text in ("good","fine","nice"):
        return "That's great to hear!, How can i help you?"
    
    elif "how are you" in text:
        return "I'm good, How about you?"

    elif "help" in text:
        return "I can chat about greetings, my name, how I'm doing, or you can type 'bye' to exit."

    elif "thank" in text:
        return "You're welcome! Happy to help."

    elif "weather" in text:
        return "I can't check live weather yet, but I hope it's nice outside!"

    elif "time" in text:
        return "Sorry, I don't have access to a live clock right now."

    elif "joke" in text:
        return "Why did the computer go to therapy? It had too many unresolved issues."
   
    elif text in ("bad","not okay","better"):
        return "I'm sorry to hear that."
    
    elif text in ("bye", "exit", "quit", "goodbye", "see you"):
        return "Goodbye!, Have a Great day"
    
    else:
        return "I'm not sure I understand that. Type 'help' to see what I can do."


def run_chatbot():
    print("ChatBot: Hello! I'm a rule-based AI chatbot.")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print("ChatBot: Please type something!")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("ChatBot: Goodbye! Have a great day. 👋")
            break
        else:
            print(f"ChatBot: {response}")


if __name__ == "__main__":
    run_chatbot()