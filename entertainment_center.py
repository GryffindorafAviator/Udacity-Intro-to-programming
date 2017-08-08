# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

#class media defined these attributes belong to Movie and TV_show.
#class fresh_tomatoes is used to create an HTML file.

#define variables for movies

sorcerers_stone = media.Movie("Harry Potter and the Sorcerer's Stone (2001)",
                              "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
                              "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/a/5/a58765ca101c2bbe46226972d72db96f230a1b5e_1_337x500.jpg",
                              "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                              "IIA | 2h 32min | 7.5/10 | 20 December 2001 (Hong Kong)")

chamber_of_secrets = media.Movie("Harry Potter and the Chamber of Secrets (2002)",
                                 "Harry ignores warnings not to return to Hogwarts, only to find the school plagued by a series of mysterious attacks and a strange voice haunting him.",
                                 "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/3/8/38379ab8012d25ca44e67c92de0346300f45ca6c_1_338x500.jpg",
                                 "https://www.youtube.com/watch?v=1bq0qff4iF8",
                                 "PG | 2h 41min | 7.4/10 | 24 January 2003 (China)")

prisoner_of_azkaban = media.Movie("Harry Potter and the Prisoner of Azkaban (2004)",
                                 "It's Harry's third year at Hogwarts; not only does he have a new \"Defense Against the Dark Arts\" teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry.",
                                 "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/0/3/033071106650b82c7ae3f560df8cabf12d89959e_1_338x500.jpg",
                                 "https://www.youtube.com/watch?v=lAxgztbYDbs",
                                 "IIA | 2h 22min | 7.8/10 | 10 September 2004 (China)")

goblet_of_fire = media.Movie("Harry Potter and the Goblet of Fire (2005)",
                             "A young wizard finds himself competing in a hazard its tournament between rival schools of magic, but he is distracted by recurring nightmares.",
                             "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/original/3X/a/e/ae3ac8e98e5324f35698ab08b291af6ecaeadef0.jpg",
                             "https://www.youtube.com/watch?v=3EGojp4Hh6I",
                             "13 | 2h 37min | 7.7/10 | 18 November 2005 (China)")

order_of_the_phoenix = media.Movie("Harry Potter and the Order of the Phoenix (2007)",
                                 "With their warning about Lord Voldemort's return scoffed at, Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
                                 "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/a/4/a4e764bfcf63ef36c7e5f25f1ff60416c1d02590_1_337x499.jpg",
                                 "https://www.youtube.com/watch?v=y6ZW7KXaXYk",
                                 "IIA | 2h 18min | 7.5/10 | 10 August 2007 (China)")

half_blood_prince = media.Movie("Harry Potter and the Half-Blood Prince (2009)",
                                 "As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as \"the property of the Half-Blood Prince\" and begins to learn more about Lord Voldemort's dark past.",
                                 "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/9/2/921500755df81a2cc9a7496e84ac90cc59fb4503_1_324x500.jpg",
                                 "https://www.youtube.com/watch?v=jpCPvHJ6p90",
                                 "IIA | 2h 33min | 7.5/10 | 15 July 2009 (China)")

deathly_hallows_1 = media.Movie("Harry Potter and the Deathly Hallows: Part 1 (2010)",
                                 "As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.",
                                 "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/0/d/0d97a745ecc797207c5aa490eb2dac1f5c2b2bd1_1_337x500.jpg",
                                 "https://www.youtube.com/watch?v=MxqsmsA8y5k",
                                 "PG-13 | 2h 26min | 7.7/10 | 19 November 2010 (China)")

deathly_hallows_2 = media.Movie("Harry Potter and the Deathly Hallows: Part 2 (2011)",
                                 "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
                                 "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/3/5/35985e88245abde9d7345afd6a2e2c5323ad9233_1_333x500.jpg",
                                 "https://www.youtube.com/watch?v=mObK5XD8udk",
                                 "PG-13 | 2h 10min | 8.1/10 | 4 August 2011 (China)")

the_flash = media.TV_show("The Flash",
                          "After being struck by lightning, Barry Allen wakes up from his coma to discover he's been given the power of super speed, becoming the Flash, fighting crime in Central City.",
                          "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/0/e/0e68e0b00023f181b05075cf6c616fbae7518e30_1_397x500.jpg",
                          "https://www.youtube.com/watch?v=Yj0l7iGKh8g",
                          "Season 4 | 8.1/10 | 2014 - ")

sherlock = media.TV_show("Sherlock",
                         "A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.",
                         "https://cn-discussions.s3.cn-north-1.amazonaws.com.cn/optimized/3X/5/8/58762869d0a2941c4c4babcdf5d12059bc4c548b_1_336x500.jpg",
                         "https://www.youtube.com/watch?v=38_c6dh6Y6M",
                         "15 episodes | 9.2/10 | 2010 -")

movies = [sorcerers_stone, chamber_of_secrets, prisoner_of_azkaban, goblet_of_fire, order_of_the_phoenix, half_blood_prince, deathly_hallows_1, deathly_hallows_2, the_flash, sherlock]
fresh_tomatoes.open_movies_page(movies)
