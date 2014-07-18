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
                self.groups_x = m[u'groups_x']
                self.groups_y = m[u'groups_y']
                self.gutter_bleed = m[u'gutter_bleed']
                self.image_replacements = m[u'image_replacements']
                self.is_image_grid = m[u'is_image_grid']
                self.left_grip = m[u'left_grip']
                self.nx = m[u'nx']
                self.ny = m[u'ny']
                self.pages = m[u'pages']
                self.paragraph_styles = m[u'paragraph_styles']
                self.polaroid_grip = m[u'polarpoid_grip']
                self.unit_height = m[u'unit_height']
                self.unit_width = m[u'unit_width']
            else:
                if u'address_code_index' in o.keys():
                    self.address_code_index = o[u'address_code_index']
                else:
                    self.address_code_index = m[u'address_code_index']
                if u'border' in o.keys():
                    self.border = o[u'border']
                else:
                    self.border = m[u'border']
                if u'bottom_grip' in o.keys():
                    self.bottom_grip = o[u'bottom_grip']
                else:
                    self.bottom_grip = m[u'bottom_grip']
                if u'colors' in o.keys():
                    self.colors = o[u'colors']
                else:
                    self.colors = m[u'colors']
                if u'group_gutter' in o.keys():
                    self.group_gutter = o[u'group_gutter']
                else:
                    self.group_gutter = m[u'group_gutter']
                if u'groups_x' in o.keys():
                    self.groups_x = o[u'groups_x']
                else:
                    self.groups_x = m[u'groups_x']
                if u'groups_y' in o.keys():
                    self.groups_y = o[u'groups_y']
                else:
                    self.groups_y = m[u'groups_y']
                if u'gutter_bleed' in o.keys():
                    self.gutter_bleed = o[u'gutter_bleed']
                else:
                    self.gutter_bleed = m[u'gutter_bleed']
                if u'image_replacements' in o.keys():
                    self.image_replacements = o[u'image_replacements']
                else:
                    self.image_replacements = m[u'image_replacements']
                if u'is_image_grid' in o.keys():
                    self.is_image_grid = o[u'is_image_grid']
                else:
                    self.is_image_grid = m[u'is_image_grid']
                if u'left_grip' in o.keys():
                    self.left_grip = o[u'left_grip']
                else:
                    self.left_grip = m[u'left_grip']
                if u'nx' in o.keys():
                    self.nx = o[u'nx']
                else:
                    self.nx = m[u'nx']
                if u'ny' in o.keys():
                    self.ny = o[u'ny']
                else:
                    self.ny = m[u'ny']
                if u'pages' in o.keys():
                    self.pages = o[u'pages']
                else:
                    self.pages = m[u'pages']
                if u'paragraph_styles' in o.keys():
                    self.paragraph_styles = o[u'paragraph_styles']
                else:
                    self.paragraph_styles = m[u'paragraph_styles']
                if u'polarpoid_grip' in o.keys():
                    self.polarpoid_grip = o[u'polarpoid_grip']
                else:
                    self.polarpoid_grip = m[u'polarpoid_grip']
                if u'unit_height' in o.keys():
                    self.unit_height = o[u'unit_height']
                else:
                    self.unit_height = m[u'unit_height']
                if u'unit_width' in o.keys():
                    self.unit_width = o[u'unit_width']
                else:
                    self.unit_width = m[u'unit_width']
                    
                    
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
