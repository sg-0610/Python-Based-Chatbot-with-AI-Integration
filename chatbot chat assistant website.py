from openai import OpenAI

client = OpenAI(api_key="Enter your Open AI API key")
import gradio as gr

# Set your API key

# Define initial system message
messages = [
    {"role": "system", "content": "`You are a computer science professor who specializes in AI and Machine Learning"}]


# Define a function to interact with ChatGPT
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    # Get response from ChatGPT
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)

    # Extract ChatGPT's reply and add it to the conversation history
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply


# Set up Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="CS Professor",
    description="Ask questions related to Computer Science and AI."
)

# Launch the interface
demo.launch(share=True)