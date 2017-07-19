from flask import Flask, render_template
#importing a package buit by you
#import Board

#imports flask and creates a new website in a new variable called "app"
#app is the WSGI application
#Started as an app __name__ = __main__ else name of the module, so that it can find the template/static folder
app = Flask(__name__)

#generate the html table needed for the UI using jinja templating

from MineSweeperInitializer import MineSweeperInitializer

#Created a minesweeper WebBoard
msBoard = MineSweeperInitializer()

#now need to show it on the UI - move it to WebBoard - to generate HTML
#this is required before rendering

height = msBoard.board.height 
#@ decorator for function definitions, if the app requests (/minesweeper) on the browser, route to hhomepage
@app.route('/Minesweeper')
def homepage():
##    templatedict = {
##        'width': msBoard.board.width,
##        'height': msBoard.board.height,
##        'array': msBoard.board.zoneArr
##        }

    
    return render_template('minesweeper.html', h = height)

    #return "Hello world"


#runs the app, calls homepage()
if __name__ == "__main__":
    app.run()

#Post writing this app set PYTHONPATH to C:\Program Files (x86)\Ampps\www\Minesweeper
#set FLASK_APP=minesweeper.py
#set FLASK_DEBUG=1
#flask run

#If this python file is updated while flask is running automatically it uploads it

#http://flask.pocoo.org/docs/0.12/quickstart/
#http://localhost:5000/Minesweeper -now will load minesweeper.html

#static folder has all the bootstrap files and template folder has the html



