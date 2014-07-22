import requests
#"Requests" handles all .get and .post requests,
#blame them if anything goes wrong there

import json
#Inbuilt python library that kindly translates
#everything we get and send into and out of json


class Template:
    public_key = ''
    #Here is the placeholder variables for the public and secret key's...
    #...to the server
    secret_key = ''
    #Used to authorize access to the templates...
    #...and (hopefully) edits to it as well
    URL = 'https://www.kite.ly/v1.1/template/'
    #Web address to the json templates
    
    def __init__(self, template_id, public_key, secret_key):
        #__init__ starts the class and loads most varaibles
        #needed in the rest of the program
        self.passcode = {"Authorization": "ApiKey {}:{}".format(public_key,
                                                           secret_key),
                    "Content-Type": "application/json"}
        #compiles public and secret key's into this mess
        #which from what I understand allows access to the json templates
        self.glob = requests.get(self.URL, headers=self.passcode).json()
        #grabs the entire archive on templates and translates it from json,
        #then rightfully titles it "glob"
        self.template_id = template_id
        self.template = self.id_search(template_id)
        if type(self.template) is not str:
            self.data_cruncher()

    def name_search(self, criteria):
        """
        Allows for searching for individual templates by name.
        I dunno, it's nice to have but isn't really used.
        """
        found = False
        for i in range(0, len(self.glob['objects'])):
            #starts a loop that checks every template in 'objects'
            #from the json glob
            if criteria == self.glob['objects'][i]['name']:
                #checks the name of each template against the name given
                #by the user
                return self.glob['objects'][i]#returns the template they asked
                                               #for (hopefully).
                                               #keep in mind this only cuts the
                                               #fat off of the glob,
                                               #but it is still a bloody mess
        
    def id_search(self, criteria=None):
        """
        Allows for searching for individual templates by template_id.
        """
        if not criteria:
            criteria = self.template_id
        found = False
        for i in range(0, len(self.glob['objects'])):
            #goes through all templates in the json glob...
            if criteria == self.glob['objects'][i]['template_id']:
                #...looking for a match to the template_id of the template
                return self.glob['objects'][i]
            #returns the template they asked for (hopefully).
            #keep in mind this only cuts the fat off of the glob,
            #it is still a bloody mess
                found = True
        if not found:
            error = 'Template "'+self.template+'" does not exsist.'
            result = "No information availible."
            not_found_message = error + '\n' + result
            return not_found_message
        
    def cost_finder(self, currency = None):
        """
        Finds the information relating to the cost of the product.
        Will give all currencies if not specified.
        """
        m = self.template        
        
        if not currency:# if they have preferenced a currency...
            for i in range(0, len(m)):# ...it begins to look...
                if currency == m['cost'][i]['currency']:# ...for the currency
                                                          #which they wanted...
                    return m['cost'][i]# ...and then shortens the result to
                                        #just that currency
        else:#otherwise they just get the whole lot
            return m['cost']

    def data_finder(self):
        """
        Returns the default data attributed to the template
        """
        m = self.template
        #this is yet another function that relies on the id_search definition
        return m['default_content']
        #not to worry this function isn't used for any other definition

    def override_finder(self):
        """
        This finds the data overrides for a template (if any)
        """
        m = self.template
        if m['content_overrides'] == 'null':# if the template doesn't
                                             #have any overrides the program
                                             #prints out a generic reply...
            nothing = ('Nothing has been changed. Template "'+self.template_id+
                       '" is using default settings.')
            return nothing# ...and returns it
        else:#Otherwise it just returns any and all overrides
            return m['content_overrides']

    def burp():# not sure what this is, why it's here, or what it's used for...
        return self.glob# ...but it's here

    def edit_thing(self, thing_name, thing_data):
        """
        Allows for the adding of overrides to the default data values
        """
        product = self.id_search(self.template_id)
        if product['content_overrides'] == "null":
            product['content_overrides'] = {}
            product['content_overrides'][thing_name] = thing_data
        else:
            product['content_overrides'][thing_name] = thing_data
        for i in range(0, len(self.glob['objects'])):
            if self.glob['objects'][i]['template_id'] == self.template_id:
                self.glob['objects'][i] = product
        requests.post(self.URL, data=self.glob, headers=self.passcode).json()

    def data_cruncher(self):
        """
        Translates mass data sent to the program into single variables
        with the same name as they were given in the json format.
        This is run automatically on class initiallation.
        """
        m = self.data_finder()
        o = self.override_finder()
        
        if o[0:7] == "Nothing":
            forget_override = True
        else:
            forget_override = False
        if self.template_id == 'default_postcard':
            if forget_override:
                self.colors = m['colors']
                self.page_height = m['page_height']
                self.page_width = m['page_width']
                self.pages = m['pages']
                self.paragraph_styles = m['paragraph_styles']
            else:
                if 'colors' in o.keys():
                    self.colors = o['colors']
                else:
                    self.colors = m['colors']
                if 'page_height' in o.keys():
                    self.page_height = o['page_height']
                else:
                    self.page_height = m['page_height']
                if 'page_width' in o.keys():
                    self.page_width = o['page_width']
                else:
                    self.page_width = m['page_width']
                if 'pages' in o.keys():
                    self.pages = o['pages']
                else:
                    self.pages = m['pages']
                if 'paragraph_styles' in o.keys():
                    self.paragraph_styles = o['paragraph_styles']
                else:
                    self.paragraph_styles = m['paragraph_styles']
        else:
            if forget_override:
                self.address_code_index = m['address_code_index']
                self.border = m['border']
                self.bottom_grip = m['bottom_grip']
                self.colors = m['colors']
                self.group_gutter = m['group_gutter']
                self.groups_x = m['groups_x']
                self.groups_y = m['groups_y']
                self.gutter_bleed = m['gutter_bleed']
                self.image_replacements = m['image_replacements']
                self.is_image_grid = m['is_image_grid']
                self.left_grip = m['left_grip']
                self.nx = m['nx']
                self.ny = m['ny']
                self.pages = m['pages']
                self.paragraph_styles = m['paragraph_styles']
                self.polaroid_grip = m['polaroid_grip']
                self.unit_height = m['unit_height']
                self.unit_width = m['unit_width']
            else:
                if 'address_code_index' in o.keys():
                    self.address_code_index = o['address_code_index']
                else:
                    self.address_code_index = m['address_code_index']
                if 'border' in o.keys():
                    self.border = o['border']
                else:
                    self.border = m['border']
                if 'bottom_grip' in o.keys():
                    self.bottom_grip = o['bottom_grip']
                else:
                    self.bottom_grip = m['bottom_grip']
                if 'colors' in o.keys():
                    self.colors = o['colors']
                else:
                    self.colors = m['colors']
                if 'group_gutter' in o.keys():
                    self.group_gutter = o['group_gutter']
                else:
                    self.group_gutter = m['group_gutter']
                if 'groups_x' in o.keys():
                    self.groups_x = o['groups_x']
                else:
                    self.groups_x = m['groups_x']
                if 'groups_y' in o.keys():
                    self.groups_y = o['groups_y']
                else:
                    self.groups_y = m['groups_y']
                if 'gutter_bleed' in o.keys():
                    self.gutter_bleed = o['gutter_bleed']
                else:
                    self.gutter_bleed = m['gutter_bleed']
                if 'image_replacements' in o.keys():
                    self.image_replacements = o['image_replacements']
                else:
                    self.image_replacements = m['image_replacements']
                if 'is_image_grid' in o.keys():
                    self.is_image_grid = o['is_image_grid']
                else:
                    self.is_image_grid = m['is_image_grid']
                if 'left_grip' in o.keys():
                    self.left_grip = o['left_grip']
                else:
                    self.left_grip = m['left_grip']
                if 'nx' in o.keys():
                    self.nx = o['nx']
                else:
                    self.nx = m['nx']
                if 'ny' in o.keys():
                    self.ny = o['ny']
                else:
                    self.ny = m['ny']
                if 'pages' in o.keys():
                    self.pages = o['pages']
                else:
                    self.pages = m['pages']
                if 'paragraph_styles' in o.keys():
                    self.paragraph_styles = o['paragraph_styles']
                else:
                    self.paragraph_styles = m['paragraph_styles']
                if 'polarpoid_grip' in o.keys():
                    self.polarpoid_grip = o['polarpoid_grip']
                else:
                    self.polarpoid_grip = m['polarpoid_grip']
                if 'unit_height' in o.keys():
                    self.unit_height = o['unit_height']
                else:
                    self.unit_height = m['unit_height']
                if 'unit_width' in o.keys():
                    self.unit_width = o['unit_width']
                else:
                    self.unit_width = m['unit_width']

                
if __name__ == "__main__":
    n = Template('polaroids_mini',
                 '7ea493ad22d5930f753cf40e9df9b254bc086a77',
                 'a8f99f40c29cc677d1740c322720aa3d9243c43a')
    print('\n')
    m= n.id_search("polaroids")
    print(m)
    print('\n')
    print(n.cost_finder(currency = 'EUR'))
    print('\n')
    print(n.data_finder())
    print('\n')
    print(n.override_finder())
    print('\n')
    n.edit_thing("nx", 5)
    print("and the overrides are: ", n.override_finder())
    print(n.id_search("polaroids_mini"))
    print('\n')
    print(n.id_search())
    
