class Note():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}\n{self.content}\n"