import pygame 
# Esse biblioteca server para criar jogos, pórem no momento eu estou utilizando ela para tocar músicas

pygame.init() # inicializar o pygame no código

pygame.mixer.init() # esse comando server para incializar a produção de música no seu codigo
pygame.mixer.music.load('caminho musica') # Esse comando recebe como parametro o caminho da musica para ela ser carregada
pygame.mixer.music.play() # play na música

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10) 

# linha 10/12 - O while é o loop que quando tiver tocando uma música recebera True é quando a música parar de tocar o valor será false parando o codigo
# pygame.mixer.music.get_busy() é usado para garantir que a música seja reproduzida até o final antes de o programa terminar.
# pygame.time.Clock().tick(10) é chamada a cada iteração do loop. Isso faz com que o loop espere 10 milissegundos antes de continuar com a próxima iteração.

