class Task:
    def __init__(self, _id, title, completed):
        self.id = int(_id)
        self.title = str(title)
        self.completed = bool(completed)

    pass
