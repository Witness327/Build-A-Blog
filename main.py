from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:wamp1234@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'wamp1234'

class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    entry = db.Column(db.String(500))

    def __init__(self, title, entry):
        self.title = title
        self.entry = entry

@app.route('/')
def index():
    blog_posts = Blog.query.all()
    return render_template('mainpage.html',blog_posts=blog_posts)




@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_entry = request.form['entry']

        new_blog = Blog(blog_title, blog_entry)
        db.session.add(new_blog)
        db.session.commit()
        
    blog_posts = Blog.query.all()
    
    return render_template('newpost.html',blog_posts=blog_posts)

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    if request.method == 'GET':
        postid = request.args.get('id')
        blog_posts = Blog.query.get(postid)
        return render_template('blog.html', postid=postid, blog=blog_posts)

        # print("POSTID: :",postid)
        # print("HELP: :")
# @app.route('/blog', methods=['POST', 'GET'])
# def blog():
#     blog_posts = Blog.query.all()
#     return render_template('blog.html', blog_posts=blog_posts)

# @app.route('/blog', methods=['POST', 'GET'])
# def blog():
#         if request.method == 'POST':
#             blog_title = request.form['title']
#             blog_entry = request.form['entry']
#             blog_posts = Blog.query.all()

#             id = request.args.get('id')
    
#         return redirect('/blog?id={0}'.format(id), blog_posts=blog_posts, blog=blog,blog_title=blog_title, blog_entry=blog_entry)
    
# @app.route('/blog', methods=['POST', 'GET'])
# def blog():

#     id = request.args.get('id')
#     blog_posts = Blog.query.get(id)
#     return render_template('blog.html', blog_posts=blog_posts,id=id)

# @app.route('/blog', methods=['POST', 'GET'])
# def blog():

    # blog_id = int(request.form['blog-id'])
    # task = Task.query.get(blog_id)

    # id = request.args.get('id')
    # blog_posts = Blog.query.get(id)
    # return redirect('/blog?blog_posts={0}'.format(blog_posts), blog_posts=blog_posts,id=id)




if __name__ == '__main__':
    app.run()
