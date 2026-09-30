class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        zombie.health -= self.damage

    def take_damage(self,zombie):
        self.health -= zombie.damage

class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        self.distance -= 5

    def attack(self, plant):
        plant.health -= self.damage

    def take_damage(self,plant):
        self.health -= plant.damage

plant1 = Plant("CabbagePult", 100, 15)
plant2 = Plant("MelonPult", 100, 45)
zombie1 = Zombie("Conehead", 100, 15, 50)

while plant1.health > 0 and plant2.health > 0:
    if zombie1.distance > 0:
        if plant1.health > 0:
            plant1.attack(zombie1)
            zombie1.take_damage(plant1)
            if zombie1.health <= 0:
                zombie1.move()

        print(plant1.name)
        print(plant1.health)
        print(plant2.name)
        print(plant2.health)
        print(zombie1.name)
        print(zombie1.health)
        print(zombie1.distance)

        if plant2.health > 0:
            plant2.attack(zombie1)
            zombie1.take_damage(plant2)
            if zombie1.health <= 0:
                zombie1.move()

        print(plant1.name)
        print(plant1.health)
        print(plant2.name)
        print(plant2.health)
        print(zombie1.name)
        print(zombie1.health)
        print(zombie1.distance)


    else:
        if plant1.health > 0:
            plant1.attack(zombie1)
            zombie1.take_damage(plant1)
            if zombie1.health <= 0:
                zombie1.move()
            else:
                zombie1.attack(plant1)
                plant1.take_damage(zombie1)

            print(plant1.name)
            print(plant1.health)
            print(plant2.name)
            print(plant2.health)
            print(zombie1.name)
            print(zombie1.health)

            break
    
        if plant2.health > 0:
            plant2.attack(zombie1)
            zombie1.take_damage(plant2)
            if zombie1.health <= 0:
                zombie1.move()
            else:
                zombie1.attack(plant2)
                plant2.take_damage(zombie1)

            print(plant1.name)
            print(plant1.health)
            print(plant2.name)
            print(plant2.health)
            print(zombie1.name)
            print(zombie1.health)