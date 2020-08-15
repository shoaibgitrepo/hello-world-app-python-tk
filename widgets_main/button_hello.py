from ui_lib.ui_library import ui


def button_hello(app):
    app.button_hello = ui.Button(app)
    app.button_hello["text"] = "Hello"
    app.button_hello["command"] = print_hello_world
    app.button_hello.pack(side="top")

    return app.button_hello


def print_hello_world():
    print("hello world!")
