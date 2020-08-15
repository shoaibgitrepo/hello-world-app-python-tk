from widgets_main.button_hello import button_hello
from widgets_main.button_task import button_task
from widgets_common.button_quit import button_quit
from ui_lib.ui_library import ui, Frame, Root


class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_hello = button_hello(self)
        self.button_task = button_task(self)

        # create all widgets in separate modules
        # import them here until you work on main window of application.
        # create another windows for different operations.
        # define another widgets for another windows

        self.quit = button_quit(self)


root = Root()
main_window = MainWindow(master=root)
main_window.mainloop()
