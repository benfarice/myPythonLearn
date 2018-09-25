import media
import fresh_tomatoes
toy_story = media.Movie(
	"Toy Story",
	"A story of a boy and his toys that come to life",
	"https://imgc.allpostersimages.com/img/print/posters/toy-story-woody-buzz_a-G-13390942-0.jpg",
	"https://youtu.be/KYz2wyBy3kc"
	)
#print(toy_story.storyline)
avatar = media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"http://www.avatarmovie.com/assets/backgrounds/avtr-he-bg-02.jpg",
	"https://youtu.be/6ziBFh3V1aM"
	)
naruto = media.Movie(
	"Naruto",
	"A marine on an alien planet",
	"https://i.ytimg.com/vi/rhHf_GdJwnE/maxresdefault.jpg",
	"https://youtu.be/mksl3tYdyK4"
	)
#avatar.show_trailer()
movies=[toy_story,avatar,naruto]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATING)