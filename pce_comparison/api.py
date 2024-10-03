# pce_comparison/api.py

from ninja import Router
import requests

router = Router()

@router.get("/compare")
def compare_products(request):
    # Get products from the scraper API
    response = requests.get("http://web:8000/api/scraper/products")
    products = response.json()

    # Mock comparison logic
    comparison_result = {}
    for product in products:
        title = product['title']
        price = product['price']
        if title not in comparison_result or price < comparison_result[title]['price']:
            comparison_result[title] = {'price': price, 'product': product}
    
    return comparison_result

