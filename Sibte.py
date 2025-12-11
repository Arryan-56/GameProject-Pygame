#=============================
#==Commit 9: Added FPS meter==
#=============================


fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
screen.blit(fps_text, (10, 10))


#=============================
#===Commit 10: Map Borders====
#=============================


# Prevent player from leaving window as it creates map borders
player_rect.x = max(0, min(player_rect.x, WIDTH - player_rect.width))
player_rect.y = max(0, min(player_rect.y, HEIGHT - player_rect.height))


#=============================
#==Commit 11: Pause Feature===
#=============================


paused = False

if event.key == pygame.K_p:
    paused = not paused

if paused:
    pause_text = font.render("Paused", True, WHITE)
    screen.blit(pause_text, (WIDTH//2 - 50, HEIGHT//2))
    pygame.display.update()
    continue



#=============================
#==Commit 12: BGM addition====
#=============================


pygame.mixer.init()

playlist = [
    "genesis.mp3",
    "ego.mp3",
    "ls_mob.mp3",
    "spacy_funk.mp3"
]

current_track = 0

def play_next_track():
    global current_track
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    current_track = (current_track + 1) % len(playlist)


play_next_track()


if not pygame.mixer.music.get_busy():
    play_next_track()

