# controller.py
"""class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)
"""

from model import Data
import view


def showAll():
    # gets list of all Person objects
    data_in_db = data.getAll()
    # calls view
    return view.showAllView(data_in_db)


def start():
    view.startView()
    show_trends()
    view.endView()


if __name__ == "__main__":
    # running controller function
    start()
