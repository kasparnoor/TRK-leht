import requests
from bs4 import BeautifulSoup
import datetime
import configparser
import os 
import requests_cache

requests_cache.install_cache(cache_name='gettimes_cache', backend='sqlite', expire_after=180)
def gettimes():
    
    config_obj = configparser.ConfigParser()
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    config_obj.read(os.path.join(__location__, 'appconfig.ini'))

    conf_app = config_obj["app"]
    conf_app_debug = conf_app["debug"]
    conf_app_date_simulation = conf_app["date_simulation"]
    conf_app_simulation_date = conf_app["simulation_date"]
    
    # URL For starting times of lessons
    URL = "https://real.edu.ee/oppimine/tunniplaan/tundide-algus/"
    # Making the request to the URL of starting times
    page = requests.get(URL)

    data = []
    # Parsing the HTML with beautifulsoup
    soup = BeautifulSoup(page.content, "html.parser")
    # Finding the table "cut-1-6" from the entire page which is the table for class 8
    kaheksasklass_table = soup.find(id="cut-1-6")
    # Getting the body of that table
    kaheksasklass_table_body = kaheksasklass_table.find('tbody')
    # Getting the rows in the table of 8kl body
    rows = kaheksasklass_table_body.find_all('tr')
    # Getting the columns, part of parsing the table, somehow made it work
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
    # Creating the table for times
    times = []
    # Checking every row in previously parsed columns
    for row in data:
        # Removing eating breakes from the list
        if "söö" in row[0]:
            data.remove(row)
            continue;
        # Formatting the time a bit
        index = row[0][0]
        time = row[1].split('–')[0]
        times.append(time)
    
    # Parsing the time "strings" as actual datetimes
    for time in times:
        newtime = time.replace(".", ":")
        newtime2 = datetime.datetime.strptime(newtime, "%H:%M")
        now = datetime.datetime.now()
        newtime3 = newtime2.replace(now.year, now.month, now.day)
        if conf_app_date_simulation == "true":
            newtime3 = newtime2.replace(int(conf_app_simulation_date.split(", ")[0]), int(conf_app_simulation_date.split(", ")[1]), int(conf_app_simulation_date.split(", ")[2]))
        times[times.index(time)] = newtime3

    return(times)