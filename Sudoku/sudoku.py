from tkinter import Tk,Frame,LEFT,RIGHT,Label,GROOVE,Button,BOTH,DISABLED,NORMAL

from random import randint

def matrice_aleatoire():
    """Renvoie une matrice 9x9 d'entiers entre 1 et 9 choisis au hasard."""
    matrice_a = [
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
        [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),
         randint(1, 9), randint(1, 9)],
    ]
    return matrice_a


def verifier_matrice(matrice):
    """Renvoie 1 si la matrice est valide, 0 sinon."""
    lst_vide = []  # permet de stocker les information pour la vérifier

    # vérification des lignes

    for ligne in range(len(matrice)):  # pour chaque élément de la ligne de la matrice
        for colonne in range(len(matrice[0])):  # pour chaque élément de la colonne de la matrice
            if matrice[ligne][colonne] not in lst_vide:  # si l'élement de la ligne n'est pas dans la liste vide
                lst_vide.append(matrice[ligne][colonne])  # ajouter les éléments de la ligne dans la liste vide
            else:
                return 0
        lst_vide = []  # réinitialiser
    # vérification des colonnes
    for ligne in range(len(matrice)):  # pour chaque élément de la ligne de la matrice
        for colonne in range(len(matrice[0])):  # pour chaque élément de la colonne de la matrice
            if matrice[colonne][ligne] not in lst_vide:  # si l'élement de la colonne n'est pas dans la liste vide
                lst_vide.append(matrice[colonne][ligne])  # ajouter les éléments de la colonne dans la liste vide
            else:
                return 0
        lst_vide = []  # réinitialiser

    # vérification des sous matrices
    for ligne_sm in range(0, 9, 3):  # pour les sous matrice
        for colonne_sm in range(0, 9, 3):
            for ligne in range(ligne_sm,
                               ligne_sm + 3):  # pour chaque élément de la ligne sous matrice le +3 sert au nombre d'élément pris
                for colonne in range(colonne_sm,
                                     colonne_sm + 3):  # pour chaque élément de la colonne sous matrice le +3 sert au nombre d'élément pris
                    if matrice[ligne][
                        colonne] not in lst_vide:  # si l'élement de la colonne n'est pas dans la liste vide
                        lst_vide.append(
                            matrice[ligne][colonne])  # ajouter les éléments de la colonne dans la liste vide
                    else:
                        return 0
            lst_vide = []
    return 1


def grille_valide_aleatoire():
    """Renvoie une matrice 9x9 d'entiers choisis au hasard qui constitue une
    grille valide (d'après les critères Sudoku)."""
    matrice = [
        [1, 2, 3, 7, 8, 9, 4, 5, 6],
        [4, 5, 6, 1, 2, 3, 7, 8, 9],
        [7, 8, 9, 4, 5, 6, 1, 2, 3],
        [2, 3, 1, 8, 9, 7, 5, 6, 4],
        [5, 6, 4, 2, 3, 1, 8, 9, 7],
        [8, 9, 7, 5, 6, 4, 2, 3, 1],
        [3, 1, 2, 9, 7, 8, 6, 4, 5],
        [6, 4, 5, 3, 1, 2, 9, 7, 8],
        [9, 7, 8, 6, 4, 5, 3, 1, 2]
    ]
    nombre = randint(1, 9)
    for lignes in range(9):
        for colonnes in range(9):
            matrice[lignes][colonnes] = (matrice[lignes][
                                             colonnes] + nombre) % 9 + 1  # formule du décalage modulaire qui sert à renvoyer d’autres solutions valides plus variées.

    return matrice


def generer_puzzle():
    """Génère un puzzle à résoudre pour l'utilisateur, en partant d'une grille
    valide."""
    matrice = grille_valide_aleatoire()
    compteur = 0
    for ligne in range(9):  # pour chaque élément de la ligne de la matrice
        for colonne in range(9):  # pour chaque élément de la colonne de la matrice
            compteur += 1  # matrice [ligne][colonne]   #augmente
    while compteur > 25:
        n_ligne = randint(0, 8)
        n_colonne = randint(0, 8)  # on ne met pas 9 car on dépasserai la matrice
        compteur -= 1
        matrice[n_ligne][n_colonne] = 0
    return matrice


