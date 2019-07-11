# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# Note: https://fbref.com/robots.txt
# Start with https://fbref.com/en/squads/986a26c1/Northampton-Town

from bs4 import BeautifulSoup as bsoup
import requests as reqs
import xlsxwriter as xsl

# Load data file to use
workbook = xsl.workbook('Ndata1819.xlsx')
worksheet = workbook.add_worksheet()

# Capture website
page = reqs.get("https://fbref.com/en/squads/986a26c1/Northampton-Town")
status = page.status_code
parsepage = bsoup(page.content, 'html.parser')

# Lists
playerlist = []
positionlist = []
agelist = []
gamesplayedlist = []
gamestartslist = []
gamesubslist = []
minuteslist = []
minutespgamelist = []

# Elements to ultimately find in toparse - gen player list off of findplayers
toparse = ["player","position","age","games","game_starts","game_subs","minutes","minutes_per_game"]
findplayers = parsepage.find_all('th',attrs={"data-stat":"player"})
for player in findplayers:
    addplayer = player.find_next('a').get_text()
    if addplayer not in playerlist and addplayer != 'coverage note':
        playerlist.append(addplayer)
print(playerlist)

# Data writing into excel file - insert lists to designated columns A1 onward
startrow = 0
startcol = 0
for header in toparse:
    worksheet.write(startrow, startcol, header)
startrow = 1
for player in addplayer:
    worksheet.write(startrow, startcol, one)
    row += 1
workbook.close()
