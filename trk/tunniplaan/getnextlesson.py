from tunniplaan import gettimes
from tunniplaan import getlessons

import datetime
from datetime import timedelta
def getnextlesson():
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

    currenttime = datetime.datetime.now()
    currenttime = datetime.datetime(2022, 3, 22, 10, 37)
    today = str(currenttime.weekday() + 1)
    lessons_ = "lessons_"
    today_lessons = lessons_ + today
    if today_lessons in "lessons_6" or today_lessons in "lessons_7":
        return "weekends"
    today_lessons = locals()[today_lessons]
    for time in times:
        lesson_end = time + timedelta(minutes=45)
        # Lesson is ongoing
        if currenttime.time() > time.time() and currenttime.time() < lesson_end.time():
            time_until_lesson_end = lesson_end - currenttime
            info = ["Tund lõpeb:", today_lessons[times.index(time)], time_until_lesson_end.total_seconds()]
            return(info)
            break
        # Time until next lesson
        if currenttime.time() < time.time() and currenttime.time() < lesson_end.time():
            next_lesson = times[times.index(time)]
            time_until_next_lesson = next_lesson - currenttime
            info = ["Tund algab:", today_lessons[times.index(time)], time_until_next_lesson.total_seconds()]
            return(info)
            break

getnextlesson()
