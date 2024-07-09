import pandas as pd
import numpy as np

num_rows = 3*(10**7)  


data = {
    'match_id': np.arange(1, num_rows + 1),
    'team_home': np.random.choice(['TeamA', 'TeamB', 'TeamC', 'TeamD', 'TeamE'], num_rows),
    'team_away': np.random.choice(['TeamA', 'TeamB', 'TeamC', 'TeamD', 'TeamE'], num_rows),
    'score_home': np.random.randint(0, 10, num_rows),
    'score_away': np.random.randint(0, 10, num_rows),
    'date': pd.date_range(start='2020-01-01', periods=num_rows, freq='T').strftime('%Y-%m-%d %H:%M:%S')
}


df = pd.DataFrame(data)


df.to_csv('large_football_data.csv', index=False)

print("Successfully")
