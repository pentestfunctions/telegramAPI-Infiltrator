import requests
import json

api_token = "123:123123"
chat_id = "-123123"

def get_bot_info(api_token):
    url = f"https://api.telegram.org/bot{api_token}/getMe"
    response = requests.get(url)
    return json.loads(response.content)

def get_chat_info(api_token, chat_id):
    url = f"https://api.telegram.org/bot{api_token}/getChat"
    params = {'chat_id': chat_id}
    response = requests.get(url, params=params)
    return json.loads(response.content)

def get_chat_admins(api_token, chat_id):
    url = f"https://api.telegram.org/bot{api_token}/getChatAdministrators"
    params = {'chat_id': chat_id}
    response = requests.get(url, params=params)
    return json.loads(response.content)

# Get Bot Information
bot_info = get_bot_info(api_token)
print("Bot Information:", json.dumps(bot_info, indent=4))

# Get Chat Information
chat_info = get_chat_info(api_token, chat_id)
print("Chat Information:", json.dumps(chat_info, indent=4))

# Get Chat Administrators
chat_admins = get_chat_admins(api_token, chat_id)
print("Chat Administrators:", json.dumps(chat_admins, indent=4))
