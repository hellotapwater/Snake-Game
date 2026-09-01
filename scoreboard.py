from turtle import Turtle
ALLIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

with open("data.txt", "r") as high_score:
    highscore = int(high_score.read())
    print(highscore)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = highscore
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALLIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            output_number = str(self.high_score)
            with open("data.txt", "w") as update:
                update.write(output_number)
                update.close()

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALLIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

