from flask import render_template, redirect, url_for
from app import app
from app.forms import ContactForm
from app.email import send_email

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
	user = {
	'image': 'https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.catbreedslist.com%2Fcat-wallpapers%2FPersian-kitten-grass-white-2560x1600.jpg&f=1',
	'desc': ['Cat', 'Filler text before next ark', 'Lord Volde', 'Author died before completing work']
	}


	projects = [
		{'name': 'Project A', 'languages': ['Html, Css, JavaScript'], 'gitrepo': '#', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim'},
		{'name': 'Project B', 'languages': ['Python'], 'gitrepo': '#', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim'},
		{'name': 'Project C', 'languages': ['Python, Flask'], 'gitrepo': '#', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim'},
		{'name': 'Project D', 'languages': ['Pandas', 'Flask Rest-Api','scikit-learn'], 'gitrepo': '#', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim'},
		{'name': 'Project E', 'languages': ['Scheme'], 'gitrepo': '#', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim'},
		{'name': 'Project F', 'languages': ['Clojure', 'Java'], 'gitrepo': '#', 'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim'}
	]
	form = ContactForm()
	if form.validate_on_submit():
		send_email(form.subject.data, app.config['EMAIL'], [app.config['EMAIL']], render_template('_email.html', email=form.email.data, description=form.content.data))		
		return redirect(url_for('index'))
	return render_template('index.html', title='Billy', form=form, projects=projects, user=user)
