import cv2
import pygame
from game.player import Player
from game.game_engine import GameEngine
from handtracking.tracker import HandTracker

def main():
    pygame.init()
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    player = Player(300, 400)
    game = GameEngine(player)
    running = True

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        hand_x, _, annotated_frame = tracker.get_hand_position(frame)
        if hand_x:
            mapped_x = int((hand_x / frame.shape[1]) * game.width)
        else:
            mapped_x = player.rect.x

        running = game.run_frame(mapped_x)

        cv2.imshow("Hand Tracking", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    main()
