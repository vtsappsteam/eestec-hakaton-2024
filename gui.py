import tkinter as tk
import metode
import bart
from tkinter.filedialog import askopenfilename
from tkinter import filedialog, Frame
# from tk import Frame
import re
import os

def extract_last_sentence(text):
    # Pronalaženje poslednje rečenice posle tačke na kraju teksta
    last_sentence_match = re.search(r'\.\s*([^\.]+)\s*$', text)

    # Izdvajanje poslednje rečenice
    if last_sentence_match:
        last_sentence = last_sentence_match.group(1).strip()
        return last_sentence
    else:
        return None

def otvori_file_explorer():
    putanja_do_fajla = filedialog.asksaveasfilename(defaultextension=".txt")
    if putanja_do_fajla:
        print("Izabrana putanja:", putanja_do_fajla)
        return putanja_do_fajla

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
        putanja = otvori_file_explorer()
        
        # Kreirajte okvir sa scrollom
        # scroll_okvir = Frame(root)
        # scroll_y = Scrollbar(scroll_okvir, orient=tk.VERTICAL)
        # scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        tabela_okvir = tk.Frame(root, borderwidth=1, relief="solid", width=1550)
        tabela_okvir.pack(padx=10, pady=10)
        
        labela_zaglavlje1 = tk.Label(tabela_okvir, text="Vaša skripta:", font=("Arial", 16, "bold"))
        labela_zaglavlje1.grid(row=0, column=0)
        
        labela_zaglavlje2 = tk.Label(tabela_okvir, text="Vaša mapa uma:", font=("Arial", 16, "bold"))
        labela_zaglavlje2.grid(row=0, column=1)
        
        labela_red1_kolona1 = tk.Label(tabela_okvir, text=string, font=("Arial", 14), wraplength=750)
        labela_red1_kolona1.grid(row=1, column=0)

        labela_red1_kolona2 = tk.Label(tabela_okvir, text=string, wraplength=750)
        labela_red1_kolona2.grid(row=1, column=1)

        
        # Kreirajte ladelu sa tekstom
        # labela = tk.Label(root, text = string, font=("Verdana", 18, "bold"), wraplength=1550 )

        # Pakirajte ladelu u prozor (postavlja se na vrh)  /// height=5
        # labela.pack()

   
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