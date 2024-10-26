from openai import OpenAI

client = OpenAI(api_key="Enter your Open AI API key")


# Set up the system message
messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type 'quit' to exit.")

while True:
    # Get user input
    user_message = input()
    if user_message.lower() == "quit":
        print("Goodbye!")
        break

    # Append user message to conversation
    messages.append({"role": "user", "content": user_message})

    # Get response from the assistant
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)

    # Extract and print the assistant's reply
    assistant_reply = response.choices[0].message.content
    print("\n" + assistant_reply + "\n")

    # Append assistant's reply to conversation
    messages.append({"role": "assistant", "content": assistant_reply})