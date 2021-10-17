import shapely.geometry, requests
from api.const import NORMAL, SPECIAL1, SPECIAL2

def get_users_json():
    """
    Get a users list from HTTP request.

    Parameters
    ----------
    None

    Returns
    ----------
    response : list
        users list from request.
    """

    response = requests.get("https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json").json()
    return response["results"]

def get_regions_json():
    """
    Get a regions and states list from HTTP request.

    Parameters
    ----------
    None

    Returns
    ----------
    response : list
        regions list from request.
    """

    response = requests.get("https://raw.githubusercontent.com/Tubaleviao/estados-regioes-json/master/estado-regiao.json").json()
    
    # fix bug from gist
    response[6]["Região"] = "Centro-Oeste"

    return response

def phone_formatter(phone):
    """
    Format a phone number on E164 format.

    Parameters
    ----------
    phone : str
        phone number of the user

    Returns
    ----------
    phone : str
        phone number formatted.
    """

    return "+55" + phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()

def set_user_category(coordinates):
    """
    Set a user's category by location.

    Parameters
    ----------
    coordinates : dict
        latitude and longitude of the user

    Returns
    ----------
    category : str
        category of the user
    """

    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]
    point = shapely.geometry.Point(float(longitude), float(latitude))

    bounding_box_normal = shapely.geometry.box(NORMAL["minlon"], NORMAL["minlat"], NORMAL["maxlon"], NORMAL["maxlat"])
    bounding_box_special1 = shapely.geometry.box(SPECIAL1["minlon"], SPECIAL1["minlat"], SPECIAL1["maxlon"], SPECIAL1["maxlat"])
    bounding_box_special2 = shapely.geometry.box(SPECIAL2["minlon"], SPECIAL2["minlat"], SPECIAL2["maxlon"], SPECIAL2["maxlat"])

    if bounding_box_normal.contains(point):
        return "normal"
    elif bounding_box_special1.contains(point) or bounding_box_special2.contains(point):
        return "special"
    else:
        return "laborious"

def set_user_gender(gender):
    """
    Update user's gender to a character

    Parameters
    ----------
    gender : str
        gender of the user

    Returns
    ----------
    gender : str
        gender of the user
    """

    return "F" if str(gender).lower() == "female" else "M"

def set_user_region(state, regions):
    """
    Set user's region by state's user.

    Parameters
    ----------
    state : str
        state of the user
    regions : list
        list of brazil's regions

    Returns
    ----------
    region : str
        region of the user
    """

    for region in regions:
        if str(state).lower().strip() == str(region["Nome"]).lower().strip():
            return str(region["Região"]).lower()

def get_updated_users():
    """
    Create a users list after update on this values.

    Parameters
    ----------
    None

    Returns
    ----------
    users_updated : list
        list of the users
    """
    
    users_updated = []
    users = get_users_json()
    regions = get_regions_json()
    for user in range(len(users)):
        updated = {
            "type": set_user_category(users[user]["location"]["coordinates"]),
            "gender": set_user_gender(users[user]["gender"]),
            "name": users[user]["name"],
            "location": users[user]["location"],
            "email": users[user]["email"],
            "birthday": users[user]["dob"]["date"],
            "registered": users[user]["registered"]["date"],
            "telephoneNumbers": [
                phone_formatter(users[user]["phone"])
            ],
            "mobileNumbers": [
                phone_formatter(users[user]["cell"])
            ],
            "picture": users[user]["picture"],
            "nationality": "BR"
        }
        updated["location"]["region"] = set_user_region(users[user]["location"]["state"], regions)
        users_updated.append(updated)
    
    return users_updated