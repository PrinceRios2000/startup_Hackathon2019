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
    emailAddress = profile.nickname()
    registeredProfile = User.query().filter(User.email == emailAddress).get()
    if not registeredProfile:
        request.redirect("/register")
        return

class Reports(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        complaintPosts = Complaints.query()
        
        postLogoutLogic = {
            "logoutUrl": users.create_logout_url('/'),
            "complaints": complaintPosts
        }
        
        home_template = the_jinja_env.get_template('templates/main.html')
        self.response.write(home_template.render(postLogoutLogic))
        
    def post(self):
        checkLoggedInAndRegistered(self)
        
        profile = users.get_current_user()
        
        post=Complaints(
            Type = self.request.get('Type1st'),
            Location = self.request.get('Location2nd')
            Date = datetime.datetime.fromtimestamp(time.mktime(utc_time.timetuple())
            )
        post_key = post.put()
        self.response.write("Reports created: " + str(post_key) + "<br>")
        self.response.write("<a href='/'>Home</a> | ")
        self.response.write("<a href='/myreport'>My posts</a>")
        


    
app = webapp2.WSGIApplication([
    ('/', Home),
    ('/reports', Reports),
    ('/myreport', userReport),
    ('register', Registration)
], debug=True)