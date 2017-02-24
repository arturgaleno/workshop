import unittest

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import testbed

class TestBase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_user_stub()
        self.testbed.init_urlfetch_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()
