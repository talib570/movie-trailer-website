# responsible for creating and
# rendering HTML for given movies
import fresh_tomatoes

# Movie class module
import media


# movie instance 1
godfather = media.Movie("The Godfather",
                        "The aging patriarch of an organized crime dynasty\
                         transfers control of his clandestine empire to his\
                         reluctant son.",
                        "images/god_1.jpg",
                        "sY1S34973zA",
                        "175",
                        "R",
                        "1972",
                        "godfather")

# movie instance 2
pirates_of_silicon_valley = media.Movie("Pirates of Silicon Valley",
                                        "History of Apple and Microsoft.",
                                        "images/pirates.jpg",
                                        "lEyrivrjAuU",
                                        "95",
                                        "PG-13",
                                        "1999",
                                        "pirates_of_silicon_valley")

# movie instance 3
trueman_show = media.Movie("The Trueman Show",
                           "An insurance salesman/adjuster discovers\
                           his entire life is actually a T.V. show.",
                           "images/trueman.jpg",
                           "loTIzXAS7v4",
                           "103",
                           "PG",
                           "1998",
                           "trueman")

# movie instance 4
braveheart = media.Movie("Braveheart",
                         "When his secret bride is executed for\
                         assaulting an English soldier who tried\
                         to rape her, William Wallace begins a revolt\
                         and leads Scottish warriors against the cruel\
                         English tyrant who rules Scotland with\
                         an iron fist.",
                         "images/braveheart.jpg",
                         "wj0I8xVTV18",
                         "178",
                         "PG-16",
                         "1995",
                         "braveheart")

# movie instance 5
apocalypse = media.Movie("Apocalypse Now",
                         "During the Vietnam War, Captain Willard\
                         is sent on a dangerous mission into Cambodia\
                         to assassinate a renegade colonel who has set\
                         himself up as a god among a local tribe.",
                         "images/apocalypse.jpg",
                         "IkrhkUeDCdQ",
                         "153",
                         "X",
                         "1979",
                         "apocalypse")

# movie instance 6
johnny_english = media.Movie("Johnny English Reborn",
                             "Johnny English goes up against international\
                             assassins hunting down the Chinese premier.",
                             "images/johnny_eng.jpg",
                             "Gh-Lubu94nA",
                             "101",
                             "PG",
                             "2011",
                             "johnny_english")

# creates list for all movies
movies = [godfather, pirates_of_silicon_valley,
          trueman_show, braveheart, apocalypse, johnny_english]

# calls fresh_tomatoes service for
# rendering and creating HTML page
fresh_tomatoes.open_movies_page(movies)
