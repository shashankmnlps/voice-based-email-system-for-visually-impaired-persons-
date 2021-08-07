import requests
def send_sms(number, messages):

    url = "https://www.fast2sms.com/dev/bulkV2"

    api = "RTmGfN1Sg7psozQEvMtnICK8PlqwYbDk4ULc6OeJWyZxAjF3udDMZG43siUkCKazELmNfnwgI6AjbB5c"
    querystring = {
        "authorization":api,
        "sender_id": " TXTIND",
        "message": messages,
        "language": "english",
        "route": "v3",
        "numbers": number
    }

    headers = {
        'cache-control': "no-cache"
    }

    requests.request("GET", url, headers=headers, params=querystring)