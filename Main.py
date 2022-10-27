from TasksList import TasksList
from Exceptions import InvalidCommandException, NotImplementedException
from Interface import Interface

class Main:

    def __init__(self):
        pass

    def launch_todolist(self):
        list_tasks = TasksList()
        user_input = ""
        interface = Interface()
        while user_input != "quit":
            interface.print_menu()
            user_input = input("Please enter your command :")
            list_tasks = self.do_action(list_tasks, user_input, interface)
        interface.print("Goodbye")
        interface.print('╭∩╮(◉_◉)╭∩╮')


    def do_action(self, list_tasks, user_input, interface):
        actions = {
            "add": ("add new task", "add", list_tasks.add_task),

            "done": ("close task", "done", list_tasks.close_task),
            #
            "update": ("amend task name", "update", list_tasks.update_task),
            #
            "list": ("list pending tasks", "list", list_tasks.list_pending_tasks),
            #
            "list-done": ("list closed tasks", "list-done", list_tasks.list_done_tasks),
            #
            "list-all": ("list all tasks", "list-all", list_tasks.list_all_tasks),
        }
        try:
            actions.get(user_input)[2](list_tasks, interface)
        except TypeError as e:
            try:
                raise InvalidCommandException
            except InvalidCommandException as error:
                interface.print("commande invalide")
        except NotImplementedException as err:
            interface.print("coucou, c'est pas bon")



        finally:
            pass
        return list_tasks


if __name__ == "__main__":
    m = Main()
    m.launch_todolist()
