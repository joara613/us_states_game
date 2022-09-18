import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # States to learn.csv
        states_to_learn = [state for state in all_states if state not in guessed_states]
        data_to_learn = pandas.DataFrame(states_to_learn)
        data_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            pen.goto(int(state_data.x), int(state_data.y))
            pen.write(f"{answer_state}", False, align='left', font=('Arial', 10, 'normal'))


screen.exitonclick()