*** Settings ***
Documentation  Test Demo
Library  projects.pivotaltracker.api.managers.story_manager.StoryManager

*** Test Cases ***
Verify that it is possible to create a story
    ${story}  Create Story  project_id=1562913
    Should Be Equal  ${story}[status_code]  ${200}
