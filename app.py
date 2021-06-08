from boggle import Boggle
from flask import Flask, session, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

boggle_game = Boggle()

app.config["SECRET_KEY"] = "maxcode"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def generate_board():
    session["board"] = boggle_game.make_board() # board looks like board[y][x]
    highscore = session.get("highscore", "0")
    plays = session.get("plays", "0")
    
    return render_template("game.html", board=session["board"], highscore=highscore, plays=plays)

@app.route('/', methods=["POST"])
def get_user_guess():
    # do something that gets the users word
    user_word = request.form.get("guess")# gets name="user_word" from html


    
    return redirect('/')

@app.route('/check_word')
def check_word():
    """
        returns jsonified API response back to user after they submit something
    """
    
    #check if word is valid for right now; THAT is it; solve easier prob then harder
    word = request.args.get('word')
    response = boggle_game.check_valid_word(session["board"], word)

    return jsonify({"result": response})

    #when using a POST request str8 from html form get data via request.form 
    #when getting stuff from axios the args are passed in via params: {}
        #the url will look like blah.com/?param1=50&param2=hello
        #now we get data with request.args

@app.route('/update_score_plays', methods=["POST"])
def update_score_plays():
    """
        updates user's score and number of plays/guesses in the backend
    """

    data = request.json
    
    if request.json["score"] > session.get("highscore", 0):
        session["highscore"] = request.json["score"]
        session["plays"] = request.json["plays"]

    # import pdb
    # pdb.set_trace()

    return redirect('/')
    
    # if newrecordReturned > oldrecordinSession :
    #     session["highscore"] = jsonthing_with_score
    #     session["plays"] = jsonthing_with_plays
    
    #store high score w/ number of plays on backend and render it somewhere later
    #make an if statement to compare if it beat the old record.