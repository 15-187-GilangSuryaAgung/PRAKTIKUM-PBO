import random

class Robot:
    def __init__(self, name, hp, attack, defense, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy

    def attack_enemy(self, enemy):
        if random.randint(1, 100) <= self.accuracy:
            damage = max(0, self.attack - enemy.defense)
            enemy.hp -= damage
            print(f"\n🔥 {self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"\n⚠️ {self.name} gagal menyerang {enemy.name}!")

    def is_defeated(self):
        return self.hp <= 0

    def display_status(self):
        return f"{self.name} [HP: {self.hp} | ATK: {self.attack} | DEF: {self.defense}]"


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play(self):
        while not (self.robot1.is_defeated() or self.robot2.is_defeated()):
            print(f"\nRound-{self.round} {'='*50}")
            print(self.robot1.display_status())
            print(self.robot2.display_status())

            for robot in [self.robot1, self.robot2]:
                action = self.get_action(robot)
                
                if action == 1:
                    enemy = self.robot2 if robot == self.robot1 else self.robot1
                    robot.attack_enemy(enemy)
                elif action == 2:
                    robot.defense += 2  # Meningkatkan pertahanan sementara
                    print(f"\n🛡️ {robot.name} memilih bertahan, DEF naik menjadi {robot.defense}!")
                elif action == 3:
                    print(f"\n🏳️ {robot.name} menyerah! {self.get_enemy(robot).name} menang!")
                    return

            self.round += 1

        winner = self.robot1 if self.robot2.is_defeated() else self.robot2
        print(f"\n🏆 {winner.name} MENANG!")

    def get_action(self, robot):
        while True:
            try:
                print("\n1. Attack  2. Defense  3. Giveup")
                action = int(input(f"{robot.name}, pilih aksi: "))
                if action in [1, 2, 3]:
                    return action
            except ValueError:
                pass
            print("⚠️ Pilihan tidak valid! Coba lagi.")

    def get_enemy(self, robot):
        return self.robot2 if robot == self.robot1 else self.robot1


# Inisialisasi robot
robot1 = Robot("Atreus", hp=500, attack=50, defense=5, accuracy=80)
robot2 = Robot("Daedalus", hp=700, attack=40, defense=8, accuracy=70)

# Mulai permainan
game = Game(robot1, robot2)
game.play()