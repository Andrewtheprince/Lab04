import time
import flet as ft
import model as md
from view import View

class SpellChecker:

    def __init__(self, v:View):
        self._multiDic = md.MultiDictionary()
        self._view = v

    def handleSpellCheck(self, e):
        frase = self._view._txtIn.value
        lingua = self._view._tendinaLingua.value
        modalita = self._view._tendinaModalita.value
        if frase == "":
            self._view._txtOut.controls.append(ft.Text(f"Devi prima inserire una frase!", color="red"))
            self._view.update()
            return
        if lingua == "":
            self._view._txtOut.controls.append(ft.Text(f"Devi prima selezionare una lingua!", color="red"))
            self._view.update()
            return
        if modalita =="":
            self._view._txtOut.controls.append(ft.Text(f"Devi prima selezionare una modalità!", color="red"))
            self._view.update()
            return
        self._view._txtOut.clean()
        self._view._txtOut.controls.append(ft.Text(frase))
        (parole, tempo) = self.handleSentence(frase, lingua, modalita)
        self._view._txtOut.controls.append(ft.Text(f"Parole errate: {parole}"))
        self._view._txtOut.controls.append(ft.Text(f"Tempo richiesto dalla ricerca: {tempo}"))
        self._view._txtIn.value = ""
        self._view.update()


    def handleLinguaSelezionata(self, e):
        print(f"Selezionato {self._view._tendinaLingua.value}")
        self._view._txtOut.controls.append(ft.Text(f"Selezionato {self._view._tendinaLingua.value}!", color="green"))
        self._view.page.update()


    def handleModalitaSelezionata(self, e):
        print(f"Selezionata modalità {self._view._tendinaModalita.value}")
        self._view._txtOut.controls.append(ft.Text(f"Selezionata modalità {self._view._tendinaModalita.value}!", color="green"))
        self._view.page.update()


    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text