# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

sorcerers_stone = media.Movie("Harry Potter and the Sorcerer's Stone (2001)",
                              "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
                              "http://www.imdb.com/title/tt0241527/mediaviewer/rm683213568",
                              "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                              "IIA | 2h 32min | 7.5/10 | 20 December 2001 (Hong Kong)")
print(sorcerers_stone.storyline)
sorcerers_stone.show_trailer()

chamber_of_secrets = media.Movie("Harry Potter and the Chamber of Secrets (2002)",
                                 "Harry ignores warnings not to return to Hogwarts, only to find the school plagued by a series of mysterious attacks and a strange voice haunting him.",
                                 "http://www.imdb.com/title/tt0295297/mediaviewer/rm1029675264",
                                 "https://www.youtube.com/watch?v=1bq0qff4iF8",
                                 "PG | 2h 41min | 7.4/10 | 24 January 2003 (China)")
print(chamber_of_secrets.storyline)
chamber_of_secrets.show_trailer()

prisoner_of_azkaban = media.Movie("Harry Potter and the Prisoner of Azkaban (2004)",
                                 "It's Harry's third year at Hogwarts; not only does he have a new \"Defense Against the Dark Arts\" teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry.",
                                 "http://www.imdb.com/title/tt0304141/mediaviewer/rm3241184256",
                                 "https://www.youtube.com/watch?v=lAxgztbYDbs",
                                 "IIA | 2h 22min | 7.8/10 | 10 September 2004 (China)")
print(prisoner_of_azkaban.storyline)
prisoner_of_azkaban.show_trailer()

goblet_of_fire = media.Movie("Harry Potter and the Goblet of Fire (2005)",
                             "A young wizard finds himself competing in a hazard its tournament between rival schools of magic, but he is distracted by recurring nightmares.",
                             "http://www.imdb.com/title/tt0330373/mediaviewer/rm436509952",
                             "https://www.youtube.com/watch?v=3EGojp4Hh6I",
                             "13 | 2h 37min | 7.7/10 | 18 November 2005 (China)")
print(goblet_of_fire.storyline)
goblet_of_fire.show_trailer()

order_of_the_phoenix = media.Movie("Harry Potter and the Order of the Phoenix (2007)",
                                 "With their warning about Lord Voldemort's return scoffed at, Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
                                 "http://www.imdb.com/title/tt0373889/mediaviewer/rm103520512",
                                 "https://www.youtube.com/watch?v=y6ZW7KXaXYk",
                                 "IIA | 2h 18min | 7.5/10 | 10 August 2007 (China)")
print(order_of_the_phoenix.storyline)
order_of_the_phoenix.show_trailer()

half_blood_prince = media.Movie("Harry Potter and the Half-Blood Prince (2009)",
                                 "As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as \"the property of the Half-Blood Prince\" and begins to learn more about Lord Voldemort's dark past.",
                                 "http://www.imdb.com/title/tt0417741/mediaviewer/rm282560512",
                                 "https://www.youtube.com/watch?v=jpCPvHJ6p90",
                                 "IIA | 2h 33min | 7.5/10 | 15 July 2009 (China)")
print(half_blood_prince.storyline)
half_blood_prince.show_trailer()

deathly_hallows_1 = media.Movie("Harry Potter and the Deathly Hallows: Part 1 (2010)",
                                 "As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.",
                                 "http://www.imdb.com/title/tt0926084/mediaviewer/rm706774528",
                                 "https://www.youtube.com/watch?v=MxqsmsA8y5k",
                                 "PG-13 | 2h 26min | 7.7/10 | 19 November 2010 (China)")
print(deathly_hallows_1.storyline)
deathly_hallows_1.show_trailer()

deathly_hallows_2 = media.Movie("Harry Potter and the Deathly Hallows: Part 2 (2011)",
                                 "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
                                 "http://www.imdb.com/title/tt1201607/mediaviewer/rm1375082496",
                                 "https://www.youtube.com/watch?v=mObK5XD8udk",
                                 "PG-13 | 2h 10min | 8.1/10 | 4 August 2011 (China)")
print(deathly_hallows_2.storyline)
deathly_hallows_2.show_trailer()

# movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)
