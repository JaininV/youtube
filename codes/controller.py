#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from video_alag import split_video_with_labels
import asyncio

def videoSplitApi():
    data = request.form
    page = split_video_with_labels(data)
    return page
