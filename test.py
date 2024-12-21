# import pygame
# import sys
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the screen
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Fade Transition")
#
# # Define colors
# black = (0, 0, 0)
# white = (255, 255, 255)
#
# # Create a surface for the fade effect
# fade_surface = pygame.Surface((screen_width, screen_height))
# fade_surface.fill(black)
#
# def fade_in(screen, fade_surface, duration):
#     """Fade in the screen."""
#     for alpha in range(255, -1, -5):  # Gradually decrease alpha
#         fade_surface.set_alpha(alpha)
#         screen.fill(white)  # Background color
#         screen.blit(fade_surface, (0, 0))
#         pygame.display.flip()
#         pygame.time.delay(duration)
#
# def fade_out(screen, fade_surface, duration):
#     """Fade out the screen."""
#     for alpha in range(0, 256, 5):  # Gradually increase alpha
#         fade_surface.set_alpha(alpha)
#         screen.fill(white)  # Background color
#         screen.blit(fade_surface, (0, 0))
#         pygame.display.flip()
#         pygame.time.delay(duration)
#
# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Example usage: Fade in and fade out
#     fade_in(screen, fade_surface, 30)  # Fade in with 30ms delay
#     pygame.time.delay(1000)           # Hold the screen for a moment
#     fade_out(screen, fade_surface, 30)  # Fade out with 30ms delay
#     pygame.time.delay(1000)           # Hold the screen for a moment
#
# # Quit Pygame
# pygame.quit()
# sys.exit()


