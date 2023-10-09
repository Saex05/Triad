*** Settings ***
Library  core/gui/abilities/login_abilities.py


*** Keywords ***
User In Trello Page
	${login_abilities}  Initialize Login Ability  ${ACTOR}
	Set Suite Variable  ${LOGIN_ABILITIES}  ${login_abilities}

Click To Login Button
	Call Method  ${LOGIN_ABILITIES}  go_and_click_to_login_button

Submit Username and Password
	Call Method  ${LOGIN_ABILITIES}  submit_username
	Call Method  ${LOGIN_ABILITIES}  submit_password

Trello Home Page Should Be Displayed
	Call Method  ${LOGIN_ABILITIES}  wait_for_trello_icon