from ui_lib.ui_library import ui


def label_about(app, root):
    app.label_about = ui.Label(
        root, text="Some description About application...")
    app.label_about.pack()

    return app.label_about
