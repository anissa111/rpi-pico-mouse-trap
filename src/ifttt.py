"""
Module for handling IFTTT requests.
"""
import urequests

def trigger_iffft(app, api_key, values=[]):
    print("posing message")
    urequests.post(make_message(app, api_key, values))

def make_message(app, api_key, values=[]):
    url = "https://maker.ifttt.com/trigger/"
    with_api_key = "/with/key/" + api_key

    message = url + app + with_api_key

    # append values to message if any
    if len(values) > 0:
        message = message + "?"

        for i in range(len(values)):
            message = message + "value" + str(i) + "=" + values[i]

            if i < len(values) - 1:
                message = message + "&"

    print(message)
    return message

