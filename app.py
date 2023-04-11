import os
import glob
# from forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from helpers import scraper

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#################################
# sql database section
#################################

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# db = SQLAlchemy(app)
# Migrate(app,db)

# class Puppy(db.Model):

#     __tablename__ = 'puppies'
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.Text)

#     def __init__(self,name):
#         self.name = name

#     def __repr__(self):
#         return f"Puppy name: {self.name}"


@app.route("/")
def home():
    message = "No job is too small. Right job at the Right price"
    return render_template("home.html", message=message)


@app.route("/services")
def services():
    message = "We offer many services"
    services = {
        "Painting":"If you need it painted, we can do it!  Interior, exterior, trim, walls ceilings and furniture.  We do it all!  Request a quote today!",
        "Powerwashing": "Is that siding, deck, fence, or sidewalk looking dingy?  Need your deck or fence stripped?  Our powerwashing service is just what you need!",
        "Cabinet and Countertop installation":"We can install your next kitchen, bathroom or bar countertop.  Hanging cabinets isn't for the faint of heart, let us do it for you!",
        "Electrical":"General electric work including doorbell, ring light and outlet installation.  We also can install your next lighting project or ceiling fan.",
        "Plumbing":"Toilet installation as well as kitchen and bathroom faucet installation are right up our alley.  We install outside faucets and spigots too.  Need that garbage disposal installed?  No problem!  Request a quote!",
        "Dryer vent cleaning":"Just what it says, No job is too small.  Request a quote!",
        "Decks and Fences": "If you have a deck or fence that needs repaired let us know, we'll repair or extend your existing structure.  We can also clean it with our powerwashing service as well as offering quality paints and stains to make it look like new!",
        "Caulking Services":"Window, bathrooms, kitchens, trim, they all need it.  It's a messy job, let us do it.",
        "Flooring":"We can install your next vinyl, faux wood or plank floor",
        "Tile":"Always wanted that beautiful tile backsplash for your kitchen?  We can do it.  We can also install your tile floor.",
        "Drywall":"Do you need patching or small to medium sections of drywall repaired?  Let us know!  Request a quote.",
        "General Landscaping":"Landscaping is where we started.  Plantings, hardscaping, seeding, fertilizer, lets us know what you need done.",
    }
    return render_template("services.html", message=message, services=services)


@app.route("/photos")
def photos():
    pictures= os.listdir(os.path.join(app.static_folder, "pictures"))
    return render_template("photos.html",pictures=pictures)


@app.route("/testimonials")
def testimonials():
    message="Testimonials"
    return render_template("testimonials.html", message=message)


@app.route("/quote")
def quote():
    return render_template("quote.html")


if __name__ == "__main__":
    app.run(debug=True)