from django.shortcuts import render, get_object_or_404, redirect
from .models import Info
from .forms import InfoForm
import requests
import json
import http.client
key = "BS4E80OI6VQTPIXR"

query = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}".format('USD', 'BTC', key)



response = requests.get(query)

print(response.json())

def get_bit(request, name): #api pull
    print("@@@@",name) ##just a test
    query = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}".format('USD', name, key)
    form = InfoForm(request.POST or None)
    response = requests.get(query)
    #print('!!!!', response.json()['Realtime Currency Exchange Rate']['6. Last Refreshed'])
    context = {'response': response.json()['Realtime Currency Exchange Rate'],
               'form': form}
    print('!!!!', context['response']['6. Last Refreshed']) #test
    print(type(context['response'])) #test
    return render(request, 'CryptoCurrency/crypto_api.html', context) #returns the render to the API page

def home(request):
    return render(request, 'CryptoCurrency/crypto_home.html')

def details(request, pk):

    pk = int(pk)  # Casts value of pk to an int so it's in the proper form
    info = get_object_or_404(Info, pk=pk)  # Gets single instance of the info from the database
    context = {'info': info}  # Creates dictionary object to pass the info object
    return render(request, 'CryptoCurrency/crypto_details.html', context)
# Create your views here.

def add_collection(request):
    form = InfoForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/info to the database
        return redirect('cryptoList')                #Redirects to the index page, which is named 'cryptoList' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = InfoForm()                     #Creates a new blank form
    return render(request, 'CryptoCurrency/crypto_create.html', {'form':form})

def index(request):
    get_Info = Info.info.all()      #Gets all the current info from the database
    context = {'Info': get_Info}      #Creates a dictionary object of all the info for the template
    return render(request, 'CryptoCurrency/crypto_index.html', context)

def edit(request, pk):
    pk = int(pk)  # Casts value of pk to an int so it's in the proper form
    info = get_object_or_404(Info, pk=pk)
    if request.method == "POST":
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            return redirect('websites', pk=info.pk)
    else:
        form = InfoForm(instance=info)
        return render(request, 'CryptoCurrency/Crypto_edit.html', {'form': form})
def delete(request, pk):
    pk = int(pk)                               #Casts value of pk to an int so it's in the proper form
    info = get_object_or_404(Info, pk=pk)
    if request.method == "POST":
        info.delete()
        return redirect('websites')
    context = {'Info':info}
    return render(request, 'CryptoCurrency/crypto_delete.html', context)
