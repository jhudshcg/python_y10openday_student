# Personality Chatbot (30 min taster)

## Goal
Build a simple chatbot that replies based on what the user types.

## What you need
- Python + VS Code
- This folder only

## How to run
1) Open `personality_chatbot.py` in VS Code.
2) Click Run (or use the play button).
3) Chat with the bot.

## Mini primer (just enough to finish the TODOs)
- **Variable:** a named box that stores a value.
   - Example: `counter = 0`   the 'box' is called counter and the value it stores is 0
   - Example: `text = "Live from space, hello!"`   the 'box' is called text and the value it stores is "Live from space, hello!"
- **If rule:** runs code only when a condition is true.
   - Example: `if "hello" in text:`
                `print("hello back!")`   "hello back!" would only print, if "hello" was found in the text variable
- **`in` keyword:** checks if a word appears inside a string.
   - Example: `"music" in text`
- **Normalising input:** make typing consistent.
   - Example: `text = user_text.strip().lower()`   this removes blank spaces from the ends of text and then makes it all lower case
- **Loop:** keeps the chat running.
   - Example: `while True:`
                `print("Are we there yet?")`   this will go on forever...

## Lesson flow (short)
1) **Easy wins (5 mins)**
   - Change the bot name and greeting.
   - Change one response line.
2) **Add rules (10 mins)**
   - Add 2 new keyword rules (e.g. "music", "food").
3) **Loop + counter (10 mins)**
   - Keep chatting until the user types "quit".
   - Track how many messages the user sent.
4) **Optional challenge (5 mins)**
   - Add random responses or a mood meter.

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
- **TODO 1:** Change `BOT_NAME` and `BOT_STYLE` at the top.
- **TODO 2:** Only edit the greeting text inside `greeting()`.
- **TODO 3:** Change the reply string under the hello rule.
- **TODO 4:** Follow the pattern and replace `"keyword"` and the response text.
- **TODO 5:** Update the help line to list your own topics.
- **TODO 6:** Create a counter variable, then add 1 each message.
- **TODO 7:** Print the counter when quitting.

General tip: If a rule never triggers, print `text` to see what it contains.

## If you finish early
- Add a "secret" word that triggers a rare response.
- Make the bot slightly dramatic. Or very dramatic.

### Optional challenges
- **Easier (secret word):** add a new rule using the same pattern as TODO 4.
   - Pattern reminder: `if "yourword" in text: return f"{BOT_NAME}: ..."`
- **Medium (random response):** make a list of replies, then pick one.
   - Hint: `import random` and `random.choice(reply_list)`
- **Medium (mood meter):** create a `mood` variable and change it when certain words appear.
   - Hint: update `mood` before `return`, then use it in the response.

Your bot is not sentient. It just wants you to think it is.
