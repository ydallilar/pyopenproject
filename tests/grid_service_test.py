import unittest

from business.grid_service import GridService


class GridServiceTestCase(unittest.TestCase):
    gridSer = GridService()

    def test_find(self):
        self.assertNotNull(self.gridSer.find(grid))

    def test_find_all(self):
        self.assertNotNull(self.gridSer.find_all(offset, pageSize, filters, sortBy))

    def test_create(self):
        self.assertNotNull(self.gridSer.create(grid))

    def test_update(self):
        self.assertNotNull(self.gridSer.update(grid))

    def test_create_form(self):
        self.assertNotNull(self.gridSer.create_form(grid))
