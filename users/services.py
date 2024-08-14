import stripe

from config import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_product(product):
    """Создает новый stripe продукт"""
    product_paid = product.paid_course if product.paid_course else product.paid_lesson
    stripe_product = stripe.Product.create(name=product_paid.title)
    return stripe_product


def create_stripe_price(product_id, amount):
    """Создает stripe цену"""
    return stripe.Price.create(
        product=product_id,
        unit_amount=amount * 100,
        currency="rub"
    )


def create_stripe_session(price):
    """
    Создает сессию и оплату в Stripe
     """
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
