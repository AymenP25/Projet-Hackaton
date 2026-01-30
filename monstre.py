class Monster:
    def __init__(self):
        self.monsters = {(3, 2): {'vie': 15, 'max_vie': 15, 'name': 'K'}}

    def attack_monster(self, hero, pos):
        monster = self.monsters[pos]
        
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
            xp_gain = 20
            hero.gain_xp(xp_gain)
            del self.monsters[pos] 
            hero.message = f" A battu K +{xp_gain} XP"

    def barre_de_vie(self, actuel, maximum, length=20, symbol="#", label="HP"):
    # On s'assure que le pourcentage est entre 0 et 1 pour éviter les bugs
    percent = min(1.0, actuel / maximum)
    filled = int(length * percent)
    #barre visuelle: partie pleine avec le symbole et la partie vide avec des tirets
    bar = (symbol * filled) + ("-" * (length - filled))
    #affichage final [###---]"
    return f"{label} [{bar}] {actuel}/{maximum}"

    def avancer_monstres(self, game_map, hero):
        """Déplacement aléatoire de tous les monstres sur la carte"""
        import random 
        
        #nouveau dico pour stocker les nouvelles positions
        nouvelles_positions = {}

        for (x, y), stats in self.monsters.items():
            #direction aleatoire: Haut, Bas, Gauche, Droite ou Rester sur place
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
            dx, dy = random.choice(directions)
            
            nx, ny = x + dx, y + dy
            
            #on check si le mouvement est possible
            # On vérifie si c'est pas un mursi c'est pas la case du héros,
            # et si un autre monstre n'est pas la
            if (game_map.is_walkable(nx, ny) and (nx, ny) != (hero.x, hero.y) and 
                (nx, ny) not in nouvelles_positions):
                
                #bouger
                nouvelles_positions[(nx, ny)] = stats
            else:
                #bloqué
                nouvelles_positions[(x, y)] = stats
        
        #MAJ
        self.monsters = nouvelles_positions