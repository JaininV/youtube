from flask import Blueprint,  jsonify
from controller import videoSplitApi

video_split = Blueprint('video_split', __name__)
@video_split.route('/split_video', methods=['GET'])
def video_split_api():
    page = videoSplitApi()
    return page
