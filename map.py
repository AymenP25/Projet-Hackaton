import random

# Constantes
WALL = '#'
FLOOR = '.'
PLAYER = '@'
COIN = '$'
ENEMIES = ['K', 'M']


class GameMap:
    def __init__(self, largeur, hauteur, ennemicpt):
        self.largeur = largeur
        self.hauteur = hauteur
        self.ennemicpt = ennemicpt

        self.tab = self._create_empty_map()
        self.player_pos = (1, 1)

        self._place_enemies()

    def _create_empty_map(self):
        """Crée une map entourée de murs, premier jet c'est juste un cadre entouré de murs"""
        self.ennemis = []
        self.coins = []

        self._place_enemies()
        self._place_coins(3)

    def _create_empty_map(self):
        """Crée une map entourée de murs"""
        tab = []
        for y in range(self.hauteur):
            row = []
            for x in range(self.largeur):
                if x == 0 or y == 0 or x == self.largeur - 1 or y == self.hauteur - 1:
                    row.append(WALL)
                else:
                    row.append(FLOOR)
            tab.append(row)
        return tab

    def _place_enemies(self):
        placed = 0
        while placed < self.ennemicpt:
            x = random.randint(1, self.largeur - 2)
            y = random.randint(1, self.hauteur - 2)

            if self.tab[y][x] == FLOOR:
                ennemi = random.choice(ENEMIES)
                self.tab[y][x] = ennemi
                self.ennemis.append({
                    "type": ennemi,
                    "x": x,
                    "y": y,
                    "hp": 5
                })
                placed += 1

    def _place_coins(self, count):
        placed = 0
        while placed < count:
            x = random.randint(1, self.largeur - 2)
            y = random.randint(1, self.hauteur - 2)

            if self.tab[y][x] == FLOOR:
                self.tab[y][x] = COIN
                self.coins.append((x, y))
                placed += 1

    def check_pickup(self, hero):
        # On récupère ce qu'il y a sur la case actuelle du héros
        on_map = self.tab[hero.y][hero.x]
        
        if on_map == $:
            # 1. Calculer la valeur aléatoire
            valeur = random.randint(10, 50)
            
            # 2. Ajouter au compteur du héros 
            hero.gold += valeur
            
            # 3. Faire disparaître la pièce (on remet du sol '.') [cite: 21, 43]
            self.tab[hero.y][hero.x] = FLOOR
            
            # 4. Afficher le message de succès 
            hero.message = f"Vous avez trouvé {valeur} pièces d'or !"

    def is_walkable(self, x, y):
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            return self.tab[y][x] in [FLOOR, COIN]
        return False

    def display(self):
        px, py = self.player_pos
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if (x, y) == (px, py):
                    print(PLAYER, end="")
                else:
                    print(self.tab[y][x], end="")
            print()


# -----------------------
# Exemple d'utilisation
# -----------------------


game_map = GameMap(10, 6, 2)  # largeur, hauteur, nombre d’ennemis
game_map.display()