from distutils.log import debug
from distutils.util import execute
from itertools import count
import json
from operator import truediv
from telnetlib import IP

from flask import make_response,Flask, send_from_directory, request, render_template, jsonify, redirect, url_for
import sys
import mysql.connector
import db.mongo_functions as mf
import sqlalchemy as db
import pandas as pd
# import gevent.pywsgi
# import socket

engine = db.create_engine('mysql://root:@localhost/movie_emotions_map')


app = Flask(__name__)





# @app.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)


def load_data():

    
    sql_statement = "SELECT * FROM MoviesEmotionMap"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/new_data_cluster_emotion.csv")


    sql_statement = "SELECT * FROM lvl2anger"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_anger.csv")

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2anticipation"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_anticipation.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2disgust"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_disgust.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2fear"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_fear.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2joy"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_joy.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2sadness"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_sadness.csv")

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2surprise"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_surprise.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2trust"
    df = pd.read_sql(sql_statement, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_trust.csv", index=False)

    # -----------------------------------------------------------------------------------------------------


# @app.route('/anger')
# def hello_world():
#     sql_statement = "SELECT * FROM MoviesEmotionMap"
#     df = pd.read_sql(sql_statement, con=engine)
#     # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
#     df.to_csv("static/new_csv/new_data_cluster_emotion.csv", index=False)
#
#     # -----------------------------------------------------------------------------------------------------
#     sql_statement = "SELECT * FROM lvl2anger"
#     df = pd.read_sql(sql_statement,con=engine)
#     # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
#     df.to_csv("static/new_csv/ll.csv",index=False)
#     response = make_response(flask.send_file("static/new_csv/ll.csv"))
#     # response.headers['my-custom-header'] = 'my-custom-status-0'
#     #
#     # response.data = df.to_string()
#     return response
#     # return flask.send_file("lvl2_anger.csv",as_attachment=True, attachment_filename=df.to_csv("static/lvl2_anger.csv"))
#     # return flask.render_template('MoviesEmotionMap/map.html')

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def get_index():
    # getting the index.html (homepage)
    return render_template('index.html')

 
def load_dataJS(data):

    id_tuple = tuple(data)

    print("*********************************************************")
    query= 'SELECT * FROM MoviesEmotionMap WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/new_data_cluster_emotion.csv")


    
    query= 'SELECT * FROM lvl2anger WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_anger.csv")

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2anticipation WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_anticipation.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2disgust WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_disgust.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2fear WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_fear.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2joy WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_joy.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2sadness WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_sadness.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2surprise WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_surprise.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2trust WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    # return flask.render_template('MoviesEmotionMap/map.html',df.to_csv("static/lvl2_anger.csv") )
    df.to_csv("static/new_csv/lvl2_trust.csv", index=False)

    
    # -----------------------------------------------------------------------------------------------------



@app.route('/', methods=['GET', 'POST'])
def getJS_postMongoDB():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    if request.method == "POST":
        title = request.json['title']
        director = request.json['director']
        star = request.json['star']
        word = request.json['word']
        genre = request.json['genre']
        numberofmap = request.json['numberofmap']
        
        if title != '':
            load_dataJS(mf.getMoviesByTitle(title))
        if  director !='':
            print(mf.getMoviesForDirector(director))
            load_dataJS(mf.getMoviesForDirector(director))
        if star != '':
            load_dataJS(mf.getMoviesForStar(star))
        if  word != '':
            load_dataJS(mf.getMoviesIdByStringInReview(word))
        if  genre != '':
            print(mf.getMoviesByGenre(genre))
            load_dataJS(mf.getMoviesByGenre(genre))
        
        if numberofmap == -1:  
            load_data()
        
        app.config["TEMPLATES_AUTO_RELOAD"] =True
        # return redirect(request.referrer)
        
        return render_template('index.html')

    return render_template('index.html')
    # else: 
    #     r = make_response(render_template('index.html'))
    #     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    #     r.headers["Pragma"] = "no-cache"
    #     r.headers["Expires"] = "0"
    #     r.headers['Cache-Control'] = 'public, max-age=0'
    #     return r
    
       

        # print(mf.getMoviesByGenre("Action"), file=sys.stderr)
       
        # // then return something back to frontend on success
        # // this returns back received data and you should see it in browser console
        # // because of the console.log() in the script.
        
    
     
    
   
    
# function get from mongodb 
# function send to js

# ********   Main    ********
if __name__ == '__main__':
    # specify an ip address to make flask run on it
    ip="35.223.110.133"
    # specify the port that the web server is listening on
    port='80'
    # command to run the Flask application with the given configuration parameters
    #app.run(debug=True,host=ip, port=port)
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    # app.config["TEMPLATES_AUTO_RELOAD"] =True
    # app.run(debug=True)
    
    load_data()
    # app.run(host= ,port , debug=True)
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('10.128.0.6', 0))
    # port = sock.getsockname()[1]
    # sock.close()
    # print(port)
    # app_server = gevent.pywsgi.WSGIServer(('10.128.0.6', 5000), app)
    # app_server.serve_forever()
    app.run(host='0.0.0.0',port=5000, debug=True)
    