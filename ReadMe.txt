Juhos Norbert (C0LOQL)

Feladat leírása
Ez a projekt egy egyszerű időpontfoglaló alkalmazás, amelyet Python Tkinter-rel készült. Az alkalmazás lehetővé teszi a felhasználók számára, hogy foglalásokat hozzanak létre, és töröljenek. Az adatok egy különálló modulban kezelt txt fájlban tárolódnak.


Modulok és a modulokban használt függvények
file_JN.py (Fájlkezelő modul)

FajlkezeloJn osztály:

init(self, fajlnev): Inicializálja az osztályt, beállítva a kezelendő fájl nevét.

betolt_jn(self): Beolvassa a mentett adatokat a fájlból, listaként visszaadja.

mentes_jn(self, tartalom): A megadott listát visszamenti a fájlba.

torol_jn(self, eltavolitando): Töröl egy adott sort az adatok közül, majd menti a változást.

Időpontfoglaló alkalmazás (main.py)
IdopontfoglaloJn osztály:

init(self, jn): Inicializálja a GUI-t, létrehozza az elemeket, beköti a billentyűparancsokat (Esc bezárás, Enter foglalás, Del törlés), betölti az adatokat.

esc_jn(self, event): Az Esc billentyű eseménykezelője, bezárja az ablakot.

foglalas_rogzitese_jn(self): A foglalás rögzítéséért felelős metódus, ellenőrzésekkel, adatfeltöltéssel és mentéssel.

torles_jn(self): Kijelölt foglalás törlése a listából és a fájlból.
