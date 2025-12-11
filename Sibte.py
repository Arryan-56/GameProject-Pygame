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
