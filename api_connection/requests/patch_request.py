import requests
from requests.auth import HTTPBasicAuth

from api_connection.request import Request


class PatchRequest(Request):

    def __init__(self, connection, context, json):
        super.__init__(connection, context, json)

    def _execute_request(self):
        return requests.patch(
            self.connection.url_base + self.context,
            auth=HTTPBasicAuth(self.connection.api_user, self.connection.api_key),
            json=self.json
        )
