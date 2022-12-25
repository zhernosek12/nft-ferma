#pip3 install anticaptchaofficial
from anticaptchaofficial.hcaptchaproxyon import *

# https://metamint.gitbook.io/metaraffles/discord-1/setup
# captcha api id --> 998703a8e281071c0a78c0198e3ab641

#token = "MTAzMzcyOTMxMzMyMjgyNzkxNg.GRKf85.G_oHRHz-7zlpU4-nhNXEHJw-sCxrNipzUT3GGM"
#token = "MTA0MTI4OTQ1MTg5MDAyMDQwMw.GBgBbl.mBnjahdJ_z6_w4o3fKvMlNysE-nPPk5cVu5b0Q"
#token = "MTA0MDc1MDgzNzY2NTg5ODQ5Ng.GiNuwQ.fKTl_AXdWCROL8j4fnU0gOSpApIsdjbW7zyvAE"
token = "MTA0MjgwNjI3MTkxMDM2NzI4Mg.GjZ3I9.3SQuXbgWai_-8TYtMxkgQlLcwp9whQMplFdaOY"

proxy = {
    "type": "socks5",
    "login": "8ByYP4Hx",
    "password": "qKxvHiMf",
    "address": "185.77.137.137",
    "port": 56148,
}


import requests
import time
import json

def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    print(r.status_code)


#sendMessage(token, "999333356393222274", "How are you?")

def join(token, proxy, server_invite):

    header = {
        "Authorization": token
    }
    proxies = {
        "http":'{}://{}:{}@{}:{}'.format(proxy["type"], proxy["login"], proxy["password"], proxy["address"], proxy["port"]),
        "https":'{}://{}:{}@{}:{}'.format(proxy["type"], proxy["login"], proxy["password"], proxy["address"], proxy["port"])
    }

    print("Join discord server...")
    request = requests.request("POST", "https://discord.com/api/v8/invites/{}".format(server_invite), headers=header, proxies=proxies)

    # capcha
    if request.status_code == 400:
        print("Captcha parsing...")

        captcha_key = request.json()["captcha_key"]
        captcha_sitekey = request.json()["captcha_sitekey"]
        captcha_service = request.json()["captcha_service"]
        captcha_rqdata = request.json()["captcha_rqdata"]
        captcha_rqtoken = request.json()["captcha_rqtoken"]

        if captcha_service == "hcaptcha":

            print("Send captcha server...")

            solver = hCaptchaProxyon()
            solver.set_verbose(0)
            solver.set_key("998703a8e281071c0a78c0198e3ab641")
            solver.set_website_url("https://discord.com/invite/{}".format(server_invite))
            solver.set_website_key(captcha_sitekey)

            solver.set_proxy_type(proxy["type"])
            solver.set_proxy_address(proxy["address"])
            solver.set_proxy_port(proxy["port"])
            solver.set_proxy_login(proxy["login"])
            solver.set_proxy_password(proxy["password"])

            solver.set_enterprise_payload({
                "rqdata": captcha_rqdata,
                "sentry": True
            })

            captcha_key = solver.solve_and_return_solution()
            if captcha_key != 0:
                payload = {
                    'captcha_key': captcha_key,
                    'captcha_rqtoken': captcha_rqtoken,
                }
                response = requests.request("POST", 'https://discord.com/api/v8/invites/{}'.format(server_invite), headers=header, json=payload, proxies=proxies)

                if response.status_code == 200:
                    return response.json()
                else:
                    print("error capcha")
                    return {}
            else:
                print("task finished with error", solver.error_code)
                return {}
        else:
            return request.json()
    else:
        return request.json()


print(join(token, proxy, "GEEqWrVBsr"))