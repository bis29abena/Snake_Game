from turtle import Turtle

POSITION = ((-100, 275), (100, 275))

with open("./scores.txt") as score:
    content_score: str = score.read()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.High_score = int(content_score)
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.High_score}", align="center", font=("Arial", 15, "normal"))

    def high_score(self):
        if self.score > self.High_score:
            self.High_score = self.score
        content = self.High_score
        with open("scores.txt", mode="w") as add_score:
            add_score.write(str(content))
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER ", align="center", font=("Arial", 24, "normal"))

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()





