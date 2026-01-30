import random

WALL = '#'
FLOOR = '.'
PLAYER = '@'
ENEMIES = ['K', 'M']


class GameMap:
    def __init__(self, largeur, hauteur, ennemicpt):
        self.largeur = largeur
        self.hauteur = hauteur
        self.ennemicpt = ennemicpt
        self.tab = self._create_empty_map()
        self.player_pos = (1, 1)
        self.ennemis = []

    self._place_enemies()

    def _create_empty_map(self):
    """Crée une map entourée de murs, premier jet c'est juste un cadre entouré de murs"""
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

    def display(game_map, hero, monster_manager):
        for y in range(game_map.hauteur):
            for x in range(game_map.largeur):
                if (x, y) == (hero.x, hero.y):
                print("@", end="")
                elif (x, y) in monster_manager.monsters:
                print("M", end="")
                else:
                print(game_map.tab[y][x], end="")
                print()


def is_walkable(self, x, y):
# Vérifie si la case est du sol, une porte ou un escalier
    if 0 <= y < self.hauteur and 0 <= x < self.largeur:
        return self.tab[y][x] in [".", "+", "=", "#"]
    return False
