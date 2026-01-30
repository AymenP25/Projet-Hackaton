import random
class Monster:
    def __init__(self, game_map):
        self.game_map = game_map
        self.monsters = {}
        self.monsters = {(3, 2): {'vie': 15, 'max_vie': 15, 'name': 'K'}}

    def spawn_monsters(self, n):
        placed = 0

        while placed < n:
            x = random.randint(1, self.game_map.largeur - 2)
            y = random.randint(1, self.game_map.hauteur - 2)

            if self.game_map.is_walkable(x, y) and (x, y) not in self.monsters:
                monster_type = random.choice(['K', 'M'])
                self.monsters[(x, y)] = {
                    "name": monster_type,
                    "vie": 15 if monster_type == 'K' else 10,
                    "max_vie": 15 if monster_type == 'K' else 10,
                    "dead": False
                }
                placed += 1

    def attack_monster(self, hero, pos):
        monster = self.monsters[pos]
        
        if not monster:
            return
        print("Combat déclenché contre", monster['name'])
        
        # Le héros frappe le monstre
        attaque = 5
        monster['vie'] -= attaque
        #pour le coté interactif, on rajoute un message
        hero.message = f"Vous frappez {monster['name']} (-{attaque} PV)"

        #le monstre attaque le heros
        if monster['vie'] > 0:
            reponse = 2
            hero.hp -= reponse
            hero.message += f" | {monster['name']} riposte (-{reponse} PV)"
        else:
            #si le heros tue le monstre, il gagne des points de vie
            #xp_gain = 20
            #hero.gain_xp(xp_gain)
            monster['dead'] = True 
            hero.message = f" A battu K"

    def barre_de_vie(self, actuel, maximum, length=20, symbol="#", label="HP"):
        # On s'assure que le pourcentage est entre 0 et 1 pour éviter les bugs
        percent = min(1.0, actuel / maximum)
        filled = int(length * percent)
        #barre visuelle: partie pleine avec le symbole et la partie vide avec des tirets
        bar = (symbol * filled) + ("-" * (length - filled))
        #affichage final [###---]"
        return f"{label} [{bar}] {actuel}/{maximum}"


    def barre_de_vie(self, actuel, maximum, length=20, symbol="#", label="HP"):
        percent = max(0, min(1.0, actuel / maximum))
        filled = int(length * percent)
        bar = symbol * filled + "-" * (length - filled)
        return f"{label} [{bar}] {actuel}/{maximum}"

    def afficher_barres(self):
        lignes = []
        for (x, y), m in self.monsters.items():
            if m.get("dead"):
                continue

            bar = self.barre_de_vie(
                m['vie'],
                m['max_vie'],
                label=m['name']
            )
            lignes.append(f"{m['name']} ({x},{y}) {bar}")

        return lignes

    def avancer_monstres(self, game_map, hero):
        """Déplacement aléatoire de tous les monstres sur la carte"""
        import random 
        
        #nouveau dico pour stocker les nouvelles positions
        nouvelles_positions = {}

        for (x, y), stats in self.monsters.items():

            if stats.get('dead'):
                continue

            #direction aleatoire: Haut, Bas, Gauche, Droite ou Rester sur place
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
            dx, dy = random.choice(directions)
            
            nx, ny = x + dx, y + dy
            
            #on check si le mouvement est possible
            # On vérifie si c'est pas un mursi c'est pas la case du héros,
            # et si un autre monstre n'est pas la
            if (nx, ny) == (hero.x, hero.y):
                hero.hp -= 2
                hero.message = f"{stats['name']} vous attaque (-2 PV)"
                nouvelles_positions[(x, y)] = stats
                continue

            if (game_map.is_walkable(nx, ny) and (nx, ny) != (hero.x, hero.y) and 
                (nx, ny) not in nouvelles_positions):
                
                #bouger
                nouvelles_positions[(nx, ny)] = stats
            else:
                #bloqué
                nouvelles_positions[(x, y)] = stats
        
        #MAJ
        self.monsters = nouvelles_positions