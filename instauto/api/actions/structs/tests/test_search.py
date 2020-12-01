import unittest

from instauto.api.client import ApiClient
import instauto.api.actions.structs.search as sr
from instauto.api.actions.tests.common import helper


class TestSearch(unittest.TestCase):

    def test_tag(self):
        client = ApiClient(testing=True)
        s = sr.Tag('test',1)
        s.fill(client)
        helper(s, self)

    def test_tag(self):
        client = ApiClient(testing=True)
        s = sr.Username("test",1)
        s.fill(client)
        helper(s, self)