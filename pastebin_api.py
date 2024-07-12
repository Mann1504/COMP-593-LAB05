import requests

def create_paste(title, body_text, expiration, listed):
    """
    Creates a new PasteBin paste.

    Args:
        title (str): The title of the paste.
        body_text (str): The body text of the paste.
        expiration (str): The expiration period of the paste.
        listed (bool): Whether the paste is publicly listed.

    Returns:
        str: The URL of the newly created paste if successful, None otherwise.
    """
    PASTEBIN_API_KEY = 'i1JTgeLlPQLqpMamsCo-SCLUM9Z8oajj
'
    url = 'https://pastebin.com/doc_api'

    data = {
        'api_dev_key': PASTEBIN_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': '1' if listed else '0',
    }

    print("Creating paste on PasteBin...")
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Paste created successfully!")
        return response.text
    else:
        print("Failed to create paste.")
        return None
