from decimal import Decimal
from eshop_orders.models import Orders, OrderDetail
from shop_products.models import Products
from django.core.exceptions import ObjectDoesNotExist


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        if 'products' not in self.session:
            self.session['products'] = dict()

    def __str__(self):
        return str(self.session['products'])

    def __iter__(self):
        products = None
        try:
            session = self.session['products']
        except KeyError:
            session = None
        else:
            cart = [str(i['id']) for i in self.session['products'].values()]
            items = self.session['products'].copy()
            products = Products.objects.filter(id__in=cart)
            for product in products:
                items[str(product.id)]['product'] = product
            for item in items.values():
                item['total_price'] = item['price'] * item['qty']
                yield item

    def add_to_cart(self, product_id, qty, price):
        if product_id in self.session['products']:
            self.session['products'][product_id]['qty'] = qty
            self.save()
        else:
            self.session['products'].update(
                {product_id: {'id': product_id, 'qty': int(qty), 'price': float(price)}})
            self.save()

    def get_total_amount(self):
        return sum([float(i['qty'] * i['price']) for i in self.session['products'].values()])

    def remove(self, id):
        if str(id) in self.session['products']:
            del self.session['products'][str(id)]
            self.save()

    def qty_down(self, id):
        if str(id) in self.session['products']:
            if self.session['products'][str(id)]['qty'] >= 2:
                self.session['products'][str(id)]['qty'] -= 1
                self.save()

    def qty_up(self, id):
        if str(id) in self.session['products']:
            if self.session['products'][str(id)]['qty'] >= 1:
                self.session['products'][str(id)]['qty'] += 1
                self.save()

    def is_exist(self, id):
        if id in self.session['products']:
            return self.session['products'][id]

    def user_login(self):
        """
        use when we want to transfer session cart to db
        """
        if self.session['products']:
            order = Orders.objects.filter(owner=self.request.user, is_paid=False).first()
            if not order:
                order = Orders.objects.create(owner=self.request.user, is_paid=False)
            for i in self.__iter__():
                try:
                    order_detail = OrderDetail.objects.get(
                        order=order,
                        product=i['product'],
                    )
                except ObjectDoesNotExist:
                    OrderDetail.objects.create(
                        order=order,
                        product=i['product'],
                        price=i['total_price'],
                        count=i['qty'],
                    )
                else:
                    order_detail.count = i['qty']
                    order_detail.price = i['total_price']

        self.clear()

    def clear(self):
        del self.session['products']

    def save(self):
        self.session.modified = True
