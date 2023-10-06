class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(pins)

    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def score(self, next_frame, next_next_frame=None):
        frame_score = sum(self.rolls)

        if self.is_strike():
            if next_frame:
                frame_score += next_frame.score(next_next_frame)
        elif self.is_spare():
            if next_frame:
                frame_score += next_frame.rolls[0]

        return frame_score


class BowlingGame:
    def __init__(self):
        self.frames = [Frame() for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        if self.current_frame >= 10:
            raise ValueError("The game has ended.")

        current_frame = self.frames[self.current_frame]
        current_frame.add_roll(pins)

        if current_frame.is_strike() or len(current_frame.rolls) == 2:
            self.current_frame += 1

    def calculate_score(self):
        total_score = 0
        for i in range(10):
            frame = self.frames[i]
            if i == 9:
                total_score += frame.score(None)
            else:
                next_frame = self.frames[i + 1]
                if frame.is_strike():
                    next_next_frame = self.frames[i + 2] if i + 2 < 10 else None
                    total_score += frame.score(next_frame, next_next_frame)
                elif frame.is_spare():
                    total_score += frame.score(next_frame)
                else:
                    total_score += frame.score(None)

        return total_score


# Ejemplo de uso:
game = BowlingGame()
rolls = [10, 5, 5, 9, 0, 10, 10, 10, 10, 5, 5, 5]
for roll in rolls:
    game.roll(roll)

score = game.calculate_score()
print("Puntaje total:", score)
