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
    "Behemoth" : "Monstre marin",
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
    "Docte" : "Savant",
    "Dodu" : "Grassouillet",
    "Émissaire" : "Agent cherché d’une mission",
    "Érudit" : "Savant",
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
    "Lagune" : "Étendue d’eau séparée par une bande de terre",
    "Languissant" : "Qui manque d’énergie",
    "Lépante" : "Grande bataille maritime de l’Antiquité",
    "Léviathan" : "Monstre marin",
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
    global errors
    if entry.get() == '':
        label1.config(text = "Write Something", fg = 'gold3')
    else:
        if entry.get().title() == toGuess:
            del words[toGuess]
            if len(words) == 0:
                messagebox.showinfo("You Finished", f"You Finished The Game With {errors} Errors")
                quit()
            else:
                temp_text('e')
                label1.config(text = 'What Is The Name Of', fg = "black")
                main()
        else:
            errors += 1
            ErrorLabel.config(text = f"Errors : {errors}")
            label1.config(text = "Try Again", fg = "red")
def temp_text(e):
    entry.delete(0, "end")
    entry.config(fg = 'black')
def reset():
    global words, errors
    errors = 0
    words = definitions
    main()
def main():
    global errors, toGuess
    toGuess = random.choice(list(words))
    label2.config(text = words[toGuess])


root = tkinter.Tk()
root.geometry("500x250")
root.resizable(False, False)
root.title("French Vocab Quiz")
label1 = tkinter.Label(text = "What Is The Name Of", font = ("Arial", 25))
label1.pack(pady = 10)

label2 = tkinter.Label(text = "Word", font = ("Arial", 23), fg = "forest green")
label2.pack(pady = 10)
reset()

ErrorLabel = tkinter.Label(text = f"Errors : {errors}", font = ("Arial", 15), fg = 'red3')
ErrorLabel.place(y = 160, x = 37.5)

entry = tkinter.Entry(width = 25, font = ("Arial", 21), justify = "center")
entry.place(y = 190, x = 39)
entry.insert(0, "Start")
entry.bind("<Return>", check)
entry.bind("<FocusIn>", temp_text)

photo = tkinter.PhotoImage(file = r"quit.png")
Quit = tkinter.Button(root, height = 32, width = 32, image = photo, command=lambda:quit())
Quit.place(y = 0, x = 0)


root.mainloop()

