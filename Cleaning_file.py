import nfl_data_py as nfl
import pandas as pd

def import_nfl_data(start_year, end_year):
    # Initialize empty DataFrames to store data
    all_seasonal_data = pd.DataFrame()
    all_player_data = pd.DataFrame()
    all_team_data = pd.DataFrame()
    all_schedule_data = pd.DataFrame()

    # Loop through each year and import data
    for year in range(start_year, end_year + 1):
        # Import seasonal data
        seasonal_data = nfl.import_seasonal_data(years=[year])
        all_seasonal_data = pd.concat([all_seasonal_data, seasonal_data], ignore_index=True)

        # Import player data
        player_data = nfl.import_players()
        all_player_data = pd.concat([all_player_data, player_data], ignore_index=True)

        # Import team description data
        team_data = nfl.import_team_desc()
        all_team_data = pd.concat([all_team_data, team_data], ignore_index=True)

        # Import game schedule data
        schedule_data = nfl.import_schedules(years=[year])
        all_schedule_data = pd.concat([all_schedule_data, schedule_data], ignore_index=True)

    return all_seasonal_data, all_player_data, all_team_data, all_schedule_data

# Define the range of years
start_year = 2018
end_year = 2024

# Import data
seasonal_data, player_data, team_data, schedule_data = import_nfl_data(start_year, end_year)

# Optionally, save the data to CSV files
seasonal_data.to_csv("seasonal_data_2018_2024.csv", index=False)
player_data.to_csv("player_data_2018_2024.csv", index=False)
team_data.to_csv("team_data_2018_2024.csv", index=False)
schedule_data.to_csv("schedule_data_2018_2024.csv", index=False)
