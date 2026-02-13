
#This programme will help farmers to calculate the seed quantity required for planting a specific area of land. It takes into account the seed rate (the amount of seed needed per unit area) and the total area to be planted, and then calculates the total seed quantity needed.
import pygame # type: ignore
import time
import random

width,height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Seed Calculator")
font = pygame.font.SysFont("Arial", 30)
def calculate_seed_quantity(seed_rate, area):
    return seed_rate * area
def main():
    running = True
    seed_rate = 0
    area = 0
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    seed_quantity = calculate_seed_quantity(seed_rate, area)
                    print(f"Total Seed Quantity Needed: {seed_quantity} kg")
                elif event.key == pygame.K_BACKSPACE:
                    seed_rate = 0
                    area = 0
                else:
                    try:
                        seed_rate = int(event.unicode)
                        area = int(event.unicode)
                    except ValueError:
                        pass
        
        seed_rate_text = font.render(f"Seed Rate (kg/ha): {seed_rate}", True, (0, 0, 0))
        area_text = font.render(f"Area (ha): {area}", True, (0, 0, 0))
        screen.blit(seed_rate_text, (50, 50))
        screen.blit(area_text, (50, 100))
        
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()


