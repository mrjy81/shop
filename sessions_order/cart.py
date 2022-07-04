class Cart:
    def __init__(self, request):
        self.request = request
        # self.request['products'] = list()

    def add_to_cart(self, product_id, qty):

        # if product_id not in self.request['products']:
        #     self.request['products'].append({product_id: {'product': product_id, 'qty': qty}})
        # else:
        #     self.request['products'][product_id]['qty'] += 1
        #     self.save()
        print(self.request)

    def save(self):
        self.request.modified = True
