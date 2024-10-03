from ninja import Router
import requests

router = Router()

@router.get("/products")
def get_products(request):
    response = requests.get("https://fakestoreapi.com/products")
    return response.json()

