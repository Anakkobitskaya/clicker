from interface_buttons.level import Level
from interface_buttons.name import Name
from interface_buttons.seed import Seed
from interface_buttons.shop_button import ShopButton


class Interface:
    def __init__(self):
        self.seed = Seed()
        self.shop_button = ShopButton()
        self.name = Name()
        self.level = Level()

    def draw(self, sc):
        self.shop_button.draw(sc)