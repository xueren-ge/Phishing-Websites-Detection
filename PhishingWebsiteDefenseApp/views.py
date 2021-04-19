from django.shortcuts import render, redirect
from django.contrib import messages
from PhishingWebsiteDefenseApp.useModel import MachineLearningModel
from PhishingWebsiteDefenseApp.phnishTankApiRequest import PhishTank

# Create your views here.
def index(request):
    return render(request, 'index.html')

# helper Function
def check(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        try:
            url = url.lower()

            if 'http' not in url:
                url = 'https://www.' + url

            phishTank = PhishTank()
            result = phishTank.check(url)
            if result.in_database:
                if result.valid:
                    print("{url} is a phish!".format(url=result.url))
                    messages.error(request, "Phishing Website: " + url)
                else:
                    print("{url} is not a phish!".format(url=result.url))
                    messages.success(request, "Legitimate Website: " + url)
            else:
                print("{url} is not in the PhishTank database".format(url=result.url))
                model = MachineLearningModel()
                ans = model.pipeline(url)[0]
                if ans == 1:
                    messages.error(request, "Phishing Website: " + url)

                elif ans == 0:
                    messages.success(request, "Legitimate Website: " + url)

        except Exception as ex:
            print(ex)
            messages.error(request, "There was Some Error in Prediction... Please Try Again")

    return redirect('/')