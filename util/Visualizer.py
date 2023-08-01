import datetime as dt
from datetime import datetime

import pandas as pd
import plotly.express as px

format_string = "%d/%m/%Y"

def visualize_dict(dict):
    room_histories = {}

    for date in dict.keys():
        for room in dict[date]:
            room_number = room["room number"]
            if room_number not in room_histories:
                previous_day = datetime.strptime(date, format_string) - dt.timedelta(days=1)
                room_histories[room_number] = {"start": previous_day.strftime(format_string), "end": date}
            else:
                room_histories[room_number]["end"] = date

    room_list = []

    for room_number in room_histories.keys():
        room_list.insert(0, {"room number": room_number, "start": room_histories[room_number]["start"], "end": room_histories[room_number]["end"]})

    source = pd.DataFrame(room_list)

    source['start'] = pd.to_datetime(source['start'], format="%d/%m/%Y")
    source['end'] = pd.to_datetime(source['end'], format="%d/%m/%Y")

    fig = px.timeline(source.sort_values('start'),
                      x_start="start",
                      x_end="end",
                      y="room number",
                      text="room number",
                      color_discrete_sequence=["tan"])
    fig.show()