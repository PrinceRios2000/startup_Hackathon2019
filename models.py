from google.appengine.ext import ndb

class Complaints(ndb.model):
    Type = ndb.StringProperty(required=True)
    Location = ndb.StringProperty(required=True)
    Date = ndb.DateProperty(auto_now_add=True)

class User(ndb.model):
    FirstName = ndb.StringProperty(required=True)
    LastName = ndb.StringProperty(required=True)
    Email = ndb.Email(required=True)
    Location = ndb.StringProperty(required=True)