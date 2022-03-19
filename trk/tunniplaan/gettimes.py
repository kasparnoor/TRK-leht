import requests
from bs4 import BeautifulSoup

URL = "https://real.edu.ee/oppimine/tunniplaan/tundide-algus/"
page = requests.get(URL)

data = []
soup = BeautifulSoup(page.content, "html.parser")
kaheksasklass_table = soup.find(id="cut-1-6")
kaheksasklass_table_body = kaheksasklass_table.find('tbody')

rows = kaheksasklass_table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

times = []
for row in data:
    if "söö" in row[0]:
        data.remove(row)
        continue;
    index = row[0][0]
    time = row[1].split('–')[0]
    lesson = [index, time]
    times.append(lesson)
print(times)