from business.services.impl.command.time_entry.create import Create
from business.services.impl.command.time_entry.create_form import CreateForm
from business.services.impl.command.time_entry.delete import Delete
from business.services.impl.command.time_entry.find import Find
from business.services.impl.command.time_entry.find_all import FindAll
from business.services.impl.command.time_entry.find_between_days import FindBetweenDays
from business.services.impl.command.time_entry.find_by_context import FindByContext
from business.services.impl.command.time_entry.find_projects import FindAvailableProjects
from business.services.impl.command.time_entry.find_schema import FindSchema
from business.services.impl.command.time_entry.update import Update
from business.services.impl.command.time_entry.update_form import UpdateForm
from business.services.time_entry_service import TimeEntryService


class TimeEntryServiceImpl(TimeEntryService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_projects(self, time_entry):
        return list(FindAvailableProjects(self.connection).execute())

    def create_form(self, project=None, work_package=None, activity=None, comment=None, spent_on=None, hours=None):
        return CreateForm(self.connection, project, work_package, activity, comment, spent_on, hours).execute()

    def update_form(self, form):
        return UpdateForm(self.connection, form).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()

    def find_between_days(self, start_date, end_date):
        return list(FindBetweenDays(self.connection, start_date, end_date).execute())

    def find(self, time_entry):
        return Find(self.connection, time_entry).execute()

    def delete(self, time_entry):
        return Delete(self.connection, time_entry).execute()

    def create(self, time_entry):
        return Create(self.connection, time_entry).execute()

    def update(self, time_entry):
        return Update(self.connection, time_entry).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())

    def find_schema(self):
        return FindSchema(self.connection).execute()
