import model.user as u
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Unlock(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            json_obj = DeleteRequest(self.connection, f"{self.CONTEXT}/{self.user.id}/lock").execute()
            return u.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error unlocking user with id: {self.user.id}") from re