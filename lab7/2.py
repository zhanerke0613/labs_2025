import pygame
import os


pygame.init()
pygame.mixer.init()


MUSIC_FOLDER = "music"
music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

if not music_files:
    print(" В папке 'music' нет MP3 файлов!")
    exit()

current_track = 0  


def load_and_play(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, music_files[index]))
    pygame.mixer.music.play()
    print(f"🎵 Playing: {music_files[index]}")


load_and_play(current_track)


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player ")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print(" Music Paused")
                else:
                    pygame.mixer.music.unpause()
                    print(" Resuming Music")

            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
                print(" Music Stopped")

            elif event.key == pygame.K_n:  
                current_track = (current_track + 1) % len(music_files)
                load_and_play(current_track)

            elif event.key == pygame.K_p:  
                current_track = (current_track - 1) % len(music_files)
                load_and_play(current_track)

pygame.quit()