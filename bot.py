from datetime import datetime, time, timedelta, timezone

MSK = timezone(timedelta(hours=3))


class GreetBot:
    """Greets watched users once per day and resets at 12:00 MSK."""

    def __init__(self, watch_list, now: datetime | None = None):
        self.watch_list = {name.lower() for name in watch_list}
        self.greeted: set[str] = set()
        if now is None:
            now = datetime.now(MSK)
        self.next_reset = self._next_reset_time(now)

    def _next_reset_time(self, now: datetime) -> datetime:
        reset_today = datetime.combine(now.date(), time(12, 0), tzinfo=MSK)
        if now >= reset_today:
            reset_today += timedelta(days=1)
        return reset_today

    def _check_reset(self, now: datetime) -> None:
        if now >= self.next_reset:
            self.greeted.clear()
            self.next_reset = self._next_reset_time(now)

    def handle_message(self, username: str, now: datetime | None = None) -> str | None:
        if now is None:
            now = datetime.now(MSK)
        self._check_reset(now)
        key = username.lower()
        if key in self.watch_list and key not in self.greeted:
            self.greeted.add(key)
            return f"catKISS {username}"
        return None
