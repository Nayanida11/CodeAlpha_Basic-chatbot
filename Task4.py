def chatbot():
    print("Chatbot")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")
        elif user == "how are you":
            print("Chatot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Chatbot: I am Chatbot.")
        elif user == "who created you":
            print("Chatbot: I was created using Python.")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:I dont understand.")

chatbot()
