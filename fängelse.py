import sys
import time

# Funktion för att skriva text långsamt
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Anpassa för snabbare eller långsammare text
    print()


def main():
    slow_print("\nVälkommen till det magiska slottet! Du är inlåst i en fängelsehåla och måste hitta en väg ut.")
    show_instructions()
    start_room()


def show_instructions():
    slow_print("\nInstruktioner:")
    slow_print("1. Du kommer att få olika val under spelets gång.")
    slow_print("2. Ange det nummer eller den text som matchar ditt val.")
    slow_print("3. Ditt mål är att fly från slottet genom att fatta rätta beslut.")


def start_room():
    slow_print("\nDu är i en fängelsehåla. Rummet är kallt och mörkt.")
    slow_print("Vad vill du göra?")
    slow_print("1. Inspektera cellen")
    slow_print("2. Försök öppna dörren")
    slow_print("3. Visa instruktionerna igen")

    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == "1":
        inspect_cell()
    elif choice == "2":
        try_open_door()
    elif choice == "3":
        show_instructions()
        start_room()
    else:
        slow_print("Ogiltigt val. Försök igen.")
        start_room()


def inspect_cell():
    slow_print("\nDu hittar en nyckel under sängen!")
    slow_print("1. Ta nyckeln och försök öppna dörren")
    slow_print("2. Undersök vidare")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        slow_print("\nDu använder nyckeln och lyckas låsa upp dörren.")
        corridor()
    elif choice == "2":
        slow_print("\nDu hittar inget mer av värde.")
        start_room()
    else:
        slow_print("Ogiltigt val. Försök igen.")
        inspect_cell()


def try_open_door():
    slow_print("\nDörren är låst. Du behöver en nyckel.")
    start_room()


def corridor():
    slow_print("\nDu är nu i en korridor. Det finns två vägar att välja:")
    slow_print("1. Gå vänster")
    slow_print("2. Gå höger")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        friendly_guard()
    elif choice == "2":
        color_puzzle()
    else:
        slow_print("Ogiltigt val. Försök igen.")
        corridor()


def friendly_guard():
    slow_print("\nDu möter en magisk väktare som ler och ger dig en ledtråd.")
    slow_print("Ledtråd: Nyckeln till friheten är färgens hemlighet!")
    corridor()


def color_puzzle():
    slow_print("\nDu står framför en dörr med tre knappar: röd, grön och blå.")
    slow_print("Vilken färg vill du trycka på?")

    choice = input("Välj färg (röd/grön/blå): ")

    if choice.lower() == "grön":
        slow_print("\nDu trycker på den gröna knappen och dörren öppnas!")
        final_room()
    else:
        slow_print("\nFel knapp! Försök igen.")
        color_puzzle()


def final_room():
    slow_print("\nGrattis! Du har nått det sista rummet och lyckats fly från det magiska slottet.")
    slow_print("Tack för att du spelade!")
    sys.exit()


if __name__ == "__main__":
    main()

