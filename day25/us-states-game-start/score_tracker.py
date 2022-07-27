import pandas as pd



class ScoreTracker:
    def __init__(self):
        self.correct_states = []
        self.state_count = 0
        self.states_df = pd.read_csv('50_states.csv')  # dataframe with a list of states and turtle coordinates
        self.total_states = len(self.states_df)

    def update_score(self, state):
        self.correct_states.append(state)
        self.state_count += 1

    def get_coordinate(self, state):
        guess_df = self.states_df[self.states_df['state'] == state]
        if len(guess_df) > 0:
            x = guess_df.iloc[0]['x']
            y = guess_df.iloc[0]['y']
            coordinate = (x, y)
            return coordinate
        else:
            return None
