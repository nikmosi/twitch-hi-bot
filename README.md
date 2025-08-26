# twitch-hi-bot

Simple example bot that greets selected users in chat once per day at most.

## Usage

Run the bot with:

```bash
uv run script.py
```

Enter nicknames in the console to simulate chat messages. If the nickname
matches the watch list, the bot will respond with `catKISS` once per day. The
count resets at 12:00 Moscow time (UTC+3).
