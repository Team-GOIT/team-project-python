class Note():
    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags

    def get_tags_label(self):
        if len(self.tags) > 0:
            return ', '.join(self.tags)
        else:
            return 'No tags'

    def get_formatted(self):
        return f"Title: {self.title}\nContent: {self.content}\nTags: {self.get_tags_label()}\n"