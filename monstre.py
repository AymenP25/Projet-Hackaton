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
        percent = max(0,actuel / maximum)
        filled = int(length * percent)
        #je veux construire visuellement la barre de vie
        bar =
        return f" [{bar}] {actuel}/{maximum}"