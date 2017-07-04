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
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube

class Movie(Video):
    # This class provides a way to store movie related information

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image, trailer_youtube, information):
        print("Movie constructor called")
        Video.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.information = information

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)

# class TV_show(Video):
#     def __init__(self, title, storyline, poster_image, trailer_youtube, season, episode, TV_station):
#         Video.__init__(title, storyline, poster_image, trailer_youtube)
#         self.season = season
#         self.episode = episode
#         self.TV_station = TV_station

# harry_potter = Video("Harry Potter and the Sorcerer's Stone (2001)",
#                      "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
#                      "http://www.imdb.com/title/tt0241527/mediaviewer/rm683213568",
#                      "https://www.youtube.com/watch?v=VyHV0BRtdxo")
# print(harry_potter.storyline)
# harry_potter.trailer_youtube

ron = Movie("Harry Potter and the Sorcerer's Stone (2001)",
            "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
            "http://www.imdb.com/title/tt0241527/mediaviewer/rm683213568",
            "https://www.youtube.com/watch?v=VyHV0BRtdxo",
            "IIA | 2h 32min | 7.5/10 | 20 December 2001 (Hong Kong)")
print(ron.storyline)
print(ron.information)
