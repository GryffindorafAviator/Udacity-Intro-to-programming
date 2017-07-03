# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Video():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        

class Movie():
    # This class provides a way to store movie related information
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, duration, ratings):
        self.duration = duration
        self.ratings = ratings

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
class TV_show:
    def __init__(self, season, episode, TV_station):
        self.season = season
        self.episode = episode
        self.TV_station = TV_station
