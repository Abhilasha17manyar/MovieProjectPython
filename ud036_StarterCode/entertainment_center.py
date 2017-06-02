import fresh_tomatoes
import media

#ChiSauka = media.Movie("Chi va Chi Sau Ka","Marathi movie, story of different Arrange Marriage","https://www.youtube.com/watch?v=T54iydLS7V0","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=7s")
#sairat = media.Movie("Sairat","Lovestory","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=wMrMKnoYWwA&t=1s")

bahubalimovie = media.Movie("Bahubali 1","A story of king","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=sOEg_YZQsTI")

Bahubali2 = media.Movie("Bahubali 2","A story of king","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=veGwOqmgBGs")


kaytar = media.Movie("katyar Kaljat Ghusli","Misical Treat","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=1iTazEogwiY")


postergirl = media.Movie("Poster Girl","story about girl","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=2ozdyvwaEZk")


zindagina = media.Movie("Zindagi Na Milegi Dobara","A story 3 friends","https://en.wikipedia.org/wiki/Zindagi_Na_Milegi_Dobara#/media/File:Zindaginamilegidobara.jpg","https://www.youtube.com/watch?v=ifIBOKCfjVs")

jabwemet = media.Movie("Jab We Meet","A story of girl, who loves herself too much","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=i7VGyugYCIk")

loveuzindagi = media.Movie("Love You Zindagi","A story of girl, who loves herself too much","https://www.youtube.com/watch?v=vsJ62RHUwJg&t=5s","https://www.youtube.com/watch?v=5DkO7ksXY8E")

movies = [kaytar, postergirl, bahubalimovie, Bahubali2, zindagina, jabwemet, loveuzindagi]

fresh_tomatoes.open_movies_page(movies)

#print(bahubalimovie.storyline)
#bahubalimovie.show_trailer()
