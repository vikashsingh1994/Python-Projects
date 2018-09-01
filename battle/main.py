import  random

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Creating Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 30, 800, "black")

#Creating White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

#Create Some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, thunder, curaga]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

#player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

#Instantiate People
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 180, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Imp  :", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Magus:", 18200, 701, 525, 25, enemy_spells, [])
enemy3 = Person("Imp  :", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.OKBLUE + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("===========================")
    print("\n\n")
    print(bcolors.BOLD + bcolors.OKGREEN + "NAME                     HP                                          MP" + bcolors.ENDC)
    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.enemy_stats()

    print("\n")

    for player in players:

        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name + "for ", dmg, "points of damage")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("     Choose magic: "))-1
            if magic_choice == -1:
                continue

            """magic_dmg = player.generate_spell_damage(magic_choice)
            spell = player.get_spell_name(magic_choice)
            cost = player.get_spell_mp_cost(magic_choice)"""

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot Enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to "
                      + enemies[enemy].name + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Items: ")) - 1
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if player.items[item_choice]["quantity"] <= 0:
                print(bcolors.FAIL + "\n" + "None Left...." + bcolors.ENDC)
                continue

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), "HP" + bcolors.ENDC)

            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals" + str(item.prop) + " points of damage to "
                      + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ","") + "has died.")
                    del enemies[enemy]

        elif index == 3:
            print("\n")
            for player in players:
                player.get_stats()
            print("\n")
            for enemy in enemies:
                enemy.enemy_stats()
            continue

    # Check if battle is over
    defeated_players = 0
    defeated_enemies = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False

    #Check if Enemy won
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your Enemies has defeated you!" + bcolors.ENDC)
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        # Chose attack
        if enemy_choice == 0:
            target = random.randrange(0, 3)

            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ","") + " attack " + players[target].name.replace(" ","") + " for ", enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + " for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ","") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to "
                      + players[target].name + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ","") + " has died!")
                    del players[target]







