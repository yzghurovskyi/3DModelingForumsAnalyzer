
class Message:
    def __init__(self, author: str, date: str, text: str, topic_id: str):
        self.author = author
        self.date = date
        self.text = text
        self.topic_id = topic_id
