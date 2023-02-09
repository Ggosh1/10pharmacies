def get_scale(json_response):
    corners = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]
    upper_corner = corners['upperCorner'].split()
    lower_corner = corners['lowerCorner'].split()
    deltax = abs(float(upper_corner[0]) - float(lower_corner[0]))
    deltay = abs(float(upper_corner[1]) - float(lower_corner[1]))
    return deltax, deltay