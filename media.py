# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Video():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        print("Video constructor called")
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie(Video):
    # This class provides a way to store movie related information

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, information):
        print("Movie constructor called")
        Video.__init__(self, title, storyline, poster_image_url, trailer_youtube_url)
        self.information = information

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TV_show(Video):
    # This class provides a way to store TV_show related information

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, information):
        Video.__init__(self, title, storyline, poster_image_url, trailer_youtube_url)
        self.information = information

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
