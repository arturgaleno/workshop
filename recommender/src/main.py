import webapp2
import services

app = webapp2.WSGIApplication([
    ('/services/register', services.AccessHandler),
], debug=True)
