from screenpy import AnActor
from screenpy_selenium import BrowseTheWeb, Open
from core.gui.config import TRELLO_USERNAME, TRELLO_PASSWORD, TRELLO_BASE_URL


def initialize_actor():
    an_actor = Actor()
    return an_actor


class Actor(AnActor):
    def __init__(self, username=TRELLO_USERNAME, password=TRELLO_PASSWORD, browser="chrome"):
        self.username = username
        self.password = password
        super().__init__(self.username)
        self.who_can(self.select_scenario(browser))

    @staticmethod
    def select_scenario(browser="chrome"):
        browser_type = {
            "chrome": BrowseTheWeb.using_chrome,
            "firefox": BrowseTheWeb.using_firefox
        }
        return browser_type.get(browser)()

    def start_function(self, scenario=TRELLO_BASE_URL):
        self.attempts_to(Open.their_browser_on(scenario))

