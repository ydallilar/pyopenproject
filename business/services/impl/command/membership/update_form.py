
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.form import Form


class UpdateForm(MembershipCommand):

    def __init__(self, connection, membership, form):
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{self.membership.id}/form",
                                    json=self.membership.__dict__)
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating membership") from re