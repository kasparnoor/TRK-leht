import requests
from bs4 import BeautifulSoup
import datetime

def gettimes():
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
        times.append(time)
    
    for time in times:
        newtime = time.replace(".", ":")
        newtime2 = datetime.datetime.strptime(newtime, "%H:%M")
        now = datetime.datetime.now()
        newtime3 = newtime2.replace(now.year, now.month, now.day)
        newtime3 = newtime2.replace(2022, 3, 22)
        times[times.index(time)] = newtime3
        
    return(times)