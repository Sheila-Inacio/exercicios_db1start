class Post:
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo


    def exibir(self):
        return f" [Titulo]: {self.titulo}\n [Conteudo]: {self.conteudo}"
    

class PostComVideo(Post):
    def __init__(self, titulo: str, conteudo: str, link_video: str):
        super().__init__(titulo,conteudo)
        self.link_video = link_video

    def exibir(self):
        return f"[Video:{self.link_video}]\n{super().exibir()}"
    
post_simples = Post('Bom dia', 'Bom dia amigos!') 
post_video = PostComVideo('Bom dia', 'Bom dia família!', 'http://youtube.com')
print(post_simples.exibir()) 
print(post_video.exibir()) 