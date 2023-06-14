from task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section" #дали е така?

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        else:
            Task.completed = True
            return f"Completed task {task_name}"

    def clean_section(self):
        #completed tasks?
        return f"Cleared {len(self.tasks)} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        [result.append(f"{s.details()}" for s in self.tasks]
        return '\n'.join(result)



task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())




