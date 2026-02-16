
#This programme will help farmers to calculate the seed quantity required for planting a specific area of land. It takes into account the seed rate (the amount of seed needed per unit area) and the total area to be planted, and then calculates the total seed quantity needed.
import pygame
import random
import sys

# --- CONFIGURATION ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (30, 30, 30)       # Dark gray (VS Code style)
TEXT_COLOR = (255, 255, 255)  # White
MATCH_COLOR = (0, 255, 0)     # Green for correct typing
FAIL_COLOR = (255, 50, 50)    # Red for game over
FONT_SIZE = 50
FALL_SPEED = 1                # How fast words fall

# A list of Python keywords to practice typing
KEYWORDS = [
    "def", "return", "class", "import", "from", "if", "else", 
    "elif", "while", "for", "try", "except", "finally", 
    "with", "as", "lambda", "yield", "async", "await", 
    "continue", "break", "pass", "global", "assert"
]

# --- SETUP ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Syntax Rain - Python Typing Practice")
font = pygame.font.SysFont("Consolas", FONT_SIZE) # Monospaced font looks 'code-like'

def get_new_word():
    """Pick a random word and start it at a random X position at the top."""
    word = random.choice(KEYWORDS)
    x_pos = random.randint(50, SCREEN_WIDTH - 200)
    return {"text": word, "x": x_pos, "y": -50}

def main():
    clock = pygame.time.Clock()
    
    # Game State Variables
    current_target = get_new_word()
    user_input = ""
    score = 0
    game_over = False

    while True:
        # 1. EVENT HANDLING (Mouse & Keyboard inputs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    # Add typed character to our buffer
                    user_input += event.unicode

            # Restart game if Enter is pressed after Game Over
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    # Reset variables
                    game_over = False
                    score = 0
                    current_target = get_new_word()
                    user_input = ""

        # 2. GAME LOGIC (Updates)
        if not game_over:
            # Move the word down
            current_target["y"] += FALL_SPEED + (score * 0.1) # Gets faster as you score higher

            # Check if word hit the bottom
            if current_target["y"] > SCREEN_HEIGHT:
                game_over = True
            
            # Check if user typed the word correctly
            if user_input == current_target["text"]:
                score += 1
                user_input = "" # Clear input
                current_target = get_new_word() # Spawn new word

        # 3. DRAWING (Rendering to screen)
        screen.fill(BG_COLOR)

        if not game_over:
            # Render the Score
            score_surf = font.render(f"Score: {score}", True, (100, 100, 100))
            screen.blit(score_surf, (10, 10))

            # Render the Falling Word
            target_surf = font.render(current_target["text"], True, TEXT_COLOR)
            screen.blit(target_surf, (current_target["x"], current_target["y"]))

            # Render what the User is typing
            # We draw it in green if it matches the start of the target, else red
            input_color = MATCH_COLOR if current_target["text"].startswith(user_input) else FAIL_COLOR
            input_surf = font.render(user_input, True, input_color)
            
            # Center the user input at the bottom
            input_rect = input_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
            screen.blit(input_surf, input_rect)
            
        else:
            # Game Over Screen
            game_over_surf = font.render("GAME OVER", True, FAIL_COLOR)
            final_score_surf = font.render(f"Final Score: {score}", True, TEXT_COLOR)
            restart_surf = font.render("Press ENTER to restart", True, (200, 200, 200))
            
            screen.blit(game_over_surf, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 60))
            screen.blit(final_score_surf, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2))
            screen.blit(restart_surf, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 + 60))

        # Update the display
        pygame.display.flip()
        
        # Limit frame rate to 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()


