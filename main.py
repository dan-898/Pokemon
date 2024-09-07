import random


# Pokemon class representing each Pokemon's attributes and behaviors
class Pokemon:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_defeated(self):
        return self.health == 0

    def __str__(self):
        return f"{self.name} (HP: {self.health}, Attack Power: {self.attack_power})"


# Player class to manage player actions
class Player:
    def __init__(self, name):
        self.name = name
        self.main_pokemon = None
        self.pokemons = []

    def choose_pokemon(self, pokemons):
        print(f"{self.name}, select your Pokemon:")
        for idx, pokemon in enumerate(pokemons):
            print(f"{idx + 1}. {pokemon}")
        choice = int(input("Enter the number of the Pokemon you want to choose: ")) - 1
        self.main_pokemon = pokemons[choice]
        print(f"{self.name} chose {self.main_pokemon.name}!")

    def change_pokemon(self, pokemons):
        print(f"{self.name}, you can change your Pokemon:")
        self.choose_pokemon(pokemons)


# Battle class to manage turn-based combat
class Battle:
    def __init__(self, player_pokemon, opponent_pokemon):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

    def start(self):
        print("The battle begins!")
        print(f"{self.player_pokemon.name} vs {self.opponent_pokemon.name}")
        while not self.player_pokemon.is_defeated() and not self.opponent_pokemon.is_defeated():
            self.player_turn()
            if self.opponent_pokemon.is_defeated():
                print(f"{self.opponent_pokemon.name} has been defeated!")
                break
            self.opponent_turn()
            if self.player_pokemon.is_defeated():
                print(f"{self.player_pokemon.name} has been defeated!")
                break

    def player_turn(self):
        print(f"{self.player_pokemon.name}'s turn!")
        self.player_pokemon.attack(self.opponent_pokemon)
        self.show_health()

    def opponent_turn(self):
        print(f"{self.opponent_pokemon.name}'s turn!")
        self.opponent_pokemon.attack(self.player_pokemon)
        self.show_health()

    def show_health(self):
        print(
            f"{self.player_pokemon.name} (HP: {self.player_pokemon.health}) | {self.opponent_pokemon.name} (HP: {self.opponent_pokemon.health})")


# Game class to manage the main menu and overall flow
class Game:
    def __init__(self):
        self.pokemons = [
            Pokemon("Pikachu", 100, 15),
            Pokemon("Charmander", 120, 12),
            Pokemon("Bulbasaur", 110, 14),
            Pokemon("Squirtle", 130, 10),
            Pokemon("Jigglypuff", 90, 18)
        ]
        self.player = Player("Ash")
        self.opponent_pokemon = random.choice(self.pokemons)

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Choose Pokemon")
            print("2. Change Pokemon")
            print("3. Start Battle")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.player.choose_pokemon(self.pokemons)
            elif choice == '2':
                if self.player.main_pokemon:
                    self.player.change_pokemon(self.pokemons)
                else:
                    print("You need to choose a Pokemon first!")
            elif choice == '3':
                if self.player.main_pokemon:
                    self.initiate_battle()
                else:
                    print("You need to choose a Pokemon first!")
            elif choice == '4':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def initiate_battle(self):
        print(f"A wild {self.opponent_pokemon.name} appeared!")
        battle = Battle(self.player.main_pokemon, self.opponent_pokemon)
        battle.start()


# Main game loop
if __name__ == "__main__":
    game = Game()
    game.main_menu()
