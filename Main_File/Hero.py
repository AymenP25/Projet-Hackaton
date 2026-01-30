class Hero:
    def __init__(self, x, y):  
        #On définit les caractéristiques principales de notre personnage
        self.x = x
        self.y = y
        self.hp = 100
        self.strengh = 16
        self.gold = 0   
        self.message = "Bienvenue dans le donjon !"

    def move(self, dx, dy, game_map, items, monsters, monster_manager):
        new_x, new_y = self.x + dx, self.y + dy
       
        #regarde si le héros se bat
        if (new_x, new_y) in monsters:
            monster_manager.attack_monster(self, (new_x, new_y))
            return

        #regarde si il y a un mur ou si le déplacement est ok
        if game_map.is_walkable(new_x, new_y):
            self.x, self.y = new_x, new_y
        
   