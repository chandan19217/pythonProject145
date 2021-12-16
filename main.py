from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my youtube channel'
@app.route('/sucess/<int:score>')
def sucess(score):
    return "<html><body><h1>the result is passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is "+str(score)
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='sucess'
    return redirect(url_for(result,score=marks))




if __name__=='__main__':
    app.run(debug=True)
