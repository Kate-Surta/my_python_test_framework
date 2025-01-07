from tests.Action import Action


class Comment(Action):
    comment_schema = {
        "type": "object",
        "properties": {
            "postId": {"type": "integer"},
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["postId", "id", "name", "email", "body"],
    }

    def __init__(self, user_id, timestamp, postId, comment_id, name, email, body):
        super().__init__(user_id, timestamp)
        self.postId = postId
        self.comment_id = comment_id
        self.name = name
        self.email = email
        self.body = body

    # Override display_action method
    def display_action(self):
        return f"Comment by {self.name} (email: {self.email}) on post ID {self.postId}: {self.body}"
