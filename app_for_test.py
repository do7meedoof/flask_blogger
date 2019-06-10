from flask import Flask, request, redirect, url_for

# app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# app.config.from_envvar('APP_SETTINGS')

def page_view(self, h3_title='Hello World', p_welcome = 'Welcome guest', first='', last='', p_post = '', p_guest = '', path_title = '', p_method='GET', formy=''):
# def page_view(self, h3_title='Hello World', p_welcome = 'Welcome guest', p_method='GET', **kwargs):
	page_html = f"""
	<h3> {h3_title} </h3>
	<p> {p_welcome} </p>
	<span> first name: {first} </span>
	<br />
	<span> last name: {last} </span>
	<br /><br />
	<p> Posts no: {p_post} </p>
	<p> Sub Path is: {path_title} </p>
	<br />
	<p> this is {p_method} </p>
	<div>{formy}<div>
	"""
	return page_html

@app.route('/')
def home():
	# return '<h3> Hello World </h3><p> Welcome</p>'
	return page_view(self='')

@app.route('/about')
def about():
	# return '<h3> This is about page </h3><p> its me again </p>'
	return page_view(self='', h3_title='This is about page', p_welcome='its me again')

@app.route('/user/<username>')
def user_show(username):
	if(username == 'admin'):
		return redirect(url_for('admin_show'))
	else:
		return redirect(url_for('guest_show', guest = username))
		# return f'<h3> User page </h3><p> Welcome {username} </p>'

@app.route('/post/<int:post_id>')
def post_show(post_id):
	# return f'<h3> Posts page </h3><p> post {post_id} </p>'
	return page_view(self='', h3_title='Posts page', p_post=post_id)

@app.route('/path/<path:sub_path>')
def path_show(sub_path):
	# return f'<h3> tree page </h3><p> this path is {sub_path} </p>'
	return page_view(self='', h3_title='tree page', path_title=f' this path is {sub_path}')

@app.route('/member')
def user_print():
	username = request.args.get('first_name')
	lastname = request.args.get('last_name')
	# return f'<h3> Members page </h3><p> Welcome: </p><span>{username}</span><br/><span>{lastname}</span>'
	return page_view(self='', h3_title='Members page', p_welcome=f'Welcome: {username} {lastname}', first=username, last=lastname)

@app.route('/admin')
def admin_show():
	# return '<h3> Admin page </h3><p> Welcome Admin </p>'
	return page_view(self='', h3_title='Admin page', p_welcome='Welcome Admin')

@app.route('/guest/<guest>')
def guest_show(guest):
	# return f'<h3> Guest page </h3><p> Welcome {guest} as guest</p>'
	return page_view(self='', h3_title='Guest page', p_welcome=f'Welcome {guest} as guest')

@app.route('/page', methods = ['POST', 'GET'])
def page_show():
	if(request.method == 'POST'):
		# return '<h3> Post page </h3><p> im posty </p>'
		return page_view(self='', h3_title='Post page', p_welcome='im posty page', formy='<form method="get"><input type="submit" value="get" /></form>')
	else:
		# return '<h3> Get page </h3><p> im getty </p><form method="post"><input type="submit" value="ok" /></form>'
		return page_view(self='', h3_title='Get page', p_welcome='im getty page', formy='<form method="post"><input type="submit" value="post" /></form>')

if __name__ == '__main__':
	app.run()
	# or app.run(port=3456) to run it on port 3456
	# ot app.run(debug=True) to run it in debug mode
	# or app.run(port=app.config['PORT'], debug=app.config['DEBUG'])