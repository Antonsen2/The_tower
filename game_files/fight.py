
from game_files.utils import item_creator


class Fight:

    def battle(self, player, npc):
        if npc:
            print("You engage the enemy, you can attack the enemy or you can defend yourself from their attack")
            while player.hp > 0 and npc.hp > 0:
                damage_reduction = 100/(player.armor + 100)
                npc_damage = npc.ap * damage_reduction
                command = input("What would you like to do? ")

                if len(command) > 0:
                    match command.lower().split():
                        case ["attack"]:
                            self.attack(npc, player, npc_damage)
                        case ["defend"]:
                            self.defend(npc, player, npc_damage)

                if npc.hp <= 0:
                    print("Congratulations! You have defeated the boss")
                    self.boss_drop(player, npc)


    @staticmethod
    def boss_drop(player, npc):
        monster_drop = []
        if npc.drop:
            print(f"The {npc.name} dropped the following:")
            for item in npc.drop:
                monster_drop.append(item_creator(item))
        for item in monster_drop:
            print(">", item.description)
            player.inventory.append(item)
        print("the items have been added to your inventory")

    @staticmethod
    def attack(npc, player, npc_damage):
        npc.hp -= player.ap
        print(f"you attack the {npc.name} with {int(player.ap)} damage")
        player.hp -= npc_damage
        print(f"The {npc.name} attack you back dealing {int(npc_damage)} damage")
        if player.hp < 0:
            player.hp = 0
        if npc.hp < 0:
            npc.hp = 0

        print(f"you have {int(player.hp)} hp left and the {npc.name} have {npc.hp} hp left")

    @staticmethod
    def defend(npc, player, npc_damage):
        match npc_damage:
            case 0:
                print(f"The skeleton completely misses you but you hit them for {player.ap}")
                npc.hp -= player.ap
            case 1 | 2:
                print(f"You blocked the attack and counter dealing {npc_damage} damage back to the {npc.name}")
                npc.hp += npc_damage
            case 3 | 4:
                print(f"You partially stop the enemy attack they hit you for {npc_damage} and you reflect back "
                      f"{npc_damage} damage to the {npc.name} ")
                player.hp -= npc_damage
                npc.hp -= npc_damage
        if player.hp < 0:
            player.hp = 0
        print(f"you have {player.hp} hp left and the {npc.name} have {npc.hp} hp left")
