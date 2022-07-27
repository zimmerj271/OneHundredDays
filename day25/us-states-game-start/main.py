import turtle
import pandas as pd
from map_labeler import MapLabeler
from score_tracker import ScoreTracker

# # function to get turtle coordinate on mouse click
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()

# def get_coordinate(df, state):
#     guess_df = df[df['state'] == state]
#     if len(guess_df) > 0:
#         x = guess_df.iloc[0]['x']
#         y = guess_df.iloc[0]['y']
#         coordinate = (x, y)
#         return coordinate
#     else:
#         return None


screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)      # Add turtle shape from image
turtle.shape(image)         # Create new turtle object with image as shape
states_df = pd.read_csv('50_states.csv') # dataframe with a list of states and turtle coordinates
tracker = ScoreTracker()

game_is_on = True
while game_is_on:
    state_guess = screen.textinput(title=f"{tracker.state_count}/{tracker.total_states} Correct States",
                                   prompt="Do you know another state?").title()

    coordinate = tracker.get_coordinate(state_guess)  # check if state guess returns a coordinate
    if coordinate is not None:
        labeler = MapLabeler()
        labeler.add_state(state_guess, coordinate)
        tracker.update_score(state_guess)

    # check if all 50 states have been guessed
    if tracker.state_count == tracker.total_states:
        labeler = MapLabeler()
        labeler.game_over()
        game_is_on = False


# print(states_df.head())

# screen.exitonclick()
