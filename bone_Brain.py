#This is the Main File everything is opraits frome here

#importing lisning Function
import bone_Ear
from bone_Ear import voice_to_text as Intake

#import Speaking Function
from bone_Mouth import speak

#importing filter module for removing noise from the output
import re

#this is filter for speaking only the text from the output and removing any unwanted noise
def clean_reply(text):
    # Remove all characters except letters, numbers, and spaces
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)

#importing os and groq for chatbot using API  
import os
os.environ['GROQ_API_KEY'] = "Enter Your API Key Here" # Set your API key here
from groq import Groq

#import to save and load history 
import json

#this part is tosave and load the history of the conversation from a file
# Save conversation history to a file
def save_history(filename="conversation_history.json"):
    with open(filename, "w") as file:
        json.dump(conversation_history, file)

# Load conversation history from a file
def load_history(filename="conversation_history.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [{"role": "system", "content": "You are Bone, a helpful assistant."}]

#this mantain the length of the history of the conversation
MAX_HISTORY_LENGTH = 10  # Keep only the last 10 exchanges

def truncate_history(history):
    if len(history) > MAX_HISTORY_LENGTH:
        return history[-MAX_HISTORY_LENGTH:]
    return history


# this part is of chatbot where we give a text input and get a text out put
client = Groq()

# Load conversation history from file
conversation_history = load_history()

# Before making an API call, truncate the history
conversation_history = truncate_history(conversation_history)

def chatbot(prompt):

    # Add user input to conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Make API call to get the assistant's reply
    # Note: Adjust the API call according to your specific requirements
    chat_completion = client.chat.completions.create(
      messages=conversation_history,
      model="gemma2-9b-it",
      stream=False,
    )
    # Extract assistant's reply
    assistant_reply = chat_completion.choices[0].message.content

    # Add assistant's reply to conversation history
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    # Save updated history to file
    save_history()


    return assistant_reply


#Test for Chat bot Functioning
while __name__ == "__main__":
    print("Speak now:")
    ask = Intake()
    print(f"You said: {ask}")
    reply = chatbot(ask)
    final_reply = clean_reply(reply)
    print(f"Chatbot reply: {final_reply}")

    #this will exit or end the conversation if the user say bye or exit
    if "bye" in final_reply.lower() or "exit" in ask.lower():
        speak(final_reply)
        print("closing the application")
        exit(0)
    else:
        speak(final_reply)



