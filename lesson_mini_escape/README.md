# Mini Escape Room (30 min taster)

## Goal
Build a tiny text adventure where the player explores rooms, finds an item, and escapes.

## What you need
- Python + VS Code
- This folder only (no other files)

## How to run
1) Open `mini_escape.py` in VS Code.
2) Click Run (or use the play button).
3) Follow the prompts.

## Mini primer (just enough to finish the TODOs)
- **Variable:** a named box that stores a value.
   - Example: `moves = 0`   the 'box' is called 'moves and the value it stores is 0.
- **List:** a collection of items in square brackets.
   - Example: `items = ["key", "note"]`  the box is called items and it contains the list of "key" and "note"
- **Dictionary (dict):** keys mapping to values using `{}`.
   - Example: `room = {"desc": "A hall", "items": ["key"]}`   if you 'look up' "desc" in this dictionary, you'll get "A hall" as the value or 'definition'
- **Accessing dict data:** `room["items"]` gets the list for that key.
- **Checking inventory:** `"key" in state["inventory"]` is `True` if the key is there.
- **Updating a dict value:** `state["turns"] += 1`  this would increase the value of state['turns'] by 3

## Lesson flow (short)
1) **Easy wins (5 mins)**
   - Change the room names and descriptions.
   - Change the item name (key -> something fun).
2) **Make choices (10 mins)**
   - Run the menu loop.
   - Move between rooms.
3) **Add two puzzles (10 mins)**
   - Block the Exit unless the player has the item.
   - Add the drawer code puzzle for a second item (crowbar).
4) **Add a counter (5 mins)**
   - Add a moves counter and print it in the Inventory.
5) **Optional challenge (5 mins)**
   - Add a new room or a second item.

## Quick Fix Table (common errors)
Use the error message and the line number to jump to the problem. Fix ONE thing, run again.
(Much of programming is fixing stuff that goes wrong - it's part of the fun!)

| Error message | What it usually means | What to check |
|---|---|---|
| `SyntaxError: EOL while scanning string literal` | A missing quote | Look for an unclosed " or ' on the line above |
| `SyntaxError: invalid syntax` | A missing colon or bracket | Check `if` / `elif` / `else` lines for `:` |
| `IndentationError: unexpected indent` | Indentation is off | Lines inside `if` or `while` must be indented evenly |
| `NameError: name 'x' is not defined` | Variable name typo | Check spelling and case (Python is picky) |
| `TypeError: can only concatenate str (not "int")` | Mixing text and numbers | Use f-strings: `f"Score: {score}"` |

## How to read errors (30-second guide)
- The **last line** of the error usually says what went wrong.
- The **line number** tells you where to look.
- Fix one thing, run again. Repeat.

## Hints (spoilers)
### Hints by TODO number
- **TODO 1:** Only change text in the room names and `"desc"` strings.
- **TODO 2:** The item list is inside each room. Example: `"items": ["key"]`.
- **TODO 3:** Add a new key in `new_state()` like `"moves": 0`.
- **TODO 4:** Update the item name in `can_move_to_exit()` to match TODO 2.
- **TODO 5:** The drawer gate lives in `can_open_drawer()`.
- **TODO 6:** Use `SECRET_CODE` and update the hint text beside it.
- **TODO 7:** Check for two items with `and`, e.g. `"key" in inv and "crowbar" in inv`.
- **TODO 8:** Increment moves after each menu choice.
- **TODO 9:** Print moves in `show_inventory()`. The indentation should be inline with the if.

General tip: If a menu choice is not working, print the choice to see what it is.

## If you finish early
- Add a riddle item (e.g. note) that hints at a code.
- Add a "choose item" menu so players can pick which item to take.
- Show the moves count in the win message.

### Optional challenges
- **New room:** copy an existing room block in `build_rooms()`, change its name/desc, then add an exit from another room to it.
- **Choose item menu:** change `take_item()` to list items and ask for a number.
- **Moves in win message:** after the win, print `Moves: <number>`.
- **Riddle note:** add `"note"` to a room. If player has it, print a hint in a new menu action.

Have fun. The building is definitely on fire. Probably.
