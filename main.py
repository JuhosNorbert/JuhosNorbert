# időpontfoglaló JN C0LOQL
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from file_JN import FajlkezeloJn

class IdopontfoglaloJn:
    def esc_jn(self,event):
        self.root.destroy()



    def __init__(self, jn):
        self.root = jn
        self.root.title("GUMIFLEX Kft.- Időpont foglaló gumicserére")

        self.root.bind('<Escape>', self.esc_jn)

        tk.Label(jn, text="Név: ").grid(row=0, column=0, padx=10, pady=10, sticky ='E')
        self.nev_entry = tk.Entry(jn, width=60)
        self.nev_entry.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        tk.Label(jn, text="Rendszám: ").grid(row=1, column=0, padx=10, pady=10, sticky ='E')
        self.rszam_entry = tk.Entry(jn, width=60)
        self.rszam_entry.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

        tk.Label(jn, text="Dátum (ÉÉÉÉ-HH-NN):").grid(row=2, column=0, padx=10, pady=10, sticky='E')
        self.ev_cb= ttk.Combobox(jn, values=["2025", "2026", "2027", "2028", "2029"], width=5)
        self.ev_cb.grid(row=2, column=1, padx=(0, 5), pady=10, sticky='W')
        self.ev_cb.current(0)

        self.honap_cb= ttk.Combobox(jn, values=["jan", "febr", "marc", "apr", "maj", "jun", "jul", "aug", "sept", "okt", "nov", "dec"], width=5)
        self.honap_cb.grid(row=2, column=2, padx=(0, 5), pady=10, sticky='W')
        self.honap_cb.current(0)

        self.nap_cb= ttk.Combobox(jn, values=[f"{i:02d}" for i in range(1, 32)], width=3)
        self.nap_cb.grid(row=2, column=3, padx=(0, 5), pady=10, sticky='W')
        self.nap_cb.current(0)


        tk.Label(jn, text="Időpont:").grid(row=3, column=0, padx=10, pady=10, sticky='E')

        self.ora_cb = ttk.Combobox(jn, values=["8", "9", "10", "11", "12", "13", "14", "15"], width=3)
        self.ora_cb.grid(row=3, column=1, padx=(0, 2), pady=10, sticky='W')
        self.ora_cb.current(0)

        tk.Label(jn, text=":").grid(row=3, column=2, pady=10, sticky='W')

        self.perc_cb = ttk.Combobox(jn, values=["00", "15", "30", "45"], width=3)
        self.perc_cb.grid(row=3, column=3, padx=(2, 10), pady=10, sticky='W')
        self.perc_cb.current(0)

        self.foglalasok_lb = tk.Listbox(jn, width=80)
        self.foglalasok_lb.grid(row=6, column=0,padx=10, columnspan=5, pady=10)

        self.foglal_btn = tk.Button(jn, text="Foglalás", command=self.foglalas_rogzitese_jn)
        self.foglal_btn.grid(row=4, column=0, columnspan=5, pady=5)
        jn.bind('<Return>',lambda event: self.foglalas_rogzitese_jn())

        self.torol_btn = tk.Button(jn, text="Törlés", command=self.torles_jn)
        self.torol_btn.grid(row=4, column=1, columnspan=5, pady=5)
        jn.bind('<Delete>',lambda event: self.torles_jn())

        self.foglalasok = []

        self.fajlkezelo = FajlkezeloJn("foglalasok.txt")
        self.foglalasok = self.fajlkezelo.betolt_jn()
        for i in self.foglalasok:
            self.foglalasok_lb.insert(tk.END, i)

    def foglalas_rogzitese_jn(self):
        nev = self.nev_entry.get().strip().upper()
        rendszam = self.rszam_entry.get().strip().upper()

        ev = self.ev_cb.get().strip()
        honap = self.honap_cb.get().strip()
        nap = self.nap_cb.get().strip()

        ora = self.ora_cb.get().strip()
        perc = self.perc_cb.get().strip()

        datum = f"{ev}-{honap}-{nap}"
        idopont = f"{ora}:{perc}"

        if not nev or not rendszam or not ev or not honap or not nap or not ora or not perc:
            messagebox.showwarning("Hiányzó adat", "Kérlek, tölts ki minden mezőt!")
            return

        foglalt_idopontok = [f"{f.split()[0]} {f.split()[1]}" for f in self.foglalasok]
        if f"{datum} {idopont}" in foglalt_idopontok:
            messagebox.showerror("Ütközés", "Ez a időpont már foglalt!")
            return

        foglalas = f"{datum:<15}\t{idopont:<20}\t{rendszam:<25}\t{nev}"
        self.foglalasok.append(foglalas)
        self.foglalasok_lb.insert(tk.END, foglalas)
        self.fajlkezelo.mentes_jn(self.foglalasok)

        self.nev_entry.delete(0, tk.END)
        self.rszam_entry.delete(0, tk.END)
        self.ev_cb.current(0)
        self.honap_cb.current(0)
        self.nap_cb.current(0)
        self.ora_cb.current(0)
        self.perc_cb.current(0)

    def torles_jn(self):
        kivalasztott = self.foglalasok_lb.curselection()
        if not kivalasztott:
            messagebox.showerror("Hiba","Nincs kijelölve a törlendő adat.")
            return
        torlendo_foglalas = self.foglalasok_lb.get(kivalasztott[0])

        if self.fajlkezelo.torol_jn(torlendo_foglalas):
            self.foglalasok_lb.delete(kivalasztott[0])
            self.foglalasok.remove(torlendo_foglalas)
            messagebox.showinfo("Siker", "A foglalás törölve lett.")
        else:
            messagebox.showerror("Hiba", "Hiba lépett fel a törlés alatt.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("550x500")
    app = IdopontfoglaloJn(root)
    root.mainloop()