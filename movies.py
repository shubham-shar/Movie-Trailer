import movies_info
import fresh_tomatoes

Wonder_Woman = movies_info.Movie("Wonder Woman",
                                 "A superfemale which put her powers to use in a world war.",
                                 "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                                 "https://www.youtube.com/watch?v=VSB4wGIdDwo")

Spider_man = movies_info.Movie("Spider-Man: Homecoming",
                               "Boy who turn into a superhero when bitten by a spider.",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                               "https://www.youtube.com/watch?v=39udgGPyYMg")

Thor_Ragnarok = movies_info.Movie("Thor: Ragnarok",
                                  "Thor battles Hela to save his world and Asgardain civilization.",
                                  "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                                  "https://www.youtube.com/watch?v=v7MGUNV8MxU")

War_for_the_planet_of_the_apes = movies_info.Movie("War For The Planet Of The Apes",

                                                   "Caesar and his apes are forced into a deadly" +
                                                   " conflict with an army of humans.",

                                                   "https://upload.wikimedia.org/wikipedia/en/d/d7/W" +
                                                   "ar_for_the_Planet_of_the_Apes_poster.jpg",

                                                   "https://www.youtube.com/watch?v=JDcAlo8i2y8")

mummy = movies_info.Movie("The Mummy",
                          "A princess thought to be dead, emerges back to terrorize the world again.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
                          "https://www.youtube.com/watch?v=vJxgxVH0Fsk")

Transformers = movies_info.Movie("Transformers: The Last Knight",
                                 "Humans are at war with the Transformers, and Optimus Prime is gone.",
                                 "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
                                 "https://www.youtube.com/watch?v=sQm3djLYWB8&pbjreload=10")

movies = [Wonder_Woman, Spider_man, Thor_Ragnarok, War_for_the_planet_of_the_apes, mummy, Transformers]

fresh_tomatoes.open_movies_page(movies)
