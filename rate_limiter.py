import time

class RateLimiter:
    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window = window_seconds
        self.requests = {}

    def allow(self, client_id):
        now = time.time()
        if client_id not in self.requests:
            self.requests[client_id] = []

        timestamps = [t for t in self.requests[client_id] if now - t < self.window]
        self.requests[client_id] = timestamps

        if len(timestamps) < self.limit:
            self.requests[client_id].append(now)
            return True
        return False
