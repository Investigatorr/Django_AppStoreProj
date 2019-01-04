from decimal import Decimal # 갯수를 셀거라 demical 숫자체계 사용
from django.conf import settings # 세팅에 적어 둔 값 연동
from shop.models import Product # model에서 product정보를 끌어와 작성해야 함


class Cart(object):        # 카트 관리하는 클래스
    def __init__(self, request):
        self.session = request.session  # 요청받은 세션을 현재 세션에도 저장 => Cart클래스 안에서 아무때나 사용 가능
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:  # cart세션이 없으면 빈 상태로 냅둠
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True