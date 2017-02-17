import webapp2
from src.queue import TrainQueue

app = webapp2.WSGIApplication([
    ('/train', TrainQueue),
], debug=True)
