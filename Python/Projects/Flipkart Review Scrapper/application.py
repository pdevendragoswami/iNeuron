from flask import Flask,request,render_template
from flask_cors import CORS,cross_origin
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import requests
import logging

logging.basicConfig(filename='reviews.log',filemode='w',level=logging.INFO, format = "%(asctime)s %(levelname)s %(msg)s")

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def home_page():
    return render_template('index.html')

@app.route('/review',methods = ["POST","GET"])
def review():
    if request.method == "POST":
        try:
            search_string = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q="
            search_url = flipkart_url+search_string
            uClient = uReq(search_url)
            flipkart_page = uClient.read()
            flipkart_html = bs(flipkart_page,"html.parser")
            bigboxes = flipkart_html.findAll("div",{"class":"_2kHMtA"})
            product_link = "https://www.flipkart.com"+bigboxes[0].a['href']
            product_page = requests.get(product_link)
            product_html = bs(product_page.text,"html.parser")
            comment_box = product_html.findAll("div",{"class":"col _2wzgFH"})
            file_name = search_string + ".csv"
            file = open(file_name,"w")
            headers = "Product, Customer Name, Place, Rating, Heading, Comment, Date \n"
            file.write(headers)

            reviews = []
            for value in comment_box:
                try:
                    name = value.findAll("p",{"class":"_2sc7ZR _2V5EHH"})[0].text
                    logging.info("name found")
                except:
                    name = 'NA'
                    logging.info("name not found")
                try:
                    place = value.findAll("p",{"class":"_2mcZGG"})[0].text
                    logging.info("place found")
                except:
                    place = "NA"
                    logging.info("place not found")
                try:
                    rating = value.findAll("div",{"class":"_3LWZlK _1BLPMq"})[0].text
                    logging.info("rating found")
                except:
                    rating = "NA"
                    logging.info("rating not found")
                try:
                    comment_head = value.findAll("p",{"class":"_2-N8zT"})[0].text
                    logging.info("comment_head found")
                except:
                    comment_head = "NA"
                    logging.info("comment_head not found")
                try:
                    comment = value.findAll("div",{"class":""})[0].div.text
                    logging.info("comment found")
                except:
                    comment = "NA"
                    logging.info("comment not found")
                try:
                    date = value.findAll("p",{"class":"_2sc7ZR"})[1].text
                    logging.info("Date  found")
                except:
                    date = "NA"
                    logging.info("date not found")
                
                


                
                mydict = {"Product":search_string,"Name":name,"Place":place,"Rating":rating,
                "Comment_Head":comment_head,"Comment":comment,"Date":date}
                reviews.append(mydict)
                row_values = search_string+","+name+","+place+","+rating+","+comment_head+","+comment+","+date+" \n"
                file.write(row_values)
                logging.info("Values addded to the list")
            file.close()
            return render_template('result.html',reviews = reviews[0:len(reviews)-1])
        except Exception as e:
            logging.info(e)
            return 'there is some issue'
    else:
         return render_template('result.html')





if __name__ == "__main__":
    app.run(host="0.0.0.0")
