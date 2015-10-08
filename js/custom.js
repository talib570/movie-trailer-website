// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var movie = $(this).attr('data-movie');
    var sourceUrl = 'http://www.youtube.com/embed/' + movies[movie].youtube_url_id + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($('<div class="col-lg-7" id="video-container"></div>'));
    $('#video-container').empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
    $("#trailer-video-container").append($("<div class='col-lg-5'><h2>"+
                                                                movies[movie].title+
                                                                "</h2><div><img class='poster_img' src='"+
                                                                movies[movie].poster+
                                                                "' /><div class='movie_info'>"+
                                                                movies[movie].rating+" | "+
                                                                movies[movie].duration+" mins |  "+
                                                                movies[movie].release_year +
                                                                "</div></div><div class='clearfix'></div><p>"+
                                                                movies[movie].storyline+"</p></div>"));
});
// Animate in the movies when the page loads
$(document).ready(function () {
  $('.movie-tile').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});