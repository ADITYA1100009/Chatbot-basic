# Simple Python Chatbot

def respond(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "resume" in user_input:
        return "Resume banane main madad chahiye? Apni details bataiye."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, mujhe samajh nahi aaya. Aap kuch aur puchhna chahenge?"
print("Chatbot Start! (Type 'bye' to exit)")

while True:
    inp = input("You: ")
    if "bye" in inp.lower():
        print("Bot:", respond(inp))
        break
    print("Bot:", respond(inp))
