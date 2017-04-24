from page_objects import PageObject, PageElement


class MainPage(PageObject):
    level_menu_opened = False
    level_menu_created = False
    css_input = PageElement(css='input.input-strobe')
    level_text_span = PageElement(css='span.level-text')
    instruction_h2 = PageElement(css='h2.order')
    enter_button = PageElement(css='div.enter-button')

    level_menu = PageElement(
        xpath='//div[@class="level-menu-toggle-wrapper"]')

    def __init__(self, webdriver, root_uri=None):
        super(MainPage, self).__init__(webdriver, root_uri)
        # hack to initialize all the menu items
        self.open_level_menu()
        self.close_level_menu()

    def ensure_menu_created(self):
        if not self.level_menu_created:
            self.open_level_menu()
            self.close_level_menu()

    def open_level_menu(self):
        if not self.level_menu_opened:
            self.level_menu.click()
            self.level_menu_opened = True
            self.level_menu_created = True

    def close_level_menu(self):
        if self.level_menu_opened:
            self.level_menu.click()
            self.level_menu_opened = False

    def get_level_link(self, level_number):
        return PageElement(
            xpath='//span[@class="level-number" and text() = "{0}"]/..'
            .format(level_number)
        )

    def open_level(self, level_number):
        self.open_level_menu()
        self.get_level_link(level_number).click()

    def css_write(self, css):
        self.css_input = css
        self.enter_button.click()

    def do_level1(self):
        self.open_level(1)
        self.css_write("page")
        self.level1_link.click()
