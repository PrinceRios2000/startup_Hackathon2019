from google.appengine.ext import ndb

class Complaints(ndb.model):
    Type = ndb.StringProperty(required=True)
    Location = ndb.StringProperty(required=True)
    Date = ndb.StringProperty(required=True)

class User(ndb.model):
    FirstName = ndb.StringProperty(required=True)
    LastName = ndb.StringProperty(required=True)
    Email = ndb.Email(required=True)
    PhoneNumber = ndb.PhoneNumberProperty(required=True)
    Location = ndb.StringProperty(required=True)