# FIN DE LA PARTIE A MODIFIER =================================================

# =============================================================================
# PARTIE A NE PAS MODIFIER ====================================================
# =============================================================================


class SudokuGUI:
    def __init__(self):
        """Initialise l'interface."""
        self.window = Tk()  # la fenêtre principale
        self.partie_gauche = Frame(self.window)
        self.partie_gauche.pack(side=LEFT)
        self.partie_droite = Frame(self.window, padx=32, width=256)
        self.partie_droite.pack(side=RIGHT)

        # initialiser la matrice de labels
        self.label_matrix = []
        for i in range(9):
            self.label_matrix.append([])
            for j in range(9):
                self.label_matrix[i].append(Label(self.partie_gauche, text=' ',
                                                  font=('Courier New', 12),
                                                  borderwidth=1, relief=GROOVE,
                                                  width=2))
                self.label_matrix[i][j].grid(row=i, column=j)

        # les boutons
        self.btn = Button(self.partie_droite, text='Remplir (aléatoire)',
                          command=self.remplissage_aleatoire)
        self.btn.pack(fill=BOTH, expand=1)
        self.btn = Button(self.partie_droite, text='Remplir (valide)',
                          command=self.remplissage_valide)
        self.btn.pack(fill=BOTH, expand=1)
        self.btn = Button(self.partie_droite, text='Puzzle',
                          command=self.remplissage_puzzle)
        self.btn.pack(fill=BOTH, expand=1)

        self.btn_verifier = Button(self.partie_droite, text='Vérifier',
                                   state=DISABLED,
                                   command=self.afficher_resultat)
        self.btn_verifier.pack(fill=BOTH, expand=1)

        self.resultat_verif = Label(self.partie_droite, text='', width=20)
        self.resultat_verif.pack(fill=BOTH, expand=1)

        self.window.title('Sudoku')
        self.window.mainloop()

    def matrice_entiere(self):
        """Renvoie la représentation de la matrice de labels sous forme de
        matrice d'entiers."""
        return [[int(self.label_matrix[i][j]['text']) for j in range(9)]
                for i in range(9)]

    def remplissage_aleatoire(self):
        """Remplit la matrice de labels avec des entrées entières aléatoires
        tirées dans 1, 2, ..., 9."""
        self.resultat_verif['text'] = ''
        matrice = matrice_aleatoire()
        if matrice is None:
            self.resultat_verif['text'] = "Pas encore implémenté"
        else:
            for i in range(9):
                for j in range(9):
                    self.label_matrix[i][j]['text'] = str(matrice[i][j])

            self.btn_verifier['state'] = NORMAL

    def remplissage_puzzle(self):
        """Remplit la matrice de labels avec un puzzle sudoku à résoudre."""
        self.resultat_verif['text'] = ''
        matrice = generer_puzzle()
        if matrice is None:
            self.resultat_verif['text'] = "Pas encore implémenté"
        else:
            for i in range(9):
                for j in range(9):
                    if matrice[i][j]:
                        self.label_matrix[i][j]['text'] = str(matrice[i][j])
                    else:
                        self.label_matrix[i][j]['text'] = ''

            # vérifier un puzzle non rempli n'a pas de sens, on désactive le
            # bouton
            self.btn_verifier['state'] = DISABLED

    def remplissage_valide(self):
        """Génère une grille valide de Sudoku."""
        matrice = grille_valide_aleatoire()
        # remplissage des labels
        for i in range(9):
            for j in range(9):
                self.label_matrix[i][j]['text'] = str(matrice[i][j])

        self.resultat_verif['text'] = ''
        self.btn_verifier['state'] = NORMAL

    def afficher_resultat(self):
        """Affiche le résultat de la vérification de la matrice."""
        matrice = self.matrice_entiere()
        r = verifier_matrice(matrice)
        messages = ['Matrice non valide', 'Matrice valide',
                    'Pas encore implémenté']
        if r > 1 or r < -1:
            self.resultat_verif['text'] = 'Code de retour inconnu'
        else:
            self.resultat_verif['text'] = messages[r]


if __name__ == "__main__":
    SudokuGUI()

