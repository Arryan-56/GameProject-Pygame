#=============================
#==Commit 9: Added FPS meter==
#=============================


fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
screen.blit(fps_text, (10, 10))
