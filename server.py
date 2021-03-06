from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def go_home():
	"""Goes to the homepage.  Homepage links user to application."""

	# Homepage welcomes user and has a link to the application
	return render_template("index.html")

@app.route('/application-form')
def get_application():
	"""Gets info from applicant."""
	
	jobs = ["Software Engineer", "QA Engineer", "Product Manager"]

	return render_template("application-form.html", jobs=jobs)

@app.route('/application-success', methods=["POST"])
def process_application():
	"""Processes application."""

	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	salary = request.form.get("salary")
	salary = "${:,.2f}".format(float(salary))
	job = request.form.get("jobapplyingfor")
	
	return render_template("application-response.html", first_name=first_name,
		last_name=last_name, salary=salary, job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
