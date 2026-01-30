#premiers imports
import os
import sys 
import Hero
import map
import monstre

def main():
    game_map = map.GameMap(20,10, 4)
    hero = Hero.Hero(1,1)
    monster_manager = monstre.Monster()

    while hero.hp > 0:
        game_map.display(hero, monster_manager)
        monster_manager.avancer_monstres(game_map,hero)

       
        action = input("Z (Haut), S (Bas), Q (Gauche), D (Droite) : ").upper()
       
        if action == "Z":
            hero.move(0, -1, game_map, monster_manager.monsters, monster_manager)

        elif action == "S":
            hero.move(0, 1, game_map, monster_manager.monsters, monster_manager)

        elif action == "Q":
            hero.move(-1, 0, game_map, monster_manager.monsters, monster_manager)

        elif action == "D":
            hero.move(1, 0, game_map, monster_manager.monsters, monster_manager)
        

                                      
main()