class Action:
    def __init__(self, user_id, timestamp):
        self.user_id = user_id
        self.timestamp = timestamp

    def display_action(self):
        return f"User ID: {self.user_id} performed an action at {self.timestamp}"