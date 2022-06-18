from database.database import Database

class Story:

    def __init__(self, title, file, send_count=0):
        self.title = title
        self.file = file
        self.send_count = send_count

        self.database = Database()

    def save(self):
        self.database.insert(
            self.title,
            self.file,
            self.send_count
        )

    def get(self):
        return self.database.find(self.title)

