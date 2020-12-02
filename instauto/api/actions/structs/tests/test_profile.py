import unittest

from instauto.api.client import ApiClient
import instauto.api.actions.structs.profile as pf

class TestProfile(unittest.TestCase):
    
    def test_setGender(self):
        client = ApiClient(testing=True)
        s = pf.SetGender("male")
        s.fill(client)

    def test_setBiography(self):
        client = ApiClient(testing=True)
        s = pf.SetBiography("I am here")
        s.fill(client)

    def test_Info(self):
        client = ApiClient(testing=True)
        s = pf.Info(1358549127)
        s.fill(client)