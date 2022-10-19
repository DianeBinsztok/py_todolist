class ActionMenu:

    def __init__(self):
        self.tasks: list = []

    def add(self):
        from task import Task
        task_name = input("Quel est le nom de votre nouvelle tache ?")
        task_status = False
        self.tasks.append(Task(task_name, task_status))

    def done(self):
        task_to_ckeck = input('Quelle tache souhaitez-vous accomplir ?')
        task_status = True
        self.tasks[int(task_to_ckeck) - 1].status = task_status

    def update(self):
        task_to_update = input('Quelle tâche voulez vous modifier ?')
        new_name = input('Quel est le nouveau nom de votre tâche ?')
        self.tasks[int(task_to_update) - 1].name = new_name

    def list_in_progress(self):
        print('Liste des tâches en cours:')
        number_of_tasks_in_progress = 0
        for count, task in enumerate(self.tasks):
            if not task.status:
                number_of_tasks_in_progress += 1
                print(count + 1, '-', task.name)
        if number_of_tasks_in_progress == 0:
            print('Aucune tâche en cours')

    def list_done(self):
        print('Liste des tâches terminées:')
        number_of_tasks_done = 0
        for count, task in enumerate(self.tasks):
            if task.status:
                number_of_tasks_done += 1
                print(count + 1, '-', task.name)
        if number_of_tasks_done == 0:
            print('Aucune tâche terminée')

    def list_all(self):
        self.list_in_progress()
        self.list_done()

    def user_input(self, user_choice: str):
        choices = {
            'add': self.add,
            'done': self.done,
            'update': self.update,
            'list': self.list_in_progress,
            'list-done': self.list_done,
            'list-all': self.list_all,
        }
        try:
            choices[user_choice]
        except KeyError:
            print("Commande inexistante")
            return self.tasks
        try:
            choices[user_choice]()
        except Exception:
            print("Erreur dans la fonction")
        return self.tasks
