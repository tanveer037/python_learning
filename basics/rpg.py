class Character:
    def __init__(self, name, hp, lvl) -> None:
        self.name = name
        self.hp = hp
        self.level = lvl


class NPC(Character):
    def __init__(self, name, hp, lvl) -> None:
        super().__init__(name, hp, lvl)

    def speak(self):
        print('"I heard there were monsters running around last night!".')

villager = NPC("Bob", 100, 12)
villager.speak()