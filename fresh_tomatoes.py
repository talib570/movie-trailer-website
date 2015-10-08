import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet"
          href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet"
          href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script
        src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js">
    </script>
    <script type="text/javascript" charset="utf-8">
        // contains movie object
        var movies = {movie_list}
    </script>
    <script src="js/custom.js"></script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close"
             data-dismiss="modal" aria-hidden="true">
            <img src="images/close.png"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
    {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4
     movie-tile text-center" data-movie="{access_name}"
     data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_object(movies):
    # creates the json object for movies

    json_object = '{'
    i = 0
    for movie in movies:
        json_object += '"'+movie.access_name+'":{"title":"'+movie.title+'",'
        json_object += '"storyline":"' + movie.storyline + '",'
        json_object += '"poster":"' + movie.poster_url + '",'
        json_object += '"youtube_url_id":"' + movie.trailer_url + '",'
        json_object += '"duration":"' + movie.duration + '",'
        json_object += '"rating":"' + movie.rating + '",'
        json_object += '"release_year":"' + movie.release_year

        if(i == len(movies)-1):
            json_object += '"}'
        else:
            json_object += '"},'

        i = i+1
    json_object += '}'
    return json_object


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_url,
            trailer_youtube_id=movie.trailer_url,
            access_name=movie.access_name
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace movie object in script section
    rendered_header = main_page_head.format(
                                        movie_list=create_movie_object(movies))

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
                                        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_header + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)