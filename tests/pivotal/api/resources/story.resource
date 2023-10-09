*** Settings ***
Documentation  Test Demo
Library  projects.pivotaltracker.api.managers.story_manager.StoryManager


*** Keywords ***
Get Proyect And Create Story
    Set Test Variable  ${PROJECT_ID}  1562913
    ${story}  Create Story  project_id=${PROJECT_ID}
    Set Test Variable  ${STORY}  ${story}

Delete Story Created In Setup
    Delete Story By Id  project_id=${PROJECT_ID}  story_id=${STORY}[id]
