from gtts import gTTS
from PyPDF2 import PdfReader
import tkinter as tk

root = tk.Tk()
root.config(padx=20,pady=20)

def convert_to_speech():
    reader = PdfReader(doc_path.get())
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    tts = gTTS(text)
    tts.save('AudioBook.mp3')
    root.destroy()

win_label = tk.Label(root, text='Enter path for a pdf file')
doc_path = tk.Entry(root, width=50)
submit_button = tk.Button(root, text="Submit", command=convert_to_speech)

win_label.grid(row=0)
doc_path.grid(row=1)
submit_button.grid(row=2)

root.mainloop()