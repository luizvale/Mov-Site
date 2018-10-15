import class_movie
import fresh_tomatoes

Monsters_sa = class_movie.Movie(9,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGF1JHDJXGFSlhNSDOS7r_vu2UHW5G6OVrbBcmHHs3tP1Kfvp3Rg",
                            " Um filme sobre Monstros", "Pete Docter", 
                            "Monstros S.A", "https://www.youtube.com/watch?v=iRh2kF-1X2E" )

Toy_story = class_movie.Movie(8,"https://imgc.allpostersimages.com/img/print/posters/toy-story-woody-buzz_a-G-13390942-0.jpg",
                                 "Um filme sobre brinquedos que falam","John Lasseter", 
                                 " Toy Story", "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

Os_incriveis = class_movie.Movie(6,"https://img.elo7.com.br/product/original/16571AC/painel-em-lona-1x70m-1x70.jpg",
                                    " Um filme sobre uma família de super-heróis!","Brad Bird",
                                 " Os Incríveis 2"," https://www.youtube.com/watch?v=zOZR0TRnSU8")

Avengers_3 = class_movie.Movie(1,"https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg", 
                                "Terceiro filme da franquia Vingadores da Marvel !", "Anthony Russo e Joe Russo",
                                 " Vingadores: Guerra Infinita", "https://www.youtube.com/watch?v=m2uqb2bt_bs")


labirinto_fauno = class_movie.Movie(10,"http://br.web.img3.acsta.net/c_215_290/medias/nmedia/18/87/14/49/19872468.jpg",
                                     " Uma menina que precisa completar 3 tarefas para se tornar imortal",
                                    "Guilherme Del Toro", "O Labirinto do Fauno", "https://www.youtube.com/watch?v=E7XGNPXdlGQ" )

watchmen = class_movie.Movie(12, "http://www.planocritico.com/wp-content/uploads/2016/06/watchmenn-600x400.jpg",
                                "Filme sobre super-herois aposentados", "Zack Snyder",
                                " Watchmen - The Movie", "https://www.youtube.com/watch?v=PVjA0y78_EQ")


movies = [Monsters_sa, Toy_story, Os_incriveis, Avengers_3,labirinto_fauno,watchmen] # lista com os filmes instanciados !
fresh_tomatoes.open_movies_page(movies) # criando a página !
