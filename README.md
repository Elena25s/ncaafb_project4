# NCAA Football Data Project

This project uses the Sportradar API to collect, analyze, and visualize NCAA Football data. It supports fetching game statistics, 
player profiles, team rosters, and converting the data into CSV format for further analysis and visualization.

##  Project Structure
ncaafb_project4/
 assets/ # Contains CSV files like game_ids.csv
 data/ # Processed CSV files (stats, rosters, etc.)
 notebooks/ # Jupyter notebooks for exploration and visualization
 scripts/ # Python scripts for data ingestion and API requests
 visualizations/ # Graphs and plots using Plotly/Tableau
 README.md # Project documentation
 requirements.txt # Required Python packages


## Features

-  Pull NCAA football data from the Sportradar API  
-  Game statistics, player profiles, and team rosters  
-  Convert nested JSON to clean CSVs using Pandas  
-  Plot statistics using Plotly  
-  Export data for Tableau dashboards  

## Sample Visuals

- Team performance over multiple games  
- Player season summaries  
- Game score breakdowns  

## Tech Stack

- Python 3.x  
- Pandas  
- Plotly  
- Requests  
- Jupyter Notebooks  
- Tableau (for dashboarding)

##  Installation

   Clone the repository:
 ```bash
 git clone https://github.com/Elena25s/ncaafb_project4.git
 cd ncaafb_project4
   
   
   Install dependencies:
pip install -r requirements.txt


 API Key Setup:
Register at Sportradar Developer Portal.
Then insert your API key into your script:
API_KEY = "your_api_key_here"

Usage:
Run data extraction:
python scripts/get_game_stats.py


View visualizations:
Open any notebook in notebooks/
Or import CSV files into Tableau
