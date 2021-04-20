import tkinter as tk
from tkinter import messagebox

from data_analyser import create_eq_map

class Interface_Menu():

    def __init__(self):

        # Utworzenie okna głównego.
        self.master = tk.Tk()
        self.master.title('Map creation menu')
        self.master.geometry("515x300")

        # Słowniki potrzebne do utworzenia przycisków pojedynczego wyboru.
        periods = {"Past day": "day",
                   "Past 7 days": "week",
                   "Past 30 days": "month",
                   }

        magnitudes = {"Over 4.5": "4.5",
                      "Over 2.5": "2.5",
                      "Over 1.0": "1.0",
                      }

        # Utworzenie dwóch grup przycisków pojedynczego wyboru.
        period_group = self.create_group("Select time period: ")
        period_group.grid(row=1, column=1)
        self.period_var = tk.StringVar(self.master, None)
        self.create_radiobuttons(periods, period_group, self.period_var)

        magnitude_group = self.create_group("Select magnitude: ")
        magnitude_group.grid(row=1, column=2)
        self.magnitude_var = tk.StringVar(self.master, None)
        self.create_radiobuttons(magnitudes, magnitude_group, self.magnitude_var)

        # Wyświetlenie notki informacyjnej i przycisku generującego mapę.
        note_text = '(Note that the greater data range you choose,\n the longer it will take to generate map.)'
        note = tk.Label(self.master, width=20, font=('bold', 9), text=note_text)
        note.grid(row=2, column=1, ipadx=60)

        button = tk.Button(self.master, text="Create map", command=self.push_button,
                           background="crimson", font=('bold', 14), bd=5)
        button.grid(row=2, column=2, pady=15, ipady=10, ipadx=35, sticky='e')

        # Pętla obsługująca działanie progamu w oknie.
        tk.mainloop()

    def create_group(self, title):
        # Utworzenie ramki wewnątrz okna.
        group = tk.LabelFrame(self.master, font=7, text=title)
        group.grid(row=1, ipadx=25, pady=20)
        return group

    def create_radiobuttons(self, dict, group, var):
        # Pętla do utworzenia listy jednokrotnego wyboru.
        for (text, value) in dict.items():
            tk.Radiobutton(group, text=text, variable=var,
                           value=value, indicator=0,
                           background="light blue").pack(side='top', fill='both', ipady=10)

    def push_button(self):
        # Funkcja sprawdzająca czy dostarczono niezbędne dane.
        if self.period_var.get() == "" or self.magnitude_var.get() == "":
            messagebox.showinfo("Error", "You have to select time period ang magnitude!")
        else:
            return create_eq_map(self.magnitude_var.get(), self.period_var.get())


if __name__ == '__main__':
    # Utworzenie i uruchomienie aplikacji.
    map = Interface_Menu()