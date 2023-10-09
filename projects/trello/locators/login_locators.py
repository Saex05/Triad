from screenpy_selenium import Target
from selenium.webdriver.common.by import By

# Web Elements
THREE_LINES_BUTTON = Target.the("three_lines_button").located_by("//*[@id='BXP-APP']/header[2]/div[1]/button[2]/div")
LOGIN_BUTTON = Target.the("Login Button").located_by("//*[@id='BXP-APP']/header[2]/div[2]/div[1]/div[2]/a[2]")
ATLASSIAN_ICON = Target.the("atlassian_icon").located_by((By.CLASS_NAME, "Logo-sc-1anfgcw-0 gguOta"))

USERNAME_TEXTBOX = Target.the("username textbox").located_by((By.ID, "username"))
SUBMIT_BUTTON = Target.the("submit button").located_by((By.ID, "login-submit"))
PASSWORD_TEXTBOX = Target.the("password textbox").located_by((By.ID, "password"))
TRELLO_ICON = Target.the("trello icon").located_by((By.CLASS_NAME, "awhMAO3feX83U4"))