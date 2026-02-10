"""Mini Escape Room - 30 min taster

Run this file and follow the TODOs.
Keep it small, keep it fun.
"""

# -------------------------
# EASY WINS (edit these first, then look for the other TODOs below)
# -------------------------
GAME_TITLE = "College Escape: Mini Edition"
START_ROOM = "Lobby"
WIN_ROOM = "Exit"
# TODO 6 (practice): Change this number and update the hint in try_open_drawer().
SECRET_CODE = 314

# TODO 1: Change the room names and descriptions.
# Tip: Keep it short and funny. Run the program and check the new text prints.

def build_rooms():
    return {
        "Lobby": {
            "desc": "You wake up in the lobby. A sign says: 'No running'. You ignore it.",
            "exits": {"east": "Storage", "north": "Exit"},
            # TODO 2 (easy win): Replace "key" inside the list with your own item.
            # Example: ["key"] -> ["pass"]
            # Run and check the item name in the room display.
            "items": ["key"],
        },
        "Storage": {
            "desc": "A tiny storage room. Dusty boxes. A suspicious smell.",
            "exits": {"west": "Lobby"},
            "items": [],
        },
        "Exit": {
            "desc": "A heavy door with a keypad. It looks unimpressed.",
            "exits": {"south": "Lobby"},
            "items": [],
        },
    }


# -------------------------
# STATE
# -------------------------

def new_state():
    return {
        "room": START_ROOM,
        "inventory": [],
        # TODO 3 (practice): Add a moves counter that starts at 0.
        # Hint: add a new key/value pair like "akeyforanumber": 0
        # Run: no visible change yet (you will use it in TODO 8/9).
    }


# -------------------------
# HELPERS
# -------------------------

def show_room(rooms, state):
    room = rooms[state["room"]]
    print("\n" + "=" * 40)
    print("ROOM:", state["room"])
    print(room["desc"])

    items = room["items"]
    if items:
        print("You can see:", ", ".join(items))
    else:
        print("You can see: nothing useful")

    exits = ", ".join(room["exits"].keys())
    print("Exits:", exits)


def show_inventory(state):
    print("\nINVENTORY")
    if not state["inventory"]:
        print("(empty)")
    else:
        print(", ".join(state["inventory"]))

    # TODO 9 (practice): If you added a moves counter, print it here.
    # Example: print("Moves:", state["nameofmoveskey"])   
    # replace nameofmoveskey with the key you used in new_state() for TODO 3.
    # Think about where the print statement should be indented to show for every inventory check.
    # Run: open Inventory and check the number changes.


def ask_int(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Please type a whole number.")
            continue
        if value < min_value or value > max_value:
            print(f"Please type a number from {min_value} to {max_value}.")
            continue
        return value


def can_move_to_exit(state):
    # TODO 4 (puzzle): Match the item name you used in TODO 2.
    # Go to build_rooms() and find the "items": ["key"] list.
    # If you changed "key" to "pass", update the check below to "pass".
    # The player must have the item before they can enter the Exit.
    # Run: take the item, then try the Exit. It should unlock.
    # TODO 7 (challenge): Require TWO items to escape (your item + the drawer item).
    # Pattern: return "item1" in state["inventory"] and "item2" in state["inventory"]
    # Run: you should need the drawer item before you can leave.
    return "key" in state["inventory"]


def can_open_drawer(state):
    # TODO 5 (practice): This is a second gate.
    # Requirement: player must have the key before they can open the drawer.
    # Example: return "thingtocheck" in state["inventory"].  
    # HINT: "thingtocheck" above should be the name of the item you want to require.
    # Run: try the drawer before taking the item (should block).
    return True # replace True with the check for the required item.


# -------------------------
# ACTIONS
# -------------------------

def move_player(rooms, state):
    room = rooms[state["room"]]
    exits = list(room["exits"].keys())

    print("\nMove where?")
    for i, direction in enumerate(exits, start=1):
        dest = room["exits"][direction]
        print(f"{i}) {direction} -> {dest}")

    choice = ask_int("Choose: ", 1, len(exits))
    direction = exits[choice - 1]
    destination = room["exits"][direction]

    if destination == WIN_ROOM and not can_move_to_exit(state):
        print("The Exit is locked. You need the item first.")
        return

    state["room"] = destination


def take_item(rooms, state):
    room = rooms[state["room"]]
    if not room["items"]:
        print("Nothing to take here.")
        return

    # Simple: take the first item
    item = room["items"].pop(0)
    state["inventory"].append(item)
    print("Picked up:", item)


def try_open_drawer(state):
    # TODO 6 (practice): Customize the drawer puzzle.
    # Change SECRET_CODE (at the top of this file) and update the hint text below.
    # Run: enter the code and check that the crowbar appears in inventory.
    if not can_open_drawer(state):
        print("The drawer is locked. You might need a key first.")
        return

    print("There is a locked drawer with a 3-digit code.")
    print("(Hint: you wouldn't want to take a bite out of this pie.)")
    code = ask_int("Enter code: ", 0, 999)
    if code == SECRET_CODE:
        if "crowbar" not in state["inventory"]:
            state["inventory"].append("crowbar")
        print("Drawer opens. You found a crowbar.")
    else:
        print("Wrong code. The drawer beeps sadly.")


# -------------------------
# MAIN LOOP
# -------------------------

def show_menu():
    print("\nACTIONS")
    print("1) Move")
    print("2) Look")
    print("3) Take")
    print("4) Inventory")
    print("5) Drawer")
    print("6) Quit")
    return ask_int("Choose: ", 1, 6)


def main():
    rooms = build_rooms()
    state = new_state()

    print("=" * 40)
    print(GAME_TITLE)
    print("Goal: find the item and escape.")
    print("=" * 40)

    show_room(rooms, state)

    while True:
        if state["room"] == WIN_ROOM:
            print("\nYOU ESCAPED. Nice." )
            break

        choice = show_menu()
        # TODO 8 (practice): If you added a moves counter, increase it here. It should increase by 1.
        # Example: state["moves"] += 22    # replace "moves" with the key you used in new_state() for TODO 3.
        # Run: take a few actions, then check TODO 9 output.
        if choice == 1:
            move_player(rooms, state)
        elif choice == 2:
            show_room(rooms, state)
        elif choice == 3:
            take_item(rooms, state)
        elif choice == 4:
            show_inventory(state)
        elif choice == 5:
            try_open_drawer(state)
        elif choice == 6:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()

# -------------------------
# OPTIONAL CHALLENGES (if you finish early)
# -------------------------
# 1) Add a new room with a new item and a new exit.
# 2) Add a riddle note that hints at the secret code.
# 3) Add a "take item" menu that lets you choose which item to pick up.
