import fresh_tomatoes
import media  # media file imported for the class Movie

""" Created object,pass value to the Movie class
 Movie("self",moivename,storyline,imageurl,movietailerurl) """

ChiSauka = media.Movie("Chi va Chi Sau Ka", "Marathi movie,story of different/"
                       "Arrange Marriage",
                       "http://cdn1.marathistars.com/wp-content/uploads/2017//"
                       "05/Chi-Va-Chi-Sau-Ka-Marathi-Movie.jpg",
                       "https://www.youtube.com/watch?v=gzdLUpqkoxo")

bahubalimovie = media.Movie("Bahubali The Beginnig", "Bahubali is a 2015/"
                            "Indian epic historical fiction film directed by/"
                            "S. S. Rajamouli",
                            "https://upload.wikimedia.org/wikipedia/en/7/7e//"
                            "Baahubali_poster.jpg",
                            "https://www.youtube.com/watch?v=VdafjyFK3ko")

Bahubali2 = media.Movie("Bahubali 2 : The Conclusion", "It is the /"
                        "continuation of Baahubali: The Beginning, taking /"
                        "place before and after the events of that film.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9//"
                        "Baahubali_the_Conclusion.jpg",
                        "https://www.youtube.com/watch?v=veGwOqmgBGs")


katyar = media.Movie("katyar Kaljat Ghusli", "Misical Treat",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/3//"
                     "35/Katyar_Kaljat_Ghusali_%28film%29.jpg//"
                     "220px-Katyar_Kaljat_Ghusali_%28film%29.jpg",
                     "https://www.youtube.com/watch?v=1iTazEogwiY")


postergirl = media.Movie("Poshter Girl", "Poshter Girl takes you on a mad/"
                         "roller coaster ride of a quaint, little village in/"
                         "Maharashtra. a beautiful and Intelligent girl/"
                         "enters the scenario and changes everything.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/7//"
                         "7f/Poshter_Girl_Official_Poster.jpeg//"
                         "220px-Poshter_Girl_Official_Poster.jpeg",
                         "https://www.youtube.com/watch?v=2ozdyvwaEZk")


zindagina = media.Movie("Zindagi Na Milegi Dobara", "The story follows three/"
                        "friends,who have been inseparable since childhood.",
                        "https://upload.wikimedia.org/wikipedia/en/3//"
                        "3d/Zindaginamilegidobara.jpg",
                        "https://www.youtube.com/watch?v=ifIBOKCfjVs")

jabwemet = media.Movie("Jab We Meet", "The film tells the story of a feisty/"
                       "Punjabi girl who is sent off track when she bumps /"
                       "into a depressed Mumbai businessman",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f//"
                       "Jab_We_Met_Poster.jpg/220px-Jab_We_Met_Poster.jpg",
                       "https://www.youtube.com/watch?v=i7VGyugYCIk")

loveuzindagi = media.Movie("Love You Zindagi", "The plot centers on a budding/"
                           "cinematographer named Kaira, who is discontented /"
                           "with her life and meets Dr. Jehangir,/"
                           "a free-spirited psychologist who helps her to /"
                           "gain a new perspective on her life.",
                           "https://upload.wikimedia.org/wikipedia/en/9//"
                           "9e/Dear_Zindagi_poster.jpg",
                           "https://www.youtube.com/watch?v=5DkO7ksXY8E")

findingdory = media.Movie("Finding Dory", "Story of Dory fish",
                          "https://vignette3.wikia.nocookie.net/pixar/images//"
                          "1/1b/Finding_Dory_Screenshot_0089.jpg/revision//"
                          "latest/scale-to-width-down/1000?cb=20161030192450",
                          "https://www.youtube.com/watch?v=otnKrHHFx80")
# movies array is created
movies = [findingdory, bahubalimovie, Bahubali2, zindagina, jabwemet,
          loveuzindagi, katyar, postergirl, ChiSauka]

# movie array is passed to function open_movie_page()
fresh_tomatoes.open_movies_page(movies)
