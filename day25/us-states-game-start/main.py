import turtle
from map_labeler import MapLabeler
from score_tracker import ScoreTracker

screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)      # Add turtle shape from image
turtle.shape(image)         # Create new turtle object with image as shape
tracker = ScoreTracker()

game_is_on = True
while game_is_on:
    state_guess = screen.textinput(title=f"{tracker.state_count}/{tracker.total_states} Correct States",
                                   prompt="Do you know another state?")

    if state_guess == "Exit" or state_guess == "exit" or state_guess is None:
        game_is_on = False
        tracker.unnamed_states()
    else:
        state_guess = state_guess.title()
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
