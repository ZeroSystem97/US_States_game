import pandas
from turtle import Turtle

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.names = self.data.state.to_list()
        self.hideturtle()
        self.penup()

    def write_state(self, answer):
        cur_state = self.data[self.data.state == answer]
        self.goto(x=cur_state.x.item(), y=cur_state.y.item())
        self.write(answer, align="center", font=("Arial", 8, "bold"))