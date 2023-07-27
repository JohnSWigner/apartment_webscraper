import JsonSerializer
import JsonDeserializer
import Webscraper
from datetime import date

#Before running, download selenium chrome webdriver and place in project directory

interested_floorplans = ["beech", "birch"]
today = date.today().strftime("%d/%m/%Y")

for floorplan in interested_floorplans:
    dict = JsonDeserializer.read_dict_from_json(floorplan)

    dict[today] = Webscraper.get_data_from_url(f"https://www.theloreeapartments.com/floorplans/{floorplan}?Beds=2")

    JsonSerializer.write_dict_to_json(floorplan, dict)
