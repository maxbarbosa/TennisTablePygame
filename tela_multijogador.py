import pygame
import constantes as const
from pygame.locals import *
from sys import exit

def exibir_tela_multijogador():
    
    #PONTUAÇÃO
    sets_jogador1 = 0
    sets_jogador2 = 0

    pts_jogador1 = 0
    pts_jogador2 = 0
    
    pygame.init()

    const.tela

    #DEFININDO A FONTE USADA PARA EXIBIR O PLACAR
    fonteTexto = pygame.font.SysFont(const.fonte, 18, True)
    fonteNumero = pygame.font.SysFont(const.fonte, 25, True)

    while True:
        const.relogio.tick(const.fps)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        #DESENHANDO A REGIÃO DO PLANO DE FUNDO, PLACAR E MESA
        const.tela.fill(const.plano_de_fundo_partida)
        pygame.draw.rect(const.tela, const.cor_verde, (0, 0, const.largura, 120))
        pygame.draw.rect(const.tela, const.cor_cinza, (890, 15, 175, 70))
        pygame.draw.rect(const.tela, const.cor_da_borda, (1015, 15, 100, 70))
        pygame.draw.line(const.tela, const.cor_da_borda, (890, 50), (1035, 50), 1)
        pygame.draw.line(const.tela, const.cor_cinza, (1015, 50), (1114, 50), 1)
        pygame.draw.line(const.tela, const.cor_cinza, (1065, 15), (1065, 85), 1)
        pygame.draw.rect(const.tela, const.cor_da_mesa, (100, 120, 920, 500))
        
        #DESENHANDO AS BORDAS ESQUERDA E DIREITA DA MESA
        pygame.draw.line(const.tela, const.cor_da_borda, (104, 120), (104, 619), 10)
        pygame.draw.line(const.tela, const.cor_da_borda, (1014, 120), (1014, 619), 10)
        
        #DESENHANDO AS BORDAS SUPERIOR E INFERIOR DA MESA
        pygame.draw.line(const.tela, const.cor_da_borda, (100, 124), (1019, 124), 10)
        pygame.draw.line(const.tela, const.cor_da_borda, (100, 614), (1019, 614), 10)
        
        #DESENHANDO REDE E LINHA DIVISÓRIA DA MESA
        pygame.draw.line(const.tela, const.cor_da_rede, (559, 124), (559, 614), 10)
        pygame.draw.aaline(const.tela, const.cor_da_rede, (100, 370), (1019, 370))

        #EXIBINDO A PONTUAÇÃO NA TELA
        nome_jogador1 = fonteTexto.render("Jogador A", True, const.cor_da_borda)
        nome_jogador2 = fonteTexto.render("Jogador B", True, const.cor_da_borda)

        pontuacao1_set = "%d" %(sets_jogador1)
        pontuacao2_set = "%d" %(sets_jogador2)

        pontuacao1 = "%d" %(pts_jogador1)
        pontuacao2 = "%d" %(pts_jogador2)

        pts_set_j1 = fonteNumero.render(pontuacao1_set, True, const.cor_preta)
        pts_set_j2 = fonteNumero.render(pontuacao2_set, True, const.cor_preta)

        p1_formatado = fonteNumero.render(pontuacao1, True, const.cor_preta)
        p2_formatado = fonteNumero.render(pontuacao2, True, const.cor_preta)

        const.tela.blit(nome_jogador1, (900, 19))
        const.tela.blit(nome_jogador2, (900, 55))
        const.tela.blit(pts_set_j1, (1022, 17))
        const.tela.blit(pts_set_j2, (1022, 53))
        const.tela.blit(p1_formatado, (1072, 17))
        const.tela.blit(p2_formatado, (1072, 53))
        
        pygame.display.flip()

exibir_tela_multijogador()