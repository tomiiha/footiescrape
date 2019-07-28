# Football Scraping and Calculation tool

Personal project to get a deeper understanding of sports analytics, to leverage for story telling later on for lower-tier leagues. Consists currently of the following programs: scraping_tool.py, league_scraper.py and season_calcs.py.

scraping_tool.py has been created to capture website data (fbref.com), that can be then fed into the season_calcs.py engine. This will run some simple metrics to track team performance. Currently in a very simplistic form, however expanding slowly to make scraping a bit easier, and then build the calculations engine to capture some narrative based off of these data.

league_scraper.py is a tool to capture league -level detail, to get a better sense of the overall season results.

# Currently building for the data parser:

- Use Data URLs.xlsx to feed the parser instead of single, manual URLs, for easy team one-off parsing. Current scope simply 2002 onward.
- Use League Two/League One Teams per Season files to feed team listings for parser, to get all teams at once. All needed is the URL team codes, and the rest can be automated.

- Run simply calculations for team performative stats (G/90, A/90, G+A/90, G-PK/90, G+A-PK/90, SOT/90, F/90, C/90) off of parser. Should just be captured rather easily off of the acquired data.

# Currently building for the calculation engine:

- Calculate player performance throughout seasons.
- Replicate FiveThirtyEight model for team success predictions.
- Apply some basic models (TBD) for team level analytics.

# Legend and Notes:

- Calculation notation: Goals (G), Assists (A), Penalties (PK), Shots on Target (SOT), Fouls (F), Cards (C), Per 90 Minutes (/90), Total Minutes Played (TM).
- Math for over 90s is simple, for example G+A-PK/90: (G+A)/(TM/90). The float result effectively will define a simple performance metric to start with. Attached is also a manual prove-out of some of the metrics, as fref has them (Per90 Manual Prove Out.xlsx).
