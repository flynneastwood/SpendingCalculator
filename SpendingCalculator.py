import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

names = ("Antoine", "Alyssa")

def ajouter_depense(*args):
	try:
		depenseInfo = string(info_value.get())
		depensePrix = string(prix_value.get())
		depenseNom = string(selNames.get())
	except ValueError:
		pass


root = tk.Tk()
ttk.Label(root, text="Spending Calculator", padding=(50, 10)).pack()

depense_value = tk.StringVar()


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
selNames_select.pack(padx=10, pady=10)

selNames_select["selectmode"] = "browse"

# -- Bouton Ajout Dépense --

send_button = ttk.Button(root, text="Ajouter dépense")
send_button.pack()

main_sep = ttk.Separator(root, orient="horizontal")
main_sep.pack(fill="x", pady=10)

# -- Box pour afficher les entrées --

depenses_label = ttk.Label(root, text="Dépenses")
depenses_label.pack()

depenses_textbox = tk.Text(root, height=8)  # Show what happens if you `.pack()` here, while still assigning to variable.
depenses_textbox.pack()


main_sep = ttk.Separator(root, orient="horizontal")
main_sep.pack(fill="x", pady=10)


root.mainloop()