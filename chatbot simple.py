from openai import OpenAI  #Import open AI Module

#Provide the link of your API
client = OpenAI(api_key="Enter your Open AI API key")


completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[{"role": "user", "content": "Give me an essay on is AI dangerous?"}]) #Write the task you want it to perform
print(completion.choices[0].message.content)