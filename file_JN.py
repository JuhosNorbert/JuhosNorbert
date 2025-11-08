# fajl kezelés JN

class FajlkezeloJn:
    def __init__(self, fajlnev):
        self.fajlnev = fajlnev

    def betolt_jn(self):
        tartalom = []
        try:
            with open(self.fajlnev, "r", encoding="utf-8") as f:
                for sor in f:
                    s = sor.strip()
                    if s:
                        tartalom.append(s)
        except FileNotFoundError:
            with open(self.fajlnev, "w", encoding="utf-8"):
                pass
        return tartalom

    def mentes_jn(self, tartalom):
        with open(self.fajlnev, "w", encoding="utf-8") as f:
            for sor in tartalom:
                f.write(sor + "\n")
    def torol_jn(self, eltavolitando):
        tartalom = self.betolt_jn()
        if eltavolitando in tartalom:
            tartalom.remove(eltavolitando)
            self.mentes_jn(tartalom)
            return True
        return False