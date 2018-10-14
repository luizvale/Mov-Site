import webbrowser

class Movie:
    ''' 
        Recebe como parâmetro uma nota, URL de imagem, um pequeno resumo, o diretor,
         titulo original e a URL do trailer 
                                   '''
    def __init__(self, nota, poster_image_url, Resumo, Diretor, title,trailer_youtube_url):
        def avaliacao(nota):
            return float(nota) if nota <= float(10) else "Verifique se foi digitado uma valor entre 0 e 10"  # Evita que seja apresentada uma nota maior que 10.  
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.Resumo = Resumo                 # Variáveis de instância 
        self.Diretor = Diretor
        self.nota = avaliacao(nota)

    def __repr__(self): # representação do objeto
        return 'Titulo: %r\n Resumo: %r\n Diretor: %r\n Rating: %s ' % (self.title, self.Resumo, self.Diretor, self.nota)
    

    def show_video(self, trailer_youtube_url): # Inicia no navegador o trailer do filme ! 
        return webbrowser.open(self.trailer_youtube_url)
