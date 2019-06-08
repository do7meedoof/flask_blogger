from flask import Flask, request, redirect, url_for

# app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('APP_SETTINGS')

@app.route('/')
def home():
	return '<h3> Hello World </h3><p> Welcome</p>'

@app.route('/about')
def about():
	return '<h3> This is about page </h3><p> its me again </p>'

@app.route('/user/<username>')
def user_show(username):
	if(username == 'admin'):
		return redirect(url_for('admin_show'))
	else:
		return redirect(url_for('guest_show', guest = username))
		# return f'<h3> User page </h3><p> Welcome {username} </p>'

@app.route('/post/<int:post_id>')
def post_show(post_id):
	return f'<h3> Posts page </h3><p> post {post_id} </p>'

@app.route('/path/<path:sub_path>')
def path_show(sub_path):
	return f'<h3> tree page </h3><p> this path is {sub_path} </p>'

@app.route('/member')
def user_print():
	username = request.args.get('first_name')
	lastname = request.args.get('last_name')
	return f'<h3> Members page </h3><p> Welcome: </p><span>{username}</span><br/><span>{lastname}</span>'

@app.route('/admin')
def admin_show():
	return '<h3> Admin page </h3><p> Welcome Admin </p>'

@app.route('/guest/<guest>')
def guest_show(guest):
	return f'<h3> Guest page </h3><p> Welcome {guest} as guest</p>'

@app.route('/page', methods = ['POST', 'GET'])
def page_show():
	if(request.method == 'POST'):
		return '<h3> Post page </h3><p> im posty </p>'
	else:
		return '<h3> Get page </h3><p> im getty </p><form method="post"><input type="submit" value="ok" /></form>'

if __name__ == '__main__':
	app.run()
	# or app.run(port=3456) to run it on port 3456
	# ot app.run(debug=True) to run it in debug mode
	# or app.run(port=app.config['PORT'], debug=app.config['DEBUG'])