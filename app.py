from flask import Flask, render_template
import pandas as pd
from bs4 import BeautifulSoup as soup
import requests 

app = Flask(__name__)

@app.route("/") 
def show_price():
    html_content = soup(requests.get("https://www.nike.com/au/w/golf-shoes-23q9wzy7ok").content, "html")
    product_title_list = html_content.find_all("div", {"class": "product-card__title"})
    title_list = []
    price_list = []
    for product_title in product_title_list:
        title_list.append(product_title.text)

    product_price_list = html_content.find_all("div", {"class": "product-price"})

    for product_price in product_price_list:
        price_list.append(product_price.text)
    product_dict = {
        "title": title_list,
        "price": price_list
    }
    df = pd.DataFrame(product_dict)
    print(df)
    return render_template("index.html", product_dict=product_dict)

if __name__ == "__main__":
    app.run(debug=True)