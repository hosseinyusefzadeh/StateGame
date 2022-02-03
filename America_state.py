import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_list = []

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct ", prompt="What's another state's names? ").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in all_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("learned_states.csv")
        break
    if answer_state in all_states:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
