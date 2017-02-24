import json
import webapp2

from google.appengine.ext import ndb

class AccessHandler(webapp2.RequestHandler):
    def post(self):
        response_data = {"status": 200}
        data = json.loads(self.request.body)

        ent = AccessEntity()
        ent.user_id = int(data["user_id"])
        ent.item_id = int(data["item_id"])
        ent.put()

        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.write(json.dumps(response_data))

class AccessEntity(ndb.Model):
    user_id = ndb.IntegerProperty(indexed=True)
    item_id = ndb.IntegerProperty(indexed=True)
    timestm = ndb.DateTimeProperty(auto_now_add=True)
