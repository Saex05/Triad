*** Settings ***
Documentation   Test to verify login user in trello
Resource  tests/trello/gui/tests/resources/common.resource
Resource  tests/trello/gui/tests/resources/login.resource
Test Setup  Initialized Actor
Test Teardown  Stop Actor


*** Test Cases ***
Verify that it is possible login a user
	Given User In Trello Page
	When Click To Login Button
	And Submit Username and Password
	Then Trello Home Page Should Be Displayed
