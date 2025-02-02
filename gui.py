import tkinter as tk
import metode
import bart
from tkinter.filedialog import askopenfilename
import re
import os
import mindmap
from PIL import ImageTk
c4 = 'BLACK'
c5 = '#ffffff'
test = 0
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
   global test
   f_path = askopenfilename(initialdir="/",
      title="Select File", filetypes=(("All Files","*.*"),("All Files","*.*")))
   
   eks = extract_last_sentence(f_path)
   
   if eks == "docx":
        metode.readWord(f_path)
        naziv_fajla_bez_ext, _ = os.path.splitext(f_path)
        string = bart.sumiranje(naziv_fajla_bez_ext+".txt",test)
        
        tabela_okvir = tk.Frame(root, borderwidth=0, relief="solid", width=1550, background=c5)
        tabela_okvir.pack(padx=10, pady=10)
        
        labela_zaglavlje1 = tk.Label(tabela_okvir, text="Your script:", font=("Arial", 16, "bold"), background=c5)
        labela_zaglavlje1.grid(row=0, column=0)
        
        labela_zaglavlje2 = tk.Label(tabela_okvir, text="Your Mind Map:", font=("Arial", 16, "bold"), background=c5)
        labela_zaglavlje2.grid(row=0, column=1)
        
        labela_red1_kolona1 = tk.Label(tabela_okvir, text=string, font=("Arial", 14), wraplength=750, background=c5)
        labela_red1_kolona1.grid(row=1, column=0)

        slicka = mindmap.wordCloudImage(string)
        
        tk_image = ImageTk.PhotoImage(slicka)
        
        labela_red1_kolona2 = tk.Label(tabela_okvir, image=tk_image, wraplength=750,borderwidth=0, relief="flat")
        labela_red1_kolona2.config(image=tk_image)
        labela_red1_kolona2.image = tk_image
        labela_red1_kolona2.grid(row=1, column=1)
        os.remove(naziv_fajla_bez_ext+".txt")

       
        
        
   elif eks == "pdf":
        metode.readPdf(f_path)
        naziv_fajla_bez_ext, _ = os.path.splitext(f_path)
        string = bart.sumiranje(naziv_fajla_bez_ext+".txt",test)
        
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
        os.remove(naziv_fajla_bez_ext+".txt")
        
   elif eks == "txt":
       
        naziv_fajla_bez_ext, _ = os.path.splitext(f_path)
        string = bart.sumiranje(naziv_fajla_bez_ext+".txt",test)
        
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
        os.remove(naziv_fajla_bez_ext+".txt")
   else:
        print("Nepoznata ekstenzija")

   

root = tk.Tk()
root.title("MindMaze")
# Uklonite okvir prozora
root.overrideredirect(False)

# Maksimizirajte prozor
root.state('zoom')

root.config(background=c5)

logo_image = tk.PhotoImage(file="img/logo.png")  # Zamenite putanju do vaše slike
resized_image = logo_image.subsample(5, 5)
logo_label = tk.Label(root, image=resized_image, bg=c5)
logo_label.pack()


button=tk.Button(root, text="Browse Folder", font =("Roboto", 14),
   command=browse)
options = ["Small Text", "Recommended text", "Large text"]

# Create a string variable to store the selected option
selected_option = tk.StringVar()
selected_option.set(options[0])  # Set the default option

def option_selected(value):
  global test
  if value == options[0]:
    print(1)
    test = 300
    print(test)
  elif value == options[1]:
     print(2)
     test = 500
     print(test)
  else:
     print(3)
     test = 750
     print(test)
# Create the option menu
option_menu = tk.OptionMenu(root, selected_option, *options, command=option_selected)
#option_menu.configure(**st.optionmenu)
option_menu["menu"].configure(
        font =("Roboto",20),
        background=c5,
        foreground=c4,
        relief="solid",
    )

# Function to handle option selection


# Pack the option menu
option_menu.pack(pady=5)
button.pack(pady=5)






root.mainloop()