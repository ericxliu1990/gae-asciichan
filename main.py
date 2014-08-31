"""

"""
import os
import webapp2
import jinja2

from google.appengine.ext import db

ERROR = "We need a title and art work"

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
	autoescape = True)

class Art(db.Model):
	"""a class represented artwork in the database"""
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	created_time = db.DateTimeProperty(auto_now_add = True)

class Handler(webapp2.RequestHandler):
	"""
	General hander class for rendering contents to GAE
	"""
	def write(self, *args, **kwargs):
		self.response.out.write(*args, **kwargs)

	def render_string(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)

	def render(self, template, **kwargs):
		self.write(self.render_string(template, **kwargs))

class MainPage(Handler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.render("asciichan.html")
	def post(self):
		title = self.request.get("title")
		art = self.request.get("art")

		if title and art:
			a_art = Art(title = title, art = art)
			a_art.put()
			self.redirect('/')
		else:
			self.render("asciichan.html", title = title, art = art, error = ERROR)


application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
