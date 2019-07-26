# Football Scraping and Calculation tool

scraping_tool.py has been created to capture website data (fbref.com), that can be then fed into the season_calcs.py engine. This will run some simple metrics to track team performance.

Legend used for the calculations and notation: Goals (G), Assists (A), Penalties (PK), Shots on Target (SOT), Fouls (F), Cards (C), Per 90 Minutes (/90).

# In the works currently for the parser:

- Use Data URLs.xlsx to feed the parser instead of single, manual URLs, for easy team one-off parsing. Current scope simply 2002 onward.
- Use League Two/League One Teams per Season files to feed team listings for parser, to get all teams at once. All needed is the URL team codes, and the rest can be automated.

- Run simply calculations for team performative stats (G/90, A/90, G-PK/90, G+A-PK/90, SOT/90, F/90, C/90) off of parser. Should just be captured rather easily off of the acquired data.

# Currently being built for the calculation engine:

- Calculate player performance throughout seasons
- Replicate FiveThirtyEight model for team success predictions
- Apply some basic models (TBD) for team level analytics
