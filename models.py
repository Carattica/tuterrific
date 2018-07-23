from google.appengine.ext import ndb

class UserInfo(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    user_type = ndb.StringProperty()
    sub = ndb.StringProperty()
    availability = ndb.StringProperty()