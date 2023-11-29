import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate random dates between a given range
def random_dates(start_date, end_date, n=10):
    date_range = end_date - start_date
    random_dates = start_date + np.random.rand(n) * date_range
    return [start_date + timedelta(days=int(date)) for date in random_dates]

# Define the ranges and lists
emp_no = list(range(1, 101))
emp_iid = list(range(1, 200, 2))
project_id = list(range(1, 101))
start_date = datetime(2023, 1, 1)
end_date = datetime(2035, 12, 31)
team_size = list(range(1, 11))
status = ['Not Started', 'Partially Done', 'Completed']
data = {
    'EMPNo': np.random.choice(emp_no, 100),
    'EMPIID': np.random.choice(emp_iid, 100),
    'ProjectID': np.random.choice(project_id, 100),
    'Start Date': [str(date) for date in random_dates(start_date, end_date, 100)],
    'End Date': [str(date) for date in random_dates(start_date, end_date, 100)],
    'Team Size': np.random.choice(team_size, 100),
    'Team Lead': np.random.choice(emp_no, 100),
    'Project Manager': np.random.choice(emp_no, 100),
    'Status': np.random.choice(status, 100)
}
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('project_data.csv', index=False)
