import requests

def link_checker(link):
    try:
        # GET request
        req = requests.get(link)

        # Print the status code
        print(f"{link} => Status code: {req.status_code}")

        if 200 <= req.status_code < 300:
            print ("Good Link")

        if 400 <= req.status_code < 600:
            print ("Bad Link")

    # Exception
    except requests.exceptions.RequestException as e:
        # Print an error message
        print(f"{link}: Something wrong\nErr: {e}")

link_checker("https://www.google.com/")