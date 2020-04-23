from gtts import gTTS   
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):


    html = requests.get("https://www.sabcnews.com/sabcnews/category/south-africa/").text
    soup = BeautifulSoup(html,'html.parser')

    title = soup.find("h1", class_='rpw2e-title').get_text()
    lead_content = soup.find('div',class_='category_lead_excerpt').get_text()
    img = soup.find('img',class_='wp-post-image')['src']
    image_caption = soup.find('div', class_='featured_caption').get_text()

    # Finding picture for sub news

    thumb_images = soup.findAll('img',class_='size-thumb')
    body_title = soup.findAll('span',class_='sabc_cat_list_item_title')
    summary = soup.findAll('p',class_='sabc_cat_list_item_summary')
    links = soup.findAll('span',class_='sabc_cat_list_item_title')
    source_image = []
    source_title = []
    source_sammary = []
    source_link =[]

    for a in links:
        new_link = a.find('a')['href']
        source_link.append(new_link)

    for i in range(len(thumb_images)):
        source_image.append(thumb_images[i]['src'])
        source_title.append(body_title[i].get_text())
        source_sammary.append(summary[i].get_text()[:75])

    mylist = zip(source_image, source_title,source_sammary,source_link)


    context = {
        'title_one':title,
        'lead_content':lead_content,
        'image_title':img,
        'text_and_image':mylist

    }
    return render(request,'base.html',context)

def new_text(request):
    val = request.POST.get("search")
    num = val[:9]
    new_num = num.replace(' ', '')
    audio = gTTS(val)
    new_audio = audio.save(f"./sabc/static/{new_num}.mp3")
    context = {
        "text": val,
        "sound":new_num,
        
    }
    return render(request, 'new_text.html',context)

    