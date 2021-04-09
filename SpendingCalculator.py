import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --
root = tk.Tk()
ttk.Label(root, text="Spending Calculator", padding=(50, 10)).pack()

names = ( "Alyssa","Antoine")

info_value = tk.StringVar()
prix_value = tk.StringVar()
output = tk.StringVar()


def ajouter_depense(*args):
	try:
		depenseInfo = (info_value.get())
		depensePrix = (prix_value.get())
		depenseNom = selNames_select.get(selNames_select.curselection())

		if len(depenseInfo) & len(depensePrix) <= 0:
			return
		else:
			pass

		
		output.set(f"{depensePrix}  {depenseInfo} {depenseNom}")

		depenses_textbox = tk.Label(root, text="", textvariable=output, height=1)
		depenses_textbox.pack()
		
	except ValueError:
		print("Value error")




# -- Text widgets pour prix et info --

info_label = ttk.Label(root, text="Info")
info_input = ttk.Entry(root, width=10, textvariable=info_value)
info_label.pack()
info_input.pack()
info_input.focus()

prix_label = ttk.Label(root, text="Prix")
prix_label_input = ttk.Entry(root, width=10, textvariable=prix_value)
prix_label.pack()
prix_label_input.pack()

# -- Liste pour selection de noms --

selNames = tk.StringVar(value=names)
selNames_select = tk.Listbox(root, listvariable=selNames, height=2)
selNames_select.select_set(0)
selNames_select.pack(padx=10, pady=10)

selNames_select["selectmode"] = "browse"

# -- Bouton Ajout Dépense --

send_button = ttk.Button(root, text="Ajouter dépense", command=ajouter_depense)
send_button.pack()

main_sep = ttk.Separator(root, orient="horizontal")
main_sep.pack(fill="x", pady=10)

# -- Box pour afficher les entrées --

depenses_label = ttk.Label(root, text="Dépenses")
depenses_label.pack()



root.mainloop()