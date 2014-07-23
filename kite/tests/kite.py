import requests
# "Requests" handles all .get and .post requests, blame them if anything
# goes wrong there.

import json
# Inbuilt python library that kindly translates everything we get and
# send into and out of json.

class Template(object):
    public_key = ''
    # Here is the placeholder variables for the public and secret key's
    # to the server.
    secret_key = ''
    # Used to authorize access to the templates and (hopefully) edits to
    # it as well.
    URL = 'https://www.kite.ly/v1.1/template/'
    # Web address to the json templates.
    
    def __init__(self, template_id, public_key, secret_key):
        # __init__ starts the class and loads most varaibles needed in
        # the rest of the program.
        self.passcode = {
            "Authorization": "ApiKey {}:{}".format(public_key, secret_key),
            "Content-Type": "application/json"
        }
        # Compiles public and secret key's into this mess which from
        # what I understand allows access to the json templates.
        self.glob = requests.get(self.URL, headers=self.passcode).json()
        # Grabs the entire archive on templates and translates it from
        # json, then rightfully titles it "glob".
        self.template_id = template_id
        self.template = self.id_search(template_id)
        if type(self.template) is not str:
            self._from_json()
        self.supported_currencies = []
        for i in range(0, len(self.template['cost'])):
            currency = self.template['cost'][i]['currency']
            self.supported_currencies.append(currency)

    def name_search(self, criteria):
        """
        Allows for searching for individual templates by name.
        I dunno, it's nice to have but isn't really used.
        """
        found = False
        for i in range(0, len(self.glob['objects'])):
            # Starts a loop that checks every template in 'objects' from
            # the json glob.
            if criteria == self.glob['objects'][i]['name']:
                # Checks the name of each template against the name
                # given by the user.
                return self.glob['objects'][i]
                # Returns the template they asked for (hopefully), keep
                # in mind this only cuts the fat off of the glob, but it
                # is still a bloody mess.
        
    def id_search(self, criteria=None):
        """
        Allows for searching for individual templates by template_id.
        """
        if not criteria:
            criteria = self.template_id
        found = False
        for i in range(0, len(self.glob['objects'])):
            # Goes through all templates in the json glob...
            if criteria == self.glob['objects'][i]['template_id']:
                # ...looking for a match to the template_id of the
                # template.
                return self.glob['objects'][i]
                # Returns the template they asked for (hopefully), keep
                # in mind this only cuts the fat off of the glob, but it
                # is still a bloody mess.
                found = True
        if not found:
            error = 'Template "'+self.template+'" does not exsist.'
            result = "No information availible."
            not_found_message = error + '\n' + result
            return not_found_message
        
    def get_cost(self, currency=None):
        """
        Finds the information relating to the cost of the product.
        Will give all currencies if not specified.
        """
        m = self.template        
        
        if currency != None:
            # If they have preferenced a currency...
            for i in range(0, len(m['cost'])):
                # ...it begins to look...
                if currency == m['cost'][i]['currency']:
                    # ...for the currency which they wanted...
                    return m['cost'][i]
                    # ...and then shortens the result to just that
                    # currency.
        else:
            for j in range(0, len(m['cost'])):
                if m['cost'][j]['currency'] == 'GBP':
                    return m['cost'][j]
            # Otherwise they just get the whole lot.

    def get_defaults(self):
        """
        Returns the default data attributed to the template
        """
        m = self.template
        return m['default_content']

    def get_overrides(self):
        """
        This finds the data overrides for a template (if any)
        """
        m = self.template
        if m['content_overrides'] == 'null':
            # If the template doesn't have any overrides the program
            # prints out a generic reply...
            nothing = ('Nothing has been changed. Template "'+self.template_id+
                       '" is using default settings.')
            return nothing
            # ...and returns it.
        else:
            # Otherwise it just returns any and all overrides.
            return m['content_overrides']

    def edit(self, content_name, content_value):
        """
        Allows for the editing of the current template
        """
        product = self.template
        if product['content_overrides'] == "null":
            product['content_overrides'] = {}
            product['content_overrides'][content_name] = content_value
        else:
            product['content_overrides'][content_name] = content_value
        self.template = product

    def _to_json(self):
        """
        Updates self.glob with the current state of the template.
        Does this automatically when you run commit.
        """
        for i in range(0, len(self.glob['objects'])):
            if self.glob['objects'][i]['template_id'] == self.template_id:
                self.glob['objects'][i] = self.template
    
    def commit(self):
        """
        Post's the current template in its current state to the server
        """
        self._to_json()
        # Puts the template (assuming it has been edited) back into
        # self.glob for posting (effectively updating self.glob).
        requests.post(self.URL, data=self.glob, headers=self.passcode).json()

    def _from_json(self):
        """
        Translates mass data sent to the program into single variables
        with the same name as they were given in the json format.
        This is run automatically on class initiallation.
        """
        m = self.get_defaults()
        o = self.get_overrides()
        
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

class PrintOrder(object):

    default_shipping_address = {
        "recipient_name": "Bilbo Baggins",
        "address_line_1": "Bag End",
        "address_line_2": "",
        "city": "Hobbiton",
        "county_state": "The Shire",
        "country_code": "GBR"
        }

    def __init__(self, staging=False):
        if staging:
            self.base_url = "http://staging.kite.ly/v1.1/"
        else:
            self.base_url = "https://www.kite.ly/v1.1/"
        self.assets = []

    def set_credentials(self, public_key, secret_key):
        self.public_key = public_key
        self.secret_key = secret_key

    def upload_files(self, files, asset_descriptions=None, client_asset=None):
        print
        print "Registering %s files" % len(files)
        print
        mime_types = ",".join(f['content_type'] for f in files)
        signing_response = self._get_request("asset/sign/?mime_types=%s" % mime_types, params={})
        print "Got signing response from Kite"
        print
        for i, f in enumerate(files):
            d = open(f['filepath'])
            print "uploading image %s / %s (%s)" % (i + 1, len(files), f['filepath'])
            requests.put(
                url=signing_response['signed_requests'][i],
                headers={"x-amz-acl": "private", "Content-Type": f['content_type']},
                data=d
                )
            d.close()
            asset_id = signing_response['asset_ids'][i]
            if f.get('crop_instructions', None):
                print 'CROPPING: resource_uri": "/v1.1/asset/%d/' % asset_id
                data = {"objects": [{
                    "resource_uri": "/v1.1/asset/%d/" % asset_id,
                    "crop_x": f.get('crop_instructions')['x'],
                    "crop_y": f.get('crop_instructions')['y'],
                    "crop_width": f.get('crop_instructions')['width'],
                    "crop_height": f.get('crop_instructions')['height']
                }]}
                res = requests.patch(
                    os.path.join(self.base_url, 'asset/'),
                    data=json.dumps(data),
                    headers=self._headers)
                print res.status_code
                print res.content
            self.assets.append(asset_id)
        return self.assets

    def register_remote_asset(self, url):
        res = self._post_request('asset/', data=json.dumps({'url': url}))
        asset_id = res['asset_id']
        self.assets.append(asset_id)
        return asset_id

    def submit(self, shipping_address=None, user_data=None):
        print
        print "Submitting order..."
        if not shipping_address:
            shipping_address = self.default_shipping_address
        if not user_data:
            user_data = {}
        responses = []
        for template_id in self.templates:
            jobs = [self._job_factory(template_id, self.assets)]
            if type(jobs) != list:
                jobs = [jobs]
            data = {"jobs": jobs, "shipping_address": shipping_address}
            res = self._post_request("print/", data=json.dumps(data))
            print res
            responses.append(res)
        return responses

    def address_search(self, address_data):
        return self._get_request("address/search/", params=address_data)

    @staticmethod
    def _job_factory(template_id, assets):
        return {
            'template_id': template_id,
            'assets': assets,
        }

    @property
    def _headers(self):
        return {
            "Authorization": "ApiKey {}:{}".format(self.public_key, self.secret_key),
            "Content-Type": "application/json",
        }

    def _get_request(self, url, params=None):
        url = os.path.join(self.base_url, url)
        r = requests.get(url, headers=self._headers)
        return r.json()

    def _post_request(self, url, data):
        url = os.path.join(self.base_url, url)
        r = requests.post(url, data=data, headers=self._headers)
        return r.json()
