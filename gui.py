import tkinter as tk
import metode
import bart
from tkinter.filedialog import askopenfilename
from tkinter import filedialog, Frame
import re
import os
import mindmap
from PIL import Image, ImageTk

def extract_last_sentence(text):
    # Pronalaženje poslednje rečenice posle tačke na kraju teksta
    last_sentence_match = re.search(r'\.\s*([^\.]+)\s*$', text)

    # Izdvajanje poslednje rečenice
    if last_sentence_match:
        last_sentence = last_sentence_match.group(1).strip()
        return last_sentence
    else:
        return None

def browse():
   f_path = askopenfilename(initialdir="/",
      title="Select File", filetypes=(("All Files","*.*"),("All Files","*.*")))
   file_explorer.configure(text="File Opened: "+f_path)
   eks = extract_last_sentence(f_path)
   
   if eks == "docx":
        metode.readWord(f_path)
        naziv_fajla = os.path.basename(f_path)
        naziv_fajla_bez_ext, extenzija = os.path.splitext(naziv_fajla)
        string = bart.sumiranje(naziv_fajla_bez_ext+".txt")
        
        tabela_okvir = tk.Frame(root, borderwidth=1, relief="solid", width=1550)
        tabela_okvir.pack(padx=10, pady=10)
        
        labela_zaglavlje1 = tk.Label(tabela_okvir, text="Vaša skripta:", font=("Arial", 16, "bold"))
        labela_zaglavlje1.grid(row=0, column=0)
        
        labela_zaglavlje2 = tk.Label(tabela_okvir, text="Vaša mapa uma:", font=("Arial", 16, "bold"))
        labela_zaglavlje2.grid(row=0, column=1)
        
        labela_red1_kolona1 = tk.Label(tabela_okvir, text=string, font=("Arial", 14), wraplength=750)
        labela_red1_kolona1.grid(row=1, column=0)

        slicka = mindmap.wordCloudImage(string)
        
        tk_image = ImageTk.PhotoImage(slicka)
        
        labela_red1_kolona2 = tk.Label(tabela_okvir, image=tk_image, wraplength=750,borderwidth=0, relief="flat")
        labela_red1_kolona2.config(image=tk_image)
        labela_red1_kolona2.image = tk_image
        labela_red1_kolona2.grid(row=1, column=1)

   
   elif eks == "pdf":
        metode.readPdf(f_path)
   elif eks == "txt":
        print(3)
   else:
        print("Nepoznata ekstenzija")

   

root = tk.Tk()
root.title("MindMaze")
# Uklonite okvir prozora
root.overrideredirect(False)

# Maksimizirajte prozor
root.state('zoom')






root.config(background="white")

file_explorer = tk.Label(root, text="Explore files",
   font=("Verdana", 14, "bold"),
   width=200,
   height=4, fg="white", bg="gray")

button=tk.Button(root, text="Browse Folder", font =("Roboto", 14),
   command=browse)
file_explorer.pack()
button.pack(pady=10)

root.mainloop()