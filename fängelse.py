import random

# ======= Player Class =======
class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.position = "Cellen"

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("\nDin ryggsäck innehåller:")
        for item in self.inventory:
            print(f"- {item}")
        if not self.inventory:
            print("(Inget i ryggsäcken än!)")

# ======= Room Class =======
class Room:
    def __init__(self, name, description, options, puzzle=None, enemy=None):
        self.name = name
        self.description = description
        self.options = options
        self.puzzle = puzzle
        self.enemy = enemy
        self.puzzle_solved = False

    def enter_room(self, player):
        print(f"\nDu är i {self.name}.")
        print(self.description)
        
        if self.enemy:
            self.battle(player)

        if self.puzzle and not self.puzzle_solved:
            self.solve_puzzle(player)

        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

        choice = input("Vad vill du göra? ")
        return choice

    def solve_puzzle(self, player):
        print(f"\nPussel: {self.puzzle['question']}")
        answer = input("Svar: ")
        if answer.lower() == self.puzzle['answer'].lower():
            print(self.puzzle['success_message'])
            if 'reward' in self.puzzle:
                player.add_item(self.puzzle['reward'])
                print(f"Du fick {self.puzzle['reward']}!")
            self.puzzle_solved = True
        else:
            print(self.puzzle['failure_message'])

    def battle(self, player):
        print(f"\nEn {self.enemy['name']} blockerar vägen!")
        while player.health > 0 and self.enemy['health'] > 0:
            attack = random.randint(5, 15)
            self.enemy['health'] -= attack
            print(f"Du träffade {self.enemy['name']} och gjorde {attack} skada!")

            if self.enemy['health'] <= 0:
                print(f"Du besegrade {self.enemy['name']}!")
                break

            enemy_attack = random.randint(5, 15)
            player.health -= enemy_attack
            print(f"{self.enemy['name']} träffade dig och gjorde {enemy_attack} skada!")

        if player.health <= 0:
            print("\nDu blev besegrad...")
            exit()

# ======= Game Data =======
rooms = {
    "Cellen": Room(
        name="Cellen",
        description="Du vaknar i en kall, mörk cell. Dörren är låst.",
        options=["Inspektera cellen", "Försök öppna dörren"],
        puzzle={
            "question": "Du hittar en låda med ett kodlås: Vad är 2 + 2?",
            "answer": "4",
            "success_message": "Låset klickar till och lådan öppnas! Du hittar en nyckel.",
            "failure_message": "Fel svar. Lådan förblir låst.",
            "reward": "Nyckel"
        }
    ),
    "Korridoren": Room(
        name="Korridoren",
        description="En lång, mörk korridor sträcker sig åt höger och vänster.",
        options=["Gå höger", "Gå vänster"],
        enemy={
            "name": "Leksakssoldat",
            "health": 30
        }
    ),
    "Magiskt förråd": Room(
        name="Magiskt förråd",
        description="Ett rum fyllt med glittrande föremål och magiska ting.",
        options=["Ta ett magiskt föremål", "Gå tillbaka till korridoren"],
        puzzle={
            "question": "Vilken färg blandar du för att få lila? (Röd, blå, grön)",
            "answer": "Röd och blå",
            "success_message": "Du löste pusslet och ett föremål framträder!",
            "failure_message": "Fel svar. Försök igen senare.",
            "reward": "Magisk nyckel"
        }
    ),
    "Dolda Trädgården": Room(
        name="Dolda Trädgården",
        description="En vacker, hemlig trädgård med mystiska växter och statyer.",
        options=["Undersök statyerna", "Gå vidare till nästa rum"],
        puzzle={
            "question": "Statyn frågar: 'Jag har grenar men inga löv, vad är jag?'.",
            "answer": "Ett träd",
            "success_message": "Statyns ögon lyser upp och en hemlig väg öppnas!",
            "failure_message": "Statyn förblir tyst."
        }
    ),
    "Väktarens Kammare": Room(
        name="Väktarens Kammare",
        description="Ett mörkt rum där en mäktig väktare väntar på att pröva dig.",
        options=["Utmana väktaren", "Gå tillbaka till trädgården"],
        enemy={
            "name": "Mäktig Väktare",
            "health": 50
        }
    ),
    "Frihetens Port": Room(
        name="Frihetens Port",
        description="En massiv port med lysande symboler som leder till frihet.",
        options=["Använd Magisk nyckel", "Gå tillbaka till Väktarens Kammare"]
    )
}

# ======= Game Logic =======
def show_instructions():
    try:
        with open("instructions.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Instruktionsfilen hittades inte.")

def main_menu():
    print("\n=== Fängelsesspelet ===")
    print("1. Starta nytt spel")
    print("2. Visa instruktioner")
    print("3. Avsluta")
    
    choice = input("Välj ett alternativ: ")
    return choice

def game_loop(player):
    while True:
        current_room = rooms[player.position]
        choice = current_room.enter_room(player)

        if player.position == "Cellen":
            if choice == "1":
                print("Du hittar en låda med ett kodlås.")
            elif choice == "2":
                if "Nyckel" in player.inventory:
                    print("Du låser upp dörren och går vidare till korridoren.")
                    player.position = "Korridoren"
                else:
                    print("Dörren är låst. Du behöver en nyckel.")

        elif player.position == "Korridoren":
            if choice == "1":
                print("Du går höger och möter en fiende!")
                current_room.battle(player)
            elif choice == "2":
                print("Du går vänster och hittar en dörr som leder till det magiska förrådet.")
                player.position = "Magiskt förråd"

        elif player.position == "Magiskt förråd":
            if choice == "1":
                print("Du plockar upp ett magiskt föremål.")
                if not current_room.puzzle_solved:
                    print("Du måste lösa pusslet först!")
                else:
                    player.add_item("Magiskt föremål")
            elif choice == "2":
                print("Du går vidare till den dolda trädgården.")
                player.position = "Dolda Trädgården"

        elif player.position == "Dolda Trädgården":
            if choice == "1":
                print("Du undersöker statyerna.")
            elif choice == "2":
                print("Du går vidare till Väktarens Kammare.")
                player.position = "Väktarens Kammare"

        elif player.position == "Väktarens Kammare":
            if choice == "1":
                print("Du utmanar väktaren!")
                current_room.battle(player)
            elif choice == "2":
                print("Du går tillbaka till den dolda trädgården.")
                player.position = "Dolda Trädgården"

        elif player.position == "Frihetens Port":
            if choice == "1":
                if "Magisk nyckel" in player.inventory:
                    print("Du använder den magiska nyckeln och porten öppnas! Du är fri!")
                    break
                else:
                    print("Du behöver den magiska nyckeln för att öppna porten.")
            elif choice == "2":
                print("Du går tillbaka till Väktarens Kammare.")
                player.position = "Väktarens Kammare"

        else:
            print("Ogiltigt val. Försök igen.")

# ======= Main Program =======
player = Player()

while True:
    choice = main_menu()

    if choice == "1":
        game_loop(player)
    elif choice == "2":
        show_instructions()
    elif choice == "3":
        print("Hejdå!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
