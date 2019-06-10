from flask import Flask, request, redirect, url_for, render_template
from flask_assets import Environment, Bundle

# app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# app.config.from_envvar('APP_SETTINGS')

css_asset = Environment(app)
css_admin = Bundle('css/bootstrap.css', 'css/main.css', filters='cssmin', output='css/main_css.css')
css_asset.register('css_admin', css_admin)

""" 
js_asset = Environment(app)
js_admin = Bundle('js/jquery-3.3-1.js', 'js/popper.js', 'js/bootstrap.js', 'js/fontawesome.js', filters='jsmin', output='js/main_js.js')
js_asset.register('js_admin', js_admin)
 """

@app.route('/')
@app.route('/index')
def home():
    posts = [
        ['التغريدة الأولى', 'هذه تغريدتي الأولى في هذا الموقع لمن أراد الفائدة', 'عمر ناصر', '11-05-2019'],
        ['التغريدة الثانية', 'مجموعة من الكلمات التي نعجز عن ذكرها وهي ', 'محمود سامي', '18-05-2019'],
        ['التغريدة الثالثة', 'لا نقول مثلهم في .. ولا نفعل مثلهم .. كذلك', 'خالد فهد', '31-05-2019'],
        ['التغريدة الرابعة', 'كلما أردت الخروج في نزهة إلى مكان ما فخذ ..', 'وليد ياسين', '11-06-2019'],
    ]
    title = 'الصفحة الرئيسة'

    return render_template('index.html', posts=posts, title=title)

if __name__ == '__main__':
	app.run()
