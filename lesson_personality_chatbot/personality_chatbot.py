"""Personality Chatbot - 30 min taster

Run this file and follow the TODOs.
"""

# -------------------------
# EASY WINS (edit these first)
# -------------------------
# TODO 1: Change the bot name and style.
# Run: the greeting should show your new name/style.
BOT_NAME = "Byte"
BOT_STYLE = "friendly"  # try: friendly, dramatic, sleepy


def greeting():
    # TODO 2: Change the greeting message.
    # Run: you should see your new greeting at the start.
    print(f"{BOT_NAME}: Hey! I am {BOT_NAME}, a {BOT_STYLE} chatbot.")
    print(f"{BOT_NAME}: Type 'quit' to leave.")


def respond(user_text):
    """Return a response based on the user text."""

    # Normalise input so it is easier to match.
    text = user_text.strip().lower()

    # TODO 3 (easy win): Change one response.
    # Run: type the trigger word and check the new reply.
    if "hello" in text or "hi" in text:
        return f"{BOT_NAME}: Hello human. I have been expecting you."

    # TODO 4 (practice): Add 2 new keyword rules here.
    # Pattern:
    # if "keyword" in text:
    #     return f"{BOT_NAME}: response about keyword"
    # Run: type your keywords to test each rule.

    if "help" in text:
        # TODO 5 (practice): Update the help line to match YOUR keywords.
        # Keep it short and list the topics you added above.
        return f"{BOT_NAME}: Try asking about topic1, topic2, or topic3."

    if "joke" in text:
        return f"{BOT_NAME}: I would tell you a UDP joke, but you might not get it."

    # Default response
    return f"{BOT_NAME}: Interesting. Tell me more."


def main():
    print("=" * 40)
    print("PERSONALITY CHATBOT")
    print("=" * 40)
    greeting()

    # TODO 6 (practice): Add a message counter that starts at 0.
    # Hint: make a variable like counter = 0
    # Run: you will print it when the user quits (see TODO 7).

    # TODO 7 (practice): Keep chatting until the user types "quit".
    # Hint: use a while loop and check the input.
    while True:
        user_text = input("You: ")
        if user_text.strip().lower() == "quit":
            # TODO 7 (continued): Print the message counter in the goodbye.
            # Example: "You sent X messages." (use your counter variable)
            print(f"{BOT_NAME}: Bye! I will miss your keystrokes.")
            break

        # TODO 6 (continued): Increase your counter by 1 here.
        reply = respond(user_text)
        print(reply)


if __name__ == "__main__":
    main()

# -------------------------
# OPTIONAL CHALLENGES (if you finish early)
# -------------------------
# 1) Add a message counter (print how many messages were sent).
# 2) Add random responses for the default case (import random).
# 3) Add a "mood" variable that changes based on certain words.
