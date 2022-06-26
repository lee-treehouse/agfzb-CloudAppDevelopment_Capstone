from cgitb import text
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import requests
import json
# import related models here
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)    
    print("GET from {} ".format(url))
    api_key = kwargs.get("api_key")
    try:
        if api_key:
        # Call get method of requests library with URL and parameters
            response = requests.get(url, headers={'Content-Type': 'application/json'},  params=kwargs, auth=HTTPBasicAuth('apikey', api_key))
        else: 
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, **kwargs)
    print (json_result)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results


def analyze_review_sentiments(text):
    print ("I am here with " + text)
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/7f62941a-710d-4ef7-8799-d2b5e932110b"
    api_key = "vq8pXV1vPJ6xpLAm70CVhO0daaMK18Ya7KGZWzE0DhUd"  

    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url=url, api_key=api_key, text=text)
    if json_result:
        print(json_result)
    return "looks good"


def get_reviews_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result["entries"]
        # For each dealer object
        for review in reviews:
            #get the sentiment 
            review_text = review.get("review")
            sentiment = ""
            if (review_text):
                sentiment = "neutral"
                #sentiment = analyze_review_sentiments(review_text)

            # Get its content in `doc` object
            # Create a CarDealer object with values in `doc` object
            review_obj = DealerReview(id=review["id"], name=review["name"], dealership=review["dealership"],
                                   review=review["review"], sentiment=sentiment, purchase=review["purchase"], purchase_date=review.get("purchase_date"),
                                   car_make=review.get("car_make"),
                                   car_model=review.get("car_model"), car_year=review.get("car_year"))
            results.append(review_obj)

        return results

def analyze_review_sentiments(text):
    print ("I am here with " + text)
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/7f62941a-710d-4ef7-8799-d2b5e932110b"
    api_key = "vq8pXV1vPJ6xpLAm70CVhO0daaMK18Ya7KGZWzE0DhUd"  

    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url=url, api_key=api_key, text=text)
    if json_result:
        print(json_result)
    return "looks good"




    # Create an `analyze_review_sentiments` method to call Watson NLU and analyze text


# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



