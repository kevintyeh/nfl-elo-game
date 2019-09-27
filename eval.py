from util import *
from forecast import *

# Read historical games from CSV
games = Util.read_games("data/nfl_games.csv")

# Forecast every game
Forecast.forecast(games)

# Evaluate our forecasts against Elo
Util.evaluate_forecasts(games)

# TODO:
"""
Create code to compare logic with ELO points and Yahoo spread

General Algorithm:

Does ELO Favorite == Yahoo Favorite:
    If True:
        Is ELO > Yahoo:
            True: ELO more bullish on favorite
                Then: Choose underdog
            False: ELO less bullish/confident then Yahoo
                Then: Choose favorite
    Else:
        Choose Favorite (ELO thinks underdog is going to win)
"""
