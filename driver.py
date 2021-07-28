from re import template
from flask import Flask, request, render_template, url_for,redirect
from email_notification_api import send_client_mail, send_admins_mail

app = Flask(__name__, template_folder='templates')



@app.route("/send", methods = ['POST','GET'])
def mail_server():
    if request.method == "POST":
       name = request.form['nm']
       email = request.form['em']
       
       send_client_mail(email)
       send_admins_mail(email,name)
       
    #    print(name+"" +email)
    #    print("transec")
       return redirect(url_for('homepage'))


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog_article')
def blogArticle():
    return render_template('blog-article.html')

    
    
if __name__ == '__main__':
    app.run(debug= True , host= '0.0.0.0')
        