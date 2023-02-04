#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

import tkinter as tk
import openai
print('Copyright (C) 2023  Mathys Penson')
root = tk.Tk()
root.configure(bg='gray')
root.attributes("-alpha", 0.9)
root.overrideredirect(True)
root.config(highlightthickness=0)
root.config(borderwidth=0)


input_text = ""


api_key = open('api.key', 'r').read()
openai.api_key = api_key

# get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the position of the window
width = int(screen_width * 0.4)
height = int(screen_height * 0.1)
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 3) - (height / 2))

# set the dimensions and position of the window
root.geometry(f"{width}x{height}+{x}+{y}")

entry = tk.Entry(root, font=("Helvetica", 16), bg='gray', highlightthickness=0, fg='black')
entry.place(relx=0, rely=0, relwidth=1, relheight=1)

# Set the placeholder text
placeholder = "Type a text to ask AI"
entry.insert(0, placeholder)
entry.config(fg='gray')

def getAnswer():
    input_text = entry.get()
    entry.destroy()
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        temperature=.4,
        max_tokens=1024
    )
    response = response['choices'][0]['text']
    print(response)

    show_popup(response)
def show_popup(text):
    popup = tk.Toplevel()
    popup.title("AI Answer")
    label = tk.Label(popup, text=text)
    label.pack()
def on_entry_click(event):
    if entry.get() == placeholder:
        entry.delete(0, 'end')
        entry.config(fg='black')
        

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='gray')
def on_ESC_press(event):
    if event.keysym == 'Escape':
        root.destroy()
        exit(0)
def on_ENTER_press(event):
    root.withdraw()
    getAnswer()


entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
root.bind('<Key>', on_ESC_press)
root.bind('<Return>', on_ENTER_press)
root.mainloop()
