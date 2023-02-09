import requests
import sys
from io import BytesIO
from PIL import Image
from yx import get_scale


search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = "37.588392,55.734036"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    pass
else:
    json_response = response.json()
    organizations = json_response["features"][:10]
    point_list = []
    for i in range(10):
        org_name = organizations[i]["properties"]["CompanyMetaData"]["name"]
        org_address = organizations[i]["properties"]["CompanyMetaData"]["address"]
        point = organizations[i]["geometry"]["coordinates"]
        org_point = "{0},{1}".format(point[0], point[1])
        try:
            if 'Everyday' in organizations[i]["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0].keys():
                mark = ',pm2gnm'
            elif "TwentyFourHours" not in organizations[i]["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0].keys():
                mark = ',pm2blm'
            else:
                mark = ',pm2grm'
        except Exception as ex:
            print(ex)
            mark = ',pm2grm'
        point_list.append(org_point + mark)
    deltax, deltay = get_scale(json_response)
    map_params = {
        "ll": address_ll,
        "spn": ",".join([str(deltax), str(deltay)]),
        "l": "map",
        "pt": "~".join(point_list)
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(
        response.content)).show()