import requests

#
def get_project():

    url = "http://checks.wordok.by/premint/api.php?method=tasks"

    payload = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def set_status_project(profile_id, project_id, status):

    url = "http://checks.wordok.by/premint/api.php?method=setStatus&profile_id=" + profile_id + "&project_id=" + project_id + "&status=" + status

    payload = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'}
    response = requests.request("GET", url, headers=headers, data=payload)

    print(status, " --> success!")

    return response.json()