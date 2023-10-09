*** Settings ***
Documentation  Test Demo
Library  projects.pivotaltracker.api.managers.story_manager.StoryManager
Resource  tests/pivotal/api/resources/story.resource
Test Setup  Get Proyect And Create Story

*** Test Cases ***
Verify that it is possible to delete a story by id
    ${response}  Delete Story By Id  project_id=${PROJECT_ID}  story_id=${STORY}[id]
    Should Be Equal  ${response}[status_code]  ${204}
    ${story}  Get Story By Id  project_id=${PROJECT_ID}   story_id=${STORY}[id]
    Should Be Equal  ${story}[status_code]  ${404}