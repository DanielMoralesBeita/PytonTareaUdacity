"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    optimus = media.Movie("Transformers: The Last Knight",
                          "In the absence of Optimus Prime, a war has commenced between the human race and the Transformers. To save their world, Cade Yeager forms an alliance with Bumblebee, an English lord named Sir Edmund Burton, and an Oxford University professor named Viviane Wembly to learn the secrets of why the Transformers keep coming back to Earth.",
                          "https://upload.wikimedia.org/wikipedia/en/2/26/"
                          "Transformers_The_Last_Knight_poster.jpg",
                          "https://www.youtube.com/watch?v=lQqhfq87FgY",
                          "June 21, 2017")

  

    matrix = media.Movie("The Matrix",
                         "The world is a simulation and Neo have super powers",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                         "March 31, 1999")

    tWonder_Woman= media.Movie("Wonder Woman (2017 film)",
                           "Wonder Woman is a 2017 American superhero film based on the DC Comics character of the same name, distributed by Warner Bros.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
                           "June 2, 2017")


    # Store the Movie objects in a list.
    movies = [optimus, matrix, tWonder_Woman]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
