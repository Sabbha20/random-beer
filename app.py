from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def get_beer():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beer_json = r.json()
    
    beer = {
        "name":beer_json[0]['name'],
        "tagline":beer_json[0]['tagline'],
        "first_brewed":beer_json[0]['first_brewed'],
        "description":beer_json[0]['description'],
        "image_url":beer_json[0]['image_url'],
        "brewers_tips":beer_json[0]['brewers_tips'],
        "contributed_by":beer_json[0]['contributed_by'],
        "food_pairing":beer_json[0]['food_pairing'],
        "abv":beer_json[0]['abv'],
        "attenuation_level":beer_json[0]['attenuation_level'],
        "ph":beer_json[0]['ph'],
        "ebc":beer_json[0]['ebc'],
        "volume_val":beer_json[0]['volume']['value'],
        "volume_unit":beer_json[0]['volume']['unit'],
        "boil_volume_val":beer_json[0]['boil_volume']['value'],
        "boil_volume_unit":beer_json[0]['boil_volume']['unit'],
        "malt":beer_json[0]['ingredients']['malt'],
        "hops":beer_json[0]['ingredients']['hops'],
        "yeast":beer_json[0]['ingredients']['yeast'],
        
    }
    
    # print(beer_json[0]['name'])
    return render_template("index.html", beer=beer)


if __name__ == '__main__':
    app.run(debug=True)