import pandas as pd


class ScoreTracker:
    def __init__(self):
        self.correct_states = []
        self.state_count = 0
        self.states_df = pd.read_csv('50_states.csv')  # dataframe with a list of states and turtle coordinates
        self.all_states = self.states_df.state.to_list()
        self.total_states = len(self.states_df)

    def update_score(self, state):
        self.correct_states.append(state)
        self.state_count += 1

    def get_coordinate(self, state):
        guess_df = self.states_df[self.states_df['state'] == state]
        if state in self.all_states:
            x = guess_df.iloc[0]['x']
            y = guess_df.iloc[0]['y']
            coordinate = (x, y)
            return coordinate
        else:
            return None

    def unnamed_states(self):
        unnamed_list = list(set(self.all_states) - set(self.correct_states))
        unnamed_df = pd.DataFrame(unnamed_list, columns=["state"])
        unnamed_df.to_csv("unnamed_states.csv", header=True, index=False)

# # function to get turtle coordinate on mouse click
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()