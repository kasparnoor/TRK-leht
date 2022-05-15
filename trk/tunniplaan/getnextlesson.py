from tunniplaan import gettimes
from tunniplaan import getlessons
import configparser
import os 

import datetime
from datetime import timedelta
import requests_cache

requests_cache.install_cache(cache_name='getnextlesson_cache', backend='sqlite', expire_after=180)
def getnextlesson():
    
    config_obj = configparser.ConfigParser()
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    config_obj.read(os.path.join(__location__, 'appconfig.ini'))

    conf_app = config_obj["app"]
    conf_app_debug = conf_app["debug"]
    conf_app_date_simulation = conf_app["date_simulation"]
    conf_app_simulation_date = conf_app["simulation_date"]
    
    now = datetime.datetime.now()
    day = now.strftime("%A")
    time = now.time()

    times = gettimes.gettimes()
    lessons = getlessons.getlessons()

    lessons_1 = lessons[::5]
    lessons_2 = lessons[1::5]
    lessons_3 = lessons[2::5]
    lessons_4 = lessons[3::5]
    lessons_5 = lessons[4::5]

    if conf_app_date_simulation == "true":
        currenttime = datetime.datetime(int(conf_app_simulation_date.split(", ")[0]), int(conf_app_simulation_date.split(", ")[1]), int(conf_app_simulation_date.split(", ")[2]), int(conf_app_simulation_date.split(", ")[3]), int(conf_app_simulation_date.split(", ")[4]))
    else:
        currenttime = datetime.datetime.now()
        

    today = str(currenttime.weekday() + 1)
    lessons_ = "lessons_"
    today_lessons = lessons_ + today
    if today_lessons in "lessons_6" or today_lessons in "lessons_7":
        return
    today_lessons = locals()[today_lessons]
    for time in times:
        lesson_end = time + timedelta(minutes=45)
        # Lesson is ongoing
        if currenttime.time() > time.time() and currenttime.time() < lesson_end.time():
            time_until_lesson_end = lesson_end - currenttime
            info = ["Praeguse tunni lõpuni:", today_lessons[times.index(time)], time_until_lesson_end.total_seconds()]
            return(info)
            break
        # Time until next lesson
        if currenttime.time() < time.time() and currenttime.time() < lesson_end.time():
            next_lesson = times[times.index(time)]
            time_until_next_lesson = next_lesson - currenttime
            info = ["Järgmise tunni alguseni:", today_lessons[times.index(time)], time_until_next_lesson.total_seconds()]
            return(info)
            break

getnextlesson()
