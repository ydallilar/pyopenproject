from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.attachment.attachment_command import AttachmentCommand


class Delete(AttachmentCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            Connection().delete(f"{self.context}")
        except RequestError as re:
            raise BusinessError(f"Error deleting attachment by context: {self.context}") from re
