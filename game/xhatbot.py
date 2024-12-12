import tkinter as tk
from tkinter import scrolledtext
import requests

class Chatbot:
	def __init__(self, master):
		self.master = master
		self.master.title("Chatbot")
		
		self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
		self.chat_area.pack(padx=10, pady=10)
		self.chat_area.config(state=tk.DISABLED)
		
		self.entry = tk.Entry(master, width=50)
		self.entry.pack(padx=10, pady=10)
		self.entry.bind("<Return>", self.send_message)
		
		self.send_button = tk.Button(master, text="Send", command=self.send_message)
		self.send_button.pack(padx=10, pady=10)
		
	def send_message(self, event=None):
		user_message = self.entry.get()
		if user_message:
			self.chat_area.config(state=tk.NORMAL)
			self.chat_area.insert(tk.END, "You: " + user_message + "\n")
			self.chat_area.config(state=tk.DISABLED)
			self.entry.delete(0, tk.END)
			self.get_response(user_message)
	
	def get_response(self, user_message):
		api_key = 'AIzaSyDFPkx9WW5u4-991RMz9Lt5a_RZpy5A9Ig'
		url = 'https://api.gemini.com/v1/chat'  # Update with the correct Gemini API endpoint
		headers = {
			'Authorization': f'Bearer {api_key}',
			'Content-Type': 'application/json'
		}
		data = {
			'message': user_message
		}
		response = requests.post(url, headers=headers, json=data)
		if response.status_code == 200:
			bot_message = response.json().get('response')
			self.chat_area.config(state=tk.NORMAL)
			self.chat_area.insert(tk.END, "Bot: " + bot_message + "\n")
			self.chat_area.config(state=tk.DISABLED)
		else:
			self.chat_area.config(state=tk.NORMAL)
			self.chat_area.insert(tk.END, "Bot: Sorry, I couldn't process your request.\n")
			self.chat_area.config(state=tk.DISABLED)

if __name__ == "__main__":
	root = tk.Tk()
	chatbot = Chatbot(root)
	root.mainloop()