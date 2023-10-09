from utils.logger.logger import logger
import random
import string
from utils.call_request.call_request import CallRequest


class StoryManager:
    def __init__(self):
        self.request = CallRequest()

    def create_story(self, project_id, name="", body_request=None):
        url = f"https://www.pivotaltracker.com/services/v5/projects/{project_id}/stories"

        if name == "":
            name = 'AGarcia'.join(random.choices(string.ascii_uppercase, k=2))

        if body_request is None:
            body_request = {
                "name": name
            }

        response = self.request.post(url=url, payload=body_request)
        status_code = response.status_code
        body_response = response.json()
        body_response.setdefault('status_code', status_code)
        return body_response

    def list_stories(self, project_id):
        url = f"https://www.pivotaltracker.com/services/v5/projects/{project_id}/stories"
        response = self.request.get(url=url)
        body_response = response.json()
        body_response.setdefault('status_code', response.status_code)
        return body_response

    def get_story_by_id(self, project_id, story_id):
        url = f"https://www.pivotaltracker.com/services/v5/projects/{project_id}/stories/{story_id}"
        response = self.request.get(url=url)
        body_response = response.json()
        body_response.setdefault('status_code', response.status_code)
        return body_response

    def delete_story_by_id(self, project_id, story_id):
        url = f"https://www.pivotaltracker.com/services/v5/projects/{project_id}/stories/{story_id}"
        response = self.request.delete(url=url)
        body_response = {'status_code': response.status_code}
        return body_response
