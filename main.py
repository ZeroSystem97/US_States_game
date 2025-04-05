import turtle, pandas


from states import States
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. Sates Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = States()
correct_answers = []
scoreboard = Scoreboard()

while len(correct_answers) < 50:
    answer = turtle.textinput(title=f"{scoreboard.score}/50 States Correct", prompt="What's another state name?").title()

    if answer == "Exit":
        break

    if answer in states.names and answer not in correct_answers:
        correct_answers.append(answer)
        states.write_state(answer)
        scoreboard.increase_score()

# states to lear
states_to_learn = []
for name in states.names:
    if name not in correct_answers:
        states_to_learn.append(name)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_lear.csv")