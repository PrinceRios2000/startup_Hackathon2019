import webapp2
import jinja2
import os
from models import Complaints, User
from google.appengine.api import users
from google.appengine.ext import db


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    

def checkLoggedInAndRegistered(request):
    profile = users.get_current_user()
    if not profile:
        request.redirect("/")
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
            Location = self.request.get('Location2nd'),
            Date = self.request.get('Date3rd')
            )
        post_key = post.put()
        self.response.write("Reports created: " + str(post_key) + "<br>")
        self.response.write("<a href='/'>Home</a> | ")
        self.response.write("<a href='/myreport'>My posts</a>")
        
class userReport(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        profile = users.get_current_user()
        email_address = profile.nickname()
        
        profile_posts = User.query().filter(User.owner == email_address).fetch()
        the_variable_dict = {
            "logout_url":  users.create_logout_url('/'),
            "profile_posts": profile_posts,
        }
        
        profile_posts_template = the_jinja_env.get_template('templates/filecomplaint.html')
        self.response.write(profile_posts_template.render(the_variable_dict))
        
    def post(self):
        checkLoggedInAndRegistered(self)
        
        post = Complaints(
        Type = self.request.get('Type1st'), 
        Location=self.request.get('Location2nd'),
        Date = self.request.get('Date3rd')
        )
        post_key = post.put()
        self.redirect("/myreport")
        
class Login(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/intro.html')
        
        the_variable_dict = {
            "login_url":  users.create_login_url('/')
        }
        self.response.write(login_template.render(the_variable_dict))
        
class Registration(webapp2.RequestHandler):
    def get(self):
        profile = users.get_current_user()
        
        registration_template = the_jinja_env.get_template('templates/registration.html')
        the_variable_dict = {
            "email_address":  profile.nickname()
        }
        
        self.response.write(registration_template.render(the_variable_dict))
    
    def post(self):
        profile = users.get_current_user()
        
        citizen_acc = User(
            FirstName=self.request.get('first_name'), 
            LastName =self.request.get('last_name'),
            PhoneNumber =self.request.get('last_name'),
            Location = self.request.get('last_name'),
            Email=profile.nickname()
        )
        
        citizen_acc.put()
        
        self.redirect('/')
class DeletepostHandler(webapp2.RequestHandler):
    def get(self):
        client = users.get_current_user()
        profile_post = Complaints.query().fetch()
        
    def post(self):
        postid= self.request.get("postid")
        post=Complaints.get_by_id(int(postid))
        post.key.delete()
        print(self.request.get("postid"))
        self.redirect("/myreport")
    
app = webapp2.WSGIApplication([
    ('/', Login),
    ('/reports', Reports),
    ('/myreport', userReport),
    ('/register', Registration)
], debug=True)