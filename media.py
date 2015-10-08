import webbrowser


class Movie():
    """ This class provides a way to store movie related information."""

    def __init__(self, title, storyline, poster,
                 trailer, duration, rating, release_year, access_name):
        self.title = title
        self.storyline = storyline
        self.poster_url = poster
        self.rating = rating
        self.release_year = release_year
        self.trailer_url = trailer
        self.duration = duration
        self.rating = rating
        self.access_name = access_name

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

    def show_poster(self):
        print("Show poster image")

    def show_info(self):
        print("Show info")
