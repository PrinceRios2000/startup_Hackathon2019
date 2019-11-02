import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import db
from models import Complaints, User

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def checkLoggedInAndRegistered(request):
    profile = users.get_current_user()
    if not profile:
        request.redirect("/login")
        return
    email_address = profile.nickname()
    registered_profile = User.query().filter(User.email == email_address).get()
    if not registered_profile:
        request.redirect("/register")
        return
class Home(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        complaintPosts = Complaints.query()
        
        
        
        


    
app = webapp2.WSGIApplication([
    ('/', Home),
    ('/reports', Reports),
    ('/myreport', userReport),
    ('register', Registration)
], debug=True)