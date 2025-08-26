from bot import GreetBot

WATCH_LIST = ["alice", "bob"]


def main() -> None:
    bot = GreetBot(WATCH_LIST)
    print("Type nicknames, one per line. Press Ctrl-D to exit.")
    try:
        while True:
            name = input().strip()
            if not name:
                continue
            response = bot.handle_message(name)
            if response:
                print(response)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
