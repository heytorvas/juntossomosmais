import shapely.geometry, json, requests
from api.const import NORMAL, SPECIAL1, SPECIAL2

def get_users_json():
    r = requests.get("https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json").json()
    return r

def phone_formatter(phone):
    return "+55" + phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()

def set_user_category(user):
    latitude = user["location"]["coordinates"]["latitude"]
    longitude = user["location"]["coordinates"]["longitude"]
    point = shapely.geometry.Point(float(longitude), float(latitude))

    bounding_box_normal = shapely.geometry.box(NORMAL["minlon"], NORMAL["minlat"], NORMAL["maxlon"], NORMAL["maxlat"])
    bounding_box_special1 = shapely.geometry.box(SPECIAL1["minlon"], SPECIAL1["minlat"], SPECIAL1["maxlon"], SPECIAL1["maxlat"])
    bounding_box_special2 = shapely.geometry.box(SPECIAL2["minlon"], SPECIAL2["minlat"], SPECIAL2["maxlon"], SPECIAL2["maxlat"])

    if bounding_box_normal.contains(point):
        return "normal"
    elif bounding_box_special1.contains(point):
        return "special"
    elif bounding_box_special2.contains(point):
        return "special"
    else:
        return "laborious"

def set_user_gender(user):
    return "F" if user['gender'] == 'female' else "M"

def get_updated_users():
    users_updated = []
    users = get_users_json()['results']
    for user in range(len(users)):
        updated = {
            "type": set_user_category(users[user]),
            "gender": set_user_gender(users[user]),
            "name": users[user]['name'],
            "location": users[user]['location'],
            "email": users[user]['email'],
            "birthday": users[user]["dob"]["date"],
            "registered": users[user]["registered"]["date"],
            "telephoneNumbers": [
                phone_formatter(users[user]['phone'])
            ],
            "mobileNumbers": [
                phone_formatter(users[user]['cell'])
            ],
            "picture": users[user]['picture'],
            "nationality": "BR"
        }
        users_updated.append(updated)
    
    # return json.dumps(users_updated,  ensure_ascii=False)
    return users_updated