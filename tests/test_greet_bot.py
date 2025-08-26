from datetime import datetime, timedelta, timezone

from bot import GreetBot

MSK = timezone(timedelta(hours=3))


def test_greets_user_once_until_reset():
    first = datetime(2024, 1, 1, 11, 0, tzinfo=MSK)
    bot = GreetBot(["alice"], now=first)
    assert bot.handle_message("alice", first) == "catKISS alice"
    assert bot.handle_message("alice", first + timedelta(minutes=10)) is None
    after_reset = datetime(2024, 1, 1, 12, 1, tzinfo=MSK)
    assert bot.handle_message("alice", after_reset) == "catKISS alice"


def test_ignores_unwatched_user():
    now = datetime(2024, 1, 1, 11, 0, tzinfo=MSK)
    bot = GreetBot(["alice"], now=now)
    assert bot.handle_message("bob", now) is None
