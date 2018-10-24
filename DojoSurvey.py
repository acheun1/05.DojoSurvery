#Dojo Survey + NOTES
#2018 09 29
#Cheung Anthony

# When you build this, please make sure that your program meets the following criteria:

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
# http://localhost:5000/result - have this display a html with the information that was submitted by POST
# http://localhost:5000/danger - have this redirect back to "/".  Before redirecting back print in the terminal/console a message: "a user tried to visit /danger.  we have redirected the user to /".

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#our index route will handle the form
@app.route('/')
def index():
    return render_template('index.html')

#route to handle form submission that calls HTTP allowed for this route
@app.route('/results', methods=['POST'])
def submitted():
    return render_template('submitted.html')

@app.route('/danger')
def alert():
    print('******ALERT: a user tried to visit /danger. we have redirected the user to /*******')

    #redirect back to the '/' route
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)


