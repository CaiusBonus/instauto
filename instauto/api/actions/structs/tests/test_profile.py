import unittest

from instauto.api.client import ApiClient
import instauto.api.actions.structs.profile as pf

class TestProfile(unittest.TestCase):
    
    def test_setGender(self):
        client = ApiClient(testing=True)
        s = pf.SetGender("male")
        s.fill(client)

    def test_username(self):
        client = ApiClient(testing=True)
        s = pf.SetBiography("I am here")
        s.fill(client)