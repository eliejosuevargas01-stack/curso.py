#faça um programa que abra e reproduza o audio de um arquivo mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load("./som.mp3")
pygame.mixer.music.play()
input("pressione Enter para encerrar a musica")