*** Settings ***
Documentation  Common steps to run API test
Library  core/gui/actors/actor.py


*** Keywords ***
Initialized Actor
    ${actor}  Initialize Actor
    Set Suite Variable  ${ACTOR}  ${actor}
    Call Method  ${ACTOR}  start_function
Stop Actor
    Call Method  ${ACTOR}  exit
