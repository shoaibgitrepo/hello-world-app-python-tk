from widgets_common.button_quit import button_quit
from widgets_about.label_about import label_about
from ui_lib.ui_library import ui, Frame, Root


class AboutWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.label_about = label_about(self, root)
        print("Some description \nAbount your application.")
        self.quit = button_quit(self)


root = Root()
about_window = AboutWindow(master=root)
about_window.mainloop()
