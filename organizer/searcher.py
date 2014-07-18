import requests as r
import json


class searcher:
    public_key = "7ea493ad22d5930f753cf40e9df9b254bc086a77"
    secret_key = "a8f99f40c29cc677d1740c322720aa3d9243c43a"
    def __init__(self):
        passcode = {"Authorization": "ApiKey {}:{}".format(self.public_key, self.secret_key),
                    "Content-Type": "application/json"}
        self.glob = r.get('https://www.kite.ly/v1.1/template/', headers=passcode).json()
        print(self.glob)

    def name_search(self, criteria):
        for i in range(0, len(self.glob[u'objects'])):
            if criteria == self.glob[u'objects'][i][u'name']:
                return self.glob[u'objects'][i]

    def id_search(self, criteria):
        for i in range(0, len(self.glob[u'objects'])):
            if criteria == self.glob[u'objects'][i][u'template_id']:
                return self.glob[u'objects'][i]

    def cost_finder(self, product_id, cur = 'none'):
        m = self.id_search(product_id)
        
        if cur != 'none':
            for i in range(0, len(m)):
                if cur == m[u'cost'][i][u'currency']:
                    return m[u'cost'][i]
        else:
            return m[u'cost']

    def data_finder(self, product_id):
        m = self.id_search(product_id)
        return m[u'default_content']

    def override_finder(self, product_id):
        m = self.id_search(product_id)
        if m[u'content_overrides'] == 'null':
            nothing = 'Nothing has been changed. Template "'+product_id+'" is using default settings.'
            return nothing
        else:
            return m[u'content_overrides']

    def burp():
        return self.glob

    def data_cruncher(self, product_id):
        m = self.data_finder(product_id)
        o = self.override_finder(product_id)
        
        if o[0:7] == "Nothing":
            forget_override = True
        else:
            forget_override = False
        
        if product_id == u'polaroids_mini':
            if forget_override:
                self.address_code_index = m[u'address_code_index']
                self.border = m[u'border']
                self.bottom_grip = m[u'bottom_grip']
                self.colors = m[u'colors']
                self.group_gutter = m[u'group_gutter']
                self.groups = [m[u'groups_x'], m[u'groups_y']]
                self.gutter_bleed = m[u'gutter_bleed']
                self.image_replacements = m[u'image_replacements']
                self.is_image_grid = m[u'is_image_grid']
                self.left_grip = m[u'left_grip']
                self.n = [m[u'nx'], m[u'ny']]
                self.pages = m[u'pages']
                self.paragraph_styles = m[u'paragraph_styles']
                self.polaroid_grip = m[u'polarpoid_grip']
                self.unit = [m[u'unit_height'], m[u'unit_width']]
            else:
                break
        elif product_id == u'polaroids':
            break
        elif product_id == u'default_postcard':
            break
        elif product_id == u'magnets':
            break
        elif product_id == u'squares':
            break
        elif product_id == u'squares_mini'
            break
        else:
            return 'Id "'+product_id+'" is not valid.'
        
        

n = searcher()
print('\n')
print(n.name_search('Polaroid minis'))
print('\n')
m= n.id_search(u"polaroids")
print(m)
print('\n')
print(n.cost_finder(u"polaroids", cur = u'EUR'))
print('\n')
print(n.data_finder(u'default_postcard'))
print('\n')
print(n.override_finder(u'polaroids'))
print('\n')
