def get_scale(json_response):
    corners = json_response["properties"]["ResponseMetaData"]["SearchResponse"]["boundedBy"]
    upper_corner = corners[0]
    lower_corner = corners[1]
    deltax = abs(float(upper_corner[0]) - float(lower_corner[0]))
    deltay = abs(float(upper_corner[1]) - float(lower_corner[1]))
    return deltax, deltay