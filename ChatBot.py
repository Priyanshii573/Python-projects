import tkinter as tk
from tkinter import ttk, scrolledtext
from nltk.chat.util import Chat, reflections
import random

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        self.chatbot = Chat(self.get_chatbot_responses(), reflections)

        self.message_history = scrolledtext.ScrolledText(root, wrap="word", state="disabled", height=20, width=50)
        self.message_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.message_entry = ttk.Entry(root, width=40)
        self.message_entry.grid(row=1, column=0, padx=10, pady=5)

        self.send_button = ttk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=5)

        self.display_message("Chatbot: Hi there! I'm Chatbot. How can I assist you today?")

    def get_chatbot_responses(self):
        return [
            (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
            (r"how are you?", ["I'm doing well, thank you!", "I'm good, thanks for asking."]),
            (r"what is your name?", ["You can call me Chatbot.", "I'm just a humble chatbot."]),
            (r"what can you do?", ["I can answer your questions and engage in a conversation."]),
            (r"what's your name?", ["My name is Chatbot.", "I'm Chatbot."]),
            (r"my name is (.*)", ["Nice to meet you, %1!"]),
            (r"what time is it?", ["It's time to chat!"]),
            (r"how old are you?", ["I'm ageless, just like the internet."]),
            (r"where are you from?", ["I exist in the digital realm."]),
            (r"thanks|thank you", ["You're welcome!", "No problem.", "Anytime!"]),
            (r"bye|goodbye", ["Goodbye!", "Bye!", "Take care!"]),
        ]

    def send_message(self):
        user_input = self.message_entry.get()
        self.display_message("You: " + user_input)

        response = self.chatbot.respond(user_input)
        self.display_message("Chatbot: " + response)

        self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.message_history.configure(state="normal")
        self.message_history.insert(tk.END, message + "\n")
        self.message_history.configure(state="disabled")
        self.message_history.see(tk.END)

def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
