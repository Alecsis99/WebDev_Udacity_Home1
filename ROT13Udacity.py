__author__ = 'FUrian'

import webapp2
import functions

form = """
	<form method="post">
		<h2><b>Enter some text to ROT13:<b/></h2>
		<textarea name="text" rows=="20" cols="50" style="height:200px; margin-bottom:20px;">%(message)s</textarea><br>
		<input type="submit" value="Submit">
	</form>
"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, message=""):
        self.response.out.write(form % {"message" : functions.escape_html(message)})

    def get(self):
        self.write_form()


    def post(self):
    	message = self.request.get('text')
    	message = functions.ROT13(message)
        self.write_form(message)


application = webapp2.WSGIApplication([('/', MainPage)], debug=True)