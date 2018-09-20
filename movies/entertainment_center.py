import media
import fresh_tomatoes
toy_story = media.Movie(
	"Toy Story",
	"A story of a boy and his toys that come to life",
	"https://i.ytimg.com/vi/rhHf_GdJwnE/maxresdefault.jpg",
	"https://youtu.be/kATywRaquhA"
	)
#print(toy_story.storyline)
avatar = media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"https://i.ytimg.com/vi/rhHf_GdJwnE/maxresdefault.jpg",
	"https://youtu.be/kATywRaquhA"
	)
#avatar.show_trailer()
movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)