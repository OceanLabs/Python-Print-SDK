place.there(URL, data, passcode)

data = {'massive':{}, 'dictionary':{}}

def edit_thing(thing_name, thing_data, product_id):
    product = self.id_search(product_id)
    if product[u'content_overrides'] == "null":
        product[u'content_overrides'] = {}
        product[u'content_overrides'][thing_name] = thing_data
    else:
        product[u'content_overrides'][thing_name] = thing_data
    for i in range(0, len(self.blob[u'objects'])):
        if self.blob[u'objects'][i][u'template_id'] == product_id:
            self.blob[u'objects'][i] = product
    post(self.blob)

def edit_cost(currency, nu_price, product_id):
    product = self.cost_finder(product_id)
    if product[u'content_overrides'] == "null":
        product[u'content_overrides'] = {}
        product[u'content_overrides'][thing_name] = thing_data
    else:
        product[u'content_overrides'][thing_name] = thing_data
    for i in range(0, len(self.blob[u'objects'])):
        if self.blob[u'objects'][i][u'template_id'] == product_id:
            self.blob[u'objects'][i] = product
    post(self.blob)
