class Task:

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name == self.name:
            return "Name cannot be the same."
        else:
            self.name = new_name
            return self.name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same."
        else:
            self.due_date = new_date
            return self.due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if not self.comments[comment_number]:
            return "Cannot find comment."
        else:
            self.comments[comment_number] = new_comment
            result = [c for c in self.comments]
            return f"{', '.join(result)}"

    def details(self):
        for _ in self.comments:
            return f"Name: {self.name} - Due Date: {self.due_date}"


