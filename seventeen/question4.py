from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the new request's timestamp to the queue
        self.requests.append(t)

        # Remove requests that are outside the time frame
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of requests within the time frame
        return len(self.requests)
