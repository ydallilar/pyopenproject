import model.membership as mem
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand


class Create(MembershipCommand):

    def __init__(self, connection, membership):
        """
        Constructor for class Create, from MembershipCommand
        :param connection: The connection data
        :param membership: The membership to create
        """
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.membership.__dict__).execute()
            return mem.Membership(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating membership") from re
