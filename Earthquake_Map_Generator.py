import tkinter as tk
from tkinter import messagebox

from data_analyser import create_eq_map


# Utworzenie głównego okna.
master = tk.Tk()
master.title('Map creation menu')
master.geometry("480x300")

period_group = tk.LabelFrame(master, text="\nSelect time period: \n")
period_group.grid(row=1, column=1, ipadx=25)

magnitude_group = tk.LabelFrame(master, text="\nSelect magnitude: \n")
magnitude_group.grid(row=1, column=2, ipadx=25)

# Zainicjowanie zmiennych do przechowywania danych z przycisków.
period = tk.StringVar(master, None)
magnitude = tk.StringVar(master, None)

# Słownik potrzebny do utworzenia wielu przycisków.
periods = {"Past day": "day",
           "Past 7 days": "week",
           "Past 30 days": "month",
           }

magnitudes = {"Over 4.5": "4.5",
              "Over 2.5": "2.5",
              "Over 1.0": "1.0",
              }


def push_button():
    if magnitude.get() == "" or period.get() == "":
        messagebox.showinfo("Error", "You have to select time period ang magnitude!")
    else:
        return create_eq_map(magnitude.get(), period.get())


# Pętla do utworzenia obu list jednokrotnego wyboru.
for (text, value) in periods.items():
    tk.Radiobutton(period_group, text=text, variable=period,
                   value=value, indicator=0,
                   background="light blue").pack(side='top', fill='both', ipady=10)

for (text, value) in magnitudes.items():
    tk.Radiobutton(magnitude_group, text=text, variable=magnitude,
                   value=value, indicator=0,
                   background="light blue").pack(side='top', fill='both', ipady=10)

note = tk.Label(master, width=20, font = ('bold', 9), text='(Note that the greater data range you choose,\n'
                                       ' the longer it will take to generate map.)')
button = tk.Button(master, text="Create map", command=push_button, background="crimson", font=('bold',14), bd=5)

note.grid(row=2, column=1, ipadx=60)
button.grid(row=2, column=2, pady=35, ipady=10, ipadx=35, sticky='e')

# Pętla obsługująca działanie progamu w oknie.
tk.mainloop()
