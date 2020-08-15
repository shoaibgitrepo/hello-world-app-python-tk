import tkinter as ui


def button_quit(app):
    app.quit = ui.Button(app, text="QUIT", fg="red",
                         command=app.master.destroy)
    app.quit.pack(side="bottom")

    return app.quit
