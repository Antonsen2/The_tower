class Fight:

    def attack(self, npc, player, npc_damage):
        npc.hp -= player.ap
        print(f"you attack the {npc.name} with {player.ap} damage")
        player.hp -= npc_damage
        print(f"The {npc.name} attack you back dealing {npc_damage} damage")
        if player.hp < 0:
            player.hp = 0
        print(f"you have {player.hp} hp left and the {npc.name} have {npc.hp} hp left")

    def defend(self, npc, player, npc_damage):

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
