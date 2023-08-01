from datetime import date

from util import JsonDeserializer, JsonSerializer, Webscraper
from util.Visualizer import visualize_dict

#Before running, download selenium chrome webdriver and place in project directory


working_directory = "C:\\Users\\19044\\PycharmProjects\\webscraper\\"
interested_floorplans = ["beech", "birch"]
today = date.today().strftime("%d/%m/%Y")

for floorplan in interested_floorplans:
    dict = JsonDeserializer.read_dict_from_json(floorplan, file_path=working_directory)

    dict[today] = Webscraper.get_data_from_url(f"https://www.theloreeapartments.com/floorplans/{floorplan}?Beds=2")

    visualize_dict(dict)

    JsonSerializer.write_dict_to_json(floorplan, dict, file_path=working_directory)
