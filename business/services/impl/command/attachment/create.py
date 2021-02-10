import json
import os

import model.attachment as att
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand


class Create(AttachmentCommand):

    def __init__(self, connection, filename, description, file_path):
        super().__init__(connection)
        self.filename = filename
        self.description = description
        with open(file=file_path, mode='rb') as f:
            self.file_content = f.read()
            self.file_path = os.path.abspath(f.name)

    def execute(self):
        try:
            metadata = {"fileName": self.filename, "description": {"raw": self.description}}
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}",
                                   files={
                                       'file': ('attachment', self.file_content),
                                       'metadata': (None, json.dumps(metadata))
                                   }
                                   ).execute()
            return att.Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating attachment : {self.filename}") from re
