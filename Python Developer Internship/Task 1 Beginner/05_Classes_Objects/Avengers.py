class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
# Method to display superhero information
    def get_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)
# Method to check whether superhero is a leader
    def is_leader(self):
        if self.name == "Captain America":
            print(self.name, "is the leader of the Avengers.")
        else:
            print(self.name, "is not the leader of the Avengers.")
# Creating six Avengers objects
captain_america = Avenger(
    "Captain America",
    100,
    "Male",
    "Super Strength",
    "Shield"
)
iron_man = Avenger(
    "Iron Man",
    45,
    "Male",
    "Technology",
    "Armor"
)
black_widow = Avenger(
    "Black Widow",
    35,
    "Female",
    "Superhuman",
    "Batons"
)
hulk = Avenger(
    "Hulk",
    40,
    "Male",
    "Unlimited Strength",
    "No Weapon"
)
thor = Avenger(
    "Thor",
    1500,
    "Male",
    "Super Energy",
    "Mjölnir"
)
hawkeye = Avenger(
    "Hawkeye",
    40,
    "Male",
    "Fighting Skills",
    "Bow and Arrows"
)
# List of Avengers
super_heroes = [
    captain_america,
    iron_man,
    black_widow,
    hulk,
    thor,
    hawkeye
]
# Display information about all superheroes
for hero in super_heroes:
    print("\n------------------------")
    hero.get_information()
    hero.is_leader()