from ui_lib.ui_library import ui


def button_task(app):
    app.button_task = ui.Button(app)
    app.button_task["text"] = "Task"
    app.button_task["command"] = perform_task
    app.button_task.pack(side="top")

    return app.button_task


def perform_task():
    # Perform some task here...
    print("Perform some task here...")
