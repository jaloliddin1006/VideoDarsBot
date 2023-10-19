import requests
import json

BASE_URL = "http://127.0.0.1:8000"

######## createuser ############
def create_user(telegram_id, username, first_name, last_name, is_active):
    context =  {
                "user_id": telegram_id,
                "username":username,
                "first_name":first_name,
                "last_name":last_name,
                "is_active":is_active
                }
    response = requests.post(f"{BASE_URL}/api/botuser/", data = context)
    return response.status_code

def get_all_users():
    response = requests.get(f"{BASE_URL}/api/botuser/")
    data = json.loads(response.text)
    return data
######### feedback ###########
def feedback(user_id, feedback):
    response = requests.post(f"{BASE_URL}/api/feedback/", data = {"user__user_id":user_id, "feedback": feedback})
    return response.status_code

######### getcategorylist ##########
def category_info(category=None, page=None):
    try:
        if category:
            response = requests.get(f"{BASE_URL}/api/category/{category}/?{page}")
        else:
            response = requests.get(f"{BASE_URL}/api/category/?{page}")
        data = json.loads(response.text)
        return data
    except:
        return []

def get_source_list(category=None):
    if category:
        response = requests.get(f"{BASE_URL}/api/source/{category}/")
    else:
        response = requests.get(f"{BASE_URL}/api/source/")
    data = json.loads(response.text)
    return data

# user = create_user(1, "test", "test", "test")
# print(user)
# feed = feedback(1, "test feedback")
# print(feed)

# categorys = category_info()
# print(categorys)

# subcategorys = category_info("Salom O'rtacha Category")
# print(subcategorys)

# source = get_source_list("G'ani category") # source ni slug qo'shish kerak, sub categoryni slug bilan yuboraman, categoryni ham slug bilan yuboraman
# print(source)
