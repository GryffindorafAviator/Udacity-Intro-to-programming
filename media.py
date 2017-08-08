import webbrowser
# To import class webbrowser is to open a web browser to play the trailer of the movie or the TV show.

class Video():
    """
    This class used to define these common attributes belong to both class Movie and class TV_show.
    """
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        print("Video constructor called")
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie(Video):
    """
    This class used to define these attributes only belong to class Movie.
    This class provides a way to store movie related information.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, information):
        print("Movie constructor called")
        Video.__init__(self, title, storyline, poster_image_url, trailer_youtube_url)
        self.information = information

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TV_show(Video):
    """
    This class used to define these attributes only belong to class TV_show.
    This class provides a way to store TV_show related information.
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, information):
        Video.__init__(self, title, storyline, poster_image_url, trailer_youtube_url)
        self.information = information

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
