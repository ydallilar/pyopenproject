from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.role.role_command import RoleCommand
from model.role import Role


class FindAll(RoleCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = f"?filters={filters}" if filters else ""

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}{self.filters}").execute()
            for role in json_obj["_embedded"]["elements"]:
                yield Role(role)
        except RequestError as re:
            raise BusinessError(f"Error finding all roles with filters: {self.filters}") from re
