def calculate_ticket_price(age, day):
    base_price = 10  

    if age == "adult":
        base_price += 5
    elif age == "child":
        base_price -= 2
    elif age == "senior":
        base_price -= 3

    if day == "weekend":
        base_price += 3

    return base_price

age_category = "adult"
day_type = "weekend"
ticket_price = calculate_ticket_price(age_category, day_type)
print(f"The ticket price for an {age_category} on a {day_type} is ${ticket_price}.")

        # Ex:2
def calculate_ticket_price(age, day, num_tickets):
    base_price = 10  

    if age == "adult":
        base_price += 5
    elif age == "child":
        base_price -= 2
    elif age == "senior":
        base_price -= 3

    if day == "weekend":
        base_price += 3

    # Apply discounts for groups or family packages
    if num_tickets >= 4:
        base_price *= 0.9  # 10% discount for 4 or more tickets

    return base_price * num_tickets

# Example usage:
age_category = "adult"
day_type = "weekend"
num_tickets = 3
total_price = calculate_ticket_price(age_category, day_type, num_tickets)
print(f"The total price for {num_tickets} {age_category} tickets on a {day_type} is ${total_price}.")



        # Ex:3
def calculate_total_bill(items, quantities, prices, discount=0, tax_rate=0, split_friends=1):
    subtotal = 0

    for item, quantity, price in zip(items, quantities, prices):
        subtotal += quantity * price

    discount_amount = subtotal * discount
    subtotal_after_discount = subtotal - discount_amount
    tax_amount = subtotal_after_discount * tax_rate
    total_amount = subtotal_after_discount + tax_amount
    amount_per_person = total_amount / split_friends

    return {
    "subtotal": subtotal,
    "discount_amount": discount_amount,
    "subtotal_after_discount": subtotal_after_discount,
    "tax_amount": tax_amount,
    "total_amount": total_amount,
    "amount_per_person": amount_per_person
 }

items = ["item1", "item2", "item3"]
quantities = [2, 3, 1]
prices = [10.99, 5.99, 8.50]
discount = 0.1  
tax_rate = 0.07  
split_friends = 3  

bill_details = calculate_total_bill(items, quantities, prices, discount, tax_rate, split_friends)
print("Bill Details:")
for key, value in bill_details.items():
    print(f"{key.capitalize()}: ${value:.2f}")
         


        #  Ex:4


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import emoji
import re

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

def analyze_social_media(text):
    sia = SentimentIntensityAnalyzer()

    emojis = [char for char in text if char in emoji.UNICODE_EMOJI['en']]

    text_no_emojis = ''.join([char for char in text if char not in emojis])

    sentiment_score = sia.polarity_scores(text_no_emojis)['compound']

    if sentiment_score >= 0.05:
        sentiment = 'positive'
    elif sentiment_score <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    tokens = re.findall(r'\b\w+\b', text_no_emojis.lower())

    stop_words = set(stopwords.words('english'))
    keywords = [word for word in tokens if word.isalnum() and word not in stop_words]

    trends = set(keywords)

    return {'sentiment': sentiment, 'emojis': emojis, 'keywords': keywords, 'trends': list(trends)}

social_media_text = "I love this product! It's amazing! 😍👍 #awesome"
result = analyze_social_media(social_media_text)
print(result)



        # EX:5

def estimate_travel_cost(destination, transportation_cost, accommodation_cost, activities_cost):
    total_cost = transportation_cost + accommodation_cost + activities_cost
    print(f"Estimated travel cost for {destination}: ${total_cost}")

destination = "Paris"
transportation_cost = 500
accommodation_cost = 800
activities_cost = 300

estimate_travel_cost(destination, transportation_cost, accommodation_cost, activities_cost)