'''Faça um script que abra e reproduza o áudio de um arquivo mp3.'''

print("•••PLAYER MP3•••")

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer_music.load('ex021musica.mp3')
pygame.mixer_music.play()
pygame.event.wait()

'''► init é  utilizado para iniciar o mixer do pygame
► event.wait utilizado para esperar o evento encerrar'''
