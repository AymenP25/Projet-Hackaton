class Hero:
    def __init__(self, x, y):  
        #On définit les caractéristiques principales de notre personnage
        self.x = x
        self.y = y
        self.hp = 100
        self.maxhp = 100
        self.message = ""
        self.strength = 16
        self.coin = 0   
        self.message = "Bienvenue dans le donjon !"

    def afficher_hp(self):
        percent = self.hp / self.maxhp
        filled = int(20 * percent)
        bar = "#" * filled + "-" * (20 - filled)
        return f"Héros HP [{bar}] {self.hp}/{self.maxhp}"


    def move(self, dx, dy, game_map, monsters, monster_manager):
        new_x, new_y = self.x + dx, self.y + dy
        print("Héros tente d'aller en", new_x, new_y)
        print("Monstres:", monster_manager.monsters.keys())
       
        #regarde si le héros se bat
        if (new_x, new_y) in monster_manager.monsters:
            monster_manager.attack_monster(self, (new_x, new_y))
            return


        #regarde si il y a un mur ou si le déplacement est ok
        if game_map.is_walkable(new_x, new_y):
            self.x, self.y = new_x, new_y


    
        
   