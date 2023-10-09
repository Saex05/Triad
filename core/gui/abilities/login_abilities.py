from screenpy_selenium import Wait, Click, Enter

from projects.trello.locators.login_locators import THREE_LINES_BUTTON, LOGIN_BUTTON, USERNAME_TEXTBOX, SUBMIT_BUTTON, \
    PASSWORD_TEXTBOX, TRELLO_ICON


def initialize_login_ability(actor):
    login_abilities = LoginAbilities(actor)
    return login_abilities


class LoginAbilities:
    def __init__(self, actor):
        self.actor = actor

    def go_and_click_to_login_button(self):
        self.actor.attempts_to(
            Wait.for_the(THREE_LINES_BUTTON),
            Click.on_the(THREE_LINES_BUTTON),
            Click.on_the(LOGIN_BUTTON)
        )

    def submit_username(self):
        self.actor.attempts_to(
            Wait.for_the(USERNAME_TEXTBOX),
            Enter.the_text(self.actor.username).into_the(USERNAME_TEXTBOX),
            Click.on_the(SUBMIT_BUTTON)
        )

    def submit_password(self):
        self.actor.attempts_to(
            Wait.for_the(PASSWORD_TEXTBOX),
            Enter.the_text(self.actor.password).into_the(PASSWORD_TEXTBOX),
            Click.on_the(SUBMIT_BUTTON),
            Wait.for_the(TRELLO_ICON)
        )

    def wait_for_trello_icon(self):
        self.actor.attempts_to(
            Wait.for_the(TRELLO_ICON)
        )

