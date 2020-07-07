import tweepy
import os
from fastapi import FastAPI, HTTPException
from tinydb import TinyDB, Query
from datetime import datetime


app = FastAPI()

@app.get('/start')
async def hello():
    if os.path.isfile("hts.json"):
        return {'Setup Status': 'Hashtag file already setup!'}

    consumer_key = "AvYE7UaVgkLMgYZw6JrgvL8T3"
    consumer_secret = "PmxOzQUDky5TFOUl9BvzXlpyAYheoWMIGsXN67K5jk0TRBsfOg"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        raise HTTPException(status_code=500, detail="Error! Failed to get request token.")
        return
    api = tweepy.API(auth)
    hts = ['#openbanking', '#remediation', '#devops', '#sre', '#microservices', '#observability', '#oauth', '#metrics', '#logmonitoring', '#opentracing']
    db = TinyDB('hts.json')
    for ht in hts:
        tweets = tweepy.Cursor(api.search, q=str(ht)).items(100)
        for tweet in tweets:
            db.insert({ 'hashtag' : ht, 'content' : tweet._json })

    return {'Setup Status': 'Done! All necessary hashtags collected'}

@app.get('/hashtags/{hashtag_str}')
async def read_hashtag(hashtag_str: str):
    if '#' not in hashtag_str:
        hashtag_str = "#"+hashtag_str
    if not os.path.isfile("hts.json"):
        raise HTTPException(status_code=500, detail="No database present. Run setup first.")
    db = TinyDB('hts.json')
    Hashtag = Query()
    result = db.search(Hashtag.hashtag == hashtag_str)
    if not result:
        raise HTTPException(status_code=404, detail="Hashtag not found")
    return result

@app.get('/hashtags/')
async def read_hashtags():

    if not os.path.isfile("hts.json"):
        raise HTTPException(status_code=500, detail="No database present. Run setup first.")
    db = TinyDB('hts.json')
    return db.all()

@app.get('/top5/')
async def top_5():
    if not os.path.isfile("hts.json"):
        raise HTTPException(status_code=500, detail="No database present. Run setup first.")
    db = TinyDB('hts.json')
    result = { }
    for item in db:
        result.update({ item['content']['user']['screen_name'] : item['content']['user']['followers_count'] })
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)[:5]}
    return result

@app.get('/tophour/')
async def top_hour():
    if not os.path.isfile("hts.json"):
        raise HTTPException(status_code=500, detail="No database present. Run setup first.")
    db = TinyDB('hts.json')
    result = { }
    for item in db:
        hour = datetime.strftime(datetime.strptime(item['content']['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%H')
        count = result.get(hour)
        if count:
            count += 1
        else:
            count = 0
        result.update({ hour : int(count+1)})
    return result

@app.get('/toplang/')
async def top_lang():
    if not os.path.isfile("hts.json"):
        raise HTTPException(status_code=500, detail="No database present. Run setup first.")
    db = TinyDB('hts.json')
    result = { }
    for item in db:
        lang = item['content']['lang']
        count = result.get(lang)
        if count:
            count += 1
        else:
            count = 0
        result.update({ lang : int(count+1)})
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
    return result

