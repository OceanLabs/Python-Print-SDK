"""
This file contains the class's: 'Template' and 'PrintOrder'. Together
they allow for intergrated printing and editing of polaroids, pictures,
and postcards into larger applications. Template is used for the
importing, reading, editing, and exporting of json templates of
availible print products. PrintOrder is used for arranging an order for
a product in a format that the server will accept. It also handles the
upload of assets to be used in the order.
"""

# Imports generally don't need comments
# Standard library imports in alphabetical order
import json
import os
from random import shuffle

# 3rd party imports
import requests


class Template(object):
    """
    This class manages the importing, reading, editing, and exporting of
    the json templates from the kite.ly templates server. It imports via
    a HTTPS get call to a json object on the server and exports via a
    HTTPS put call (with a json payload). It requires the public and
    private keys that you are presented with after registration on
    www.kite.ly otherwise you will not be permitted to alter any aspect
    of the template. To edit the price of a template/product can only be
    done from your kite account. All changes will first be commited to
    the "content_overrides" of a template before the server merges it
    with the "content" section of the template information.
    """
    public_key = ''
    # Here is the placeholder variables for the public and secret key's
    # to the server.
    secret_key = ''
    # Used to authorize access to the templates and (hopefully) edits to
    # it as well.
    URL = 'https://www.kite.ly/v1.1/template/'
    # Web address to the json templates.
    
    def __init__(self, template_id, public_key, secret_key):
        """
        When starting the module, please give the template id of the
        template you wish to be working on and your public and secret
        keys. In order for editing of multiple template simultaniously
        initiallise multiple instances of the Template module.
        """
        # __init__ starts the class and loads most varaibles needed in
        # the rest of the program.
        self.passcode = {
            "Authorization": "ApiKey {}:{}".format(public_key, secret_key),
            "Content-Type": "application/json"
        }
        # Compiles public and secret key's into this mess which from
        # what I understand allows access to the json templates.
        self.URL = self.URL + template_id + '/'
        self.glob = requests.get(self.URL, headers=self.passcode).json()
        # Grabs the entire archive on templates and translates it from
        # json, then rightfully titles it "glob".
        self.template_id = template_id
        if type(self.glob) is not str:
            self._from_json(self.glob)
        self.supported_currencies = []
        for cost in range(len(self.glob['cost'])):
            self.supported_currencies.append(
                self.glob['cost'][cost]['currency']
                )
        
    def get_cost(self, currency="GBP"):
        """
        Finds the information relating to the cost of the
        product/template. Will default to GBP if not specified.
        """

        for cost in self.glob['cost']:
            if currency == cost['currency']:
                amount = cost['amount']
                break
        else:
            raise ValueError("Currency is not supported.")
        return amount

    def get_defaults(self):
        """
        Returns the default data (AKA "content") attributed to the
        template
        """
        return self.glob['content']

    def get_overrides(self):
        """
        This finds the data overrides (AKA "content_overrides") for a
        template (if any).
        """
        if self.glob['content_overrides'] == 'null':
            # If the template doesn't have any overrides the program
            # prints out a generic reply...
            nothing = ('Nothing has been changed. Template "'+self.template_id+
                       '" is using default settings.')
            return nothing
            # ...and returns it.
        else:
            # Otherwise it just returns any and all overrides.
            return self.glob['content_overrides']

    def _to_json(self):
        """
        Updates the overrides with the current state of all variables.
        Does this automatically when you run commit().
        """
        if self.template_id == 'default_postcard':
            to_be_sent = {
                'colors': self.colors,
                'page_height': self.page_height,
                'page_width': self.page_width,
                'pages': self.pages,
                'paragraph_styles': self.paragraph_styles
                }
        else:
            to_be_sent = {
                'address_code_index': self.address_code_index,
                'border': self.border,
                'bottom_grip': self.bottom_grip,
                'colors': self.colors,
                'group_gutter': self.group_gutter,
                'groups_x': self.groups_x,
                'groups_y': self.groups_y,
                'gutter_bleed': self.gutter_bleed,
                'image_replacements': self.image_replacements,
                'is_image_grid': self.is_image_grid,
                'left_grip': self.left_grip,
                'nx': self.nx,
                'ny': self.ny,
                'pages': self.pages,
                'paragraph_styles': self.paragraph_styles,
                'polaroid_grip': self.polaroid_grip,
                'unit_height': self.unit_height,
                'unit_width': self.unit_width
                }
        self.glob['content_overrides'] = to_be_sent
    
    def commit(self):
        """
        Adds all changes to the overrides of the template.
        """
        self._to_json()
        # Puts the template (assuming it has been edited) back into
        # self.glob for posting (effectively updating self.glob).
        requests.put(self.URL, data=self.glob, headers=self.passcode).json()

    def _from_json(self, template):
        """
        Translates mass json dictionary into single variables with the
        same names as they were originally. This is run automatically on
        class initiallation.
        """
<<<<<<< HEAD
        content = template['content']
        
        if template['content_overrides'] != "null":
            content.update({
                allowed_key: template['content_overrides'][allowed_key]
                for allowed_key in set(template['content'].keys()) & set(template['content_overrides'].keys())
            })
        if self.template_id == 'default_postcard':
            self.colors = content['colors']
            self.page_height = content['page_height']
            self.page_width = content['page_width']
            self.pages = content['pages']
            self.paragraph_styles = content['paragraph_styles']
=======

        content = template['content']

        # now you don't have to do lots of if statements because content
        # is a combination of content and overrides
        # this code first synthesises a dictionary that is essentially
        # overrides with any keys that aren't in content removed
        # then updates content with those overrides
        if not forget_override:
            content.update({
                allowed_key: template['content_overrides'][allowed_key]
                for allowed_key in template['content'].keys() & template['content_overrides'].keys()
            })

        if o == "null":
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
                # don't need these branches anymore, but if you did, could omit the .keys()
                if 'colors' in o:  # iterating over a dictionary returns the keys
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
>>>>>>> 538e1819bf83251d500a204e43452590f3720a1b
        else:
            self.address_code_index = content['address_code_index']
            self.border = content['border']
            self.bottom_grip = content['bottom_grip']
            self.colors = content['colors']
            self.group_gutter = content['group_gutter']
            self.groups_x = content['groups_x']
            self.groups_y = content['groups_y']
            self.gutter_bleed = content['gutter_bleed']
            self.image_replacements = content['image_replacements']
            self.is_image_grid = content['is_image_grid']
            self.left_grip = content['left_grip']
            self.nx = content['nx']
            self.ny = content['ny']
            self.pages = content['pages']
            self.paragraph_styles = content['paragraph_styles']
            self.polaroid_grip = content['polaroid_grip']
            self.unit_height = content['unit_height']
            self.unit_width = content['unit_width']

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
