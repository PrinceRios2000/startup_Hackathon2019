from google.appengine.ext import ndb

class Complaints(ndb.Model):
    Type = ndb.StringProperty(required=True)
    Location = ndb.StringProperty(required=True)
    Date = ndb.StringProperty(required=True)
    owner = ndb.StringProperty(required=True)

class User(ndb.Model):
    FirstName = ndb.StringProperty(required=True)
    LastName = ndb.StringProperty(required=True)
    Email = ndb.StringProperty(required=True)
    PhoneNumber = ndb.StringProperty(required=True)
    Location = ndb.StringProperty(required=True)
    Special = ndb.StringProperty(required=False)