#!coding:utf-8
# Main script of the application
from flask import Flask, render_template, request
from modules import preprocess

app = Flask(__name__)  # generate Flask instance.
@app.route('/')  # decorator (root).
def index():
    return render_template('index.html')  # first view (template file).

# Main process
@app.route('/app.py', methods=['POST'])  # form access by POST.
def creeibility_assessment():
    target = request.form['target']  # get the input from users (form).
    lang = preprocess.lang_judge(target)  # evaluate language type.
    
    # Natural language preprocessing
    if lang == "English":  # English process.
        target = preprocess.english(target)
    elif lang == "Japanese":  # Japanese process.
        target = preprocess.japanese(target)
        


    score = 0  # credibility score.
    # Return the result of all process
    return render_template('output.html',
    target = target,
    score = score
    )

if __name__=='__main__':
    app.debug = True  # debug mode ON.
    app.run(host='localhost')  # run localhost.
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))  # run heroku.