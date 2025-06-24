from flask import Flask, request, jsonify
from route import video_split

app = Flask(__name__)

app.register_blueprint(video_split, url_prefix = '/api')

# start server
if (__name__ == '__main__'):
    app.run(debug=True)

    