import random
import tkinter
from tkinter import messagebox

definitions = {
    "Abîme" : "Espace vide",
    "Abysse" : "Gouffre marin",
    "Akkad" : "État de la Mésopotamie antique",
    "Altérer" : "Assoiffer",
    "Armateur" : "Propriétaire d’un navire",
    "Atavique" : "Héréditaire",
    "Behemoth" : "Monstre marin 1",
    "Bey" : "Officier d’un sultan",
    "Cabalistique" : "Mystérieux, difficile à comprendre",
    "Chébèque" : "Voilier turc",
    "Chiourme" : "Ensemble des rameurs d’une galère",
    "Chu" : "Tombé",
    "Conspuer" : "Huer",
    "Cyrénaïque" : "Région de l’Afrique du Nord",
    "Dagon" : "Dieu poisson",
    "Damasquiné" : "Incrusté de filets d’argent ou d’or",
    "Délié" : "Tracé d’une lettre",
    "Dessein" : "Destin, aventure",
    "Docte" : "Savant 1",
    "Dodu" : "Grassouillet",
    "Émissaire" : "Agent cherché d’une mission",
    "Érudit" : "Savant 2",
    "Escarcelle" : "Bourse attachée à la ceinture",
    "Étique" : "Très maigre",
    "Famélique" : "Amaigri par manque de nourriture",
    "Funeste" : "Qui apporte le malheur, la mort",
    "Gemme" : "Pierre précieuse",
    "Glapir" : "Crier en parlant du renard",
    "Hermétisme" : "Langage mystérieux des alchimistes",
    "Hidalgo" : "Noble espagnol",
    "Huis" : "Porte",
    "Hyksos" : "Dynastie égyptienne",
    "Infortune" : "Mésaventure",
    "Lagune" : "Étendue d’eau séparée\npar une bande de terre",
    "Languissant" : "Qui manque d’énergie",
    "Lépante" : "Grande bataille maritime\nde l’Antiquité",
    "Léviathan" : "Monstre marin 2",
    "Occis" : "Tué",
    "Ottoman" : "Turc",
    "Pécune" : "Argent",
    "Pitres" : "Clowns",
    "Ressac" : "Retour des vagues sur elles-mêmes",
    "Romanichels" : "Bohémiens",
    "Salamalec" : "Discours",
    "Saltimbanques" : "Comédiens itinérants",
    "Sénile" : "Vieux",
    "Sublime Porte" : "Monument turc",
    "Talisman" : "Objet magique",
    "Umar Kayyam" : "Philosophe perse",
    "Versatile" : "Converti (religion)",
}


def check(e):
    global errors, wrongs, answers
    if e == "skip":
        if errors == 0 and skips == 0:
            messagebox.showinfo("Bravo!", "Tu as fini le quiz avec 0 erreures!")
            quit()
        else:
            if messagebox.askyesno("Bravo!",
                                   f"Tu as fini le jeu\navec {errors} erreures et tu as skipper {skips} fois\n"
                                   f"Voudrais-tu voir tes erreures?"):
                toprint = ''
                wrongs = wrongs
                answers = answers
                for i in range(len(wrongs)):
                    toprint = toprint + f'{answers[i]} est {wrongs[i]}\n'
                messagebox.showinfo('Get Better', toprint)
                quit()
            else:
                quit()
    else:
        if entry.get() == '':
            label1.config(text = "Écrit Quelque Chose", fg = 'chocolate2')
        else:
            if entry.get().title() == toGuess:
                del words[toGuess]
                if len(words) == 0:
                    if errors == 0 and skips == 0:
                        messagebox.showinfo("Félicitation", "Tu as fini le jeu avec 0 erreures!")
                    else:
                        if messagebox.askyesno("Bravo", f"Tu as fini le jeu\navec {errors} erreures et tu as skipper {skips} fois\n"
                                                        f"Voudrais-tu voir tes erreures"):
                             toprint = ''
                             wrongs = wrongs
                             answers = answers
                             for i in range(len(wrongs)):
                                toprint = toprint+f'{answers[i]} est {wrongs[i]}\n'
                             messagebox.showinfo('Get Better', toprint)
                             quit()
                        else:
                            quit()
                else:
                    temp_text('e')
                    label1.config(text = "C'est quoi le nom de", fg = "black")
                    main()
            else:
                errors += 1
                if toGuess in wrongs:
                    temp_text('e')
                    ErrorLabel.config(text=f"Erreures : {errors}")
                    label1.config(text="Essaie encore", fg="red")
                else:
                    wrongs.append(toGuess)
                    answers.append(words[toGuess])
                    temp_text('e')
                    ErrorLabel.config(text = f"Erreures : {errors}")
                    label1.config(text = "Essaie encore", fg = "red")
def temp_text(e):
    entry.delete(0, "end")
    entry.config(fg = 'black')
def reset():
    global words, errors, wrongs, answers, skips
    errors = 0
    skips = 0
    words = definitions
    wrongs = []
    answers = []
    main()
def main():
    global errors, toGuess
    toGuess = random.choice(list(words))
    label2.config(text = words[toGuess])
def skip():
    global skips
    skips += 1
    SkipLabel.config(text = f"Skips : {skips}")
    label1.config(text= "C'est quoi le nom de", fg="black")
    if len(words) == 1:
        if toGuess in wrongs:
            del words[toGuess]
            check('skip')
        else:
            wrongs.append(toGuess)
            answers.append(words[toGuess])
            del words[toGuess]
            check('skip')
    else:
        if toGuess in wrongs:
            del words[toGuess]
            temp_text('e')
            main()
        else:
            wrongs.append(toGuess)
            answers.append(words[toGuess])
            del words[toGuess]
            temp_text('e')
            main()

root = tkinter.Tk()
root.geometry("500x250")
root.resizable(False, False)
root.title("Quiz de Capes et de Crocs")
label1 = tkinter.Label(text = "C'est quoi le nom de", font = ("Arial", 25))
label1.pack(pady = 10)

label2 = tkinter.Label(text = "Word", font = ("Arial", 23), fg = "forest green")
label2.pack()
reset()

ErrorLabel = tkinter.Label(text = f"Erreures : {errors}", font = ("Arial", 15), fg = 'red3')
ErrorLabel.place(y = 160, x = 37.5)

SkipLabel = tkinter.Label(root, text = f"Skips : {skips}", font = ("Arial", 15), fg = 'gold2')
SkipLabel.place(y = 160, x = 160)

entry = tkinter.Entry(width = 25, font = ("Arial", 21), justify = "center")
entry.place(y = 190, x = 39)
entry.insert(0, "Commence à taper")
entry.bind("<Return>", check)
entry.bind("<FocusIn>", temp_text)

photo_skip = tkinter.PhotoImage(file = r"skip.png")
SkipB = tkinter.Button(text = "Skip", fg = 'gold4', height = 32, width = 64, image = photo_skip, compound = 'left', command=skip)
SkipB.place(y = 147.5, x = 371)

photo_quit = tkinter.PhotoImage(file = r"quit.png")
Quit = tkinter.Button(root, height = 32, width = 32, image = photo_quit, command=lambda:quit())
Quit.place(y = 0, x = 0)


root.mainloop()

