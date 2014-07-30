import random
import unittest

from kite import Template

class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.public_key = '7ea493ad22d5930f753cf40e9df9b254bc086a77'
        # Make sure these are test credentials.
        self.secret_key = 'a8f99f40c29cc677d1740c322720aa3d9243c43a'
        # Make sure these are test credentials.
    def test_get_cost_given_polaroids_mini(self):
        tests = [
            [
                'USD', 'EUR', 'GBP', 'JPY', '', None
                ],
            [
                '7.00', '5.00', '4.00', "Currency is not supported.",
                "Currency is not supported.", '4.00'
                ]
            ]
        template = Template("polaroids_mini", self.public_key, self.secret_key)
        for i in range(0, len(tests[0])):
            cost = template.get_cost(tests[0][i])
            self.assertEquals(cost, tests[1][i])
        cost = template.get_cost()
        self.assertEquals(cost, '4.00')
    def test_get_cost_given_polaroids(self):
        tests = [
            [
                'USD', 'EUR', 'GBP', 'JPY', '', None
                ],
            [
                '7.00', '5.00', '4.00', "Currency is not supported.",
                "Currency is not supported.", '4.00'
                ]
            ]
        template = Template("polaroids", self.public_key, self.secret_key)
        for i in range(0, len(tests[0])):
            cost = template.get_cost(tests[0][i])
            self.assertEquals(cost, tests[1][i])
        cost = template.get_cost()
        self.assertEquals(cost, '4.00')
    def test_get_cost_given_default_postcard(self):
        tests = [
            [
                'USD', 'EUR', 'GBP', 'JPY', '', None
                ],
            [
                '2.49', '1.99', '1.49', "Currency is not supported.",
                "Currency is not supported.", '1.49'
                ]
            ]
        template = Template(
            "default_postcard", self.public_key, self.secret_key
            )
        for i in range(0, len(tests[0])):
            cost = template.get_cost(tests[0][i])
            self.assertEquals(cost, tests[1][i])
        cost = template.get_cost()
        self.assertEquals(cost, '1.49')
    def test_get_cost_given_magnets(self):
        tests = [
            [
                'USD', 'EUR', 'GBP', 'JPY', '', None
                ],
            [
                '14.00', '10.00', '12.50', "Currency is not supported.",
                "Currency is not supported.", '12.50'
                ]
            ]
        template = Template("magnets", self.public_key, self.secret_key)
        for i in range(0, len(tests[0])):
            cost = template.get_cost(tests[0][i])
            self.assertEquals(cost, tests[1][i])
        cost = template.get_cost()
        self.assertEquals(cost, '12.50')
    def test_get_cost_given_squares(self):
        tests = [
            [
                'USD', 'EUR', 'GBP', 'JPY', '', None
                ],
            [
                '7.00', '5.00', '4.00', "Currency is not supported.",
                "Currency is not supported.", '4.00'
                ]
            ]
        template = Template("squares", self.public_key, self.secret_key)
        for i in range(0, len(tests[0])):
            cost = template.get_cost(tests[0][i])
            self.assertEquals(cost, tests[1][i])
        cost = template.get_cost()
        self.assertEquals(cost, '4.00')
    def test_get_cost_given_squares_mini(self):
        tests = [
            [
                'USD', 'EUR', 'GBP', 'JPY', '', None
                ],
            [
                '7.00', '5.00', '4.00', "Currency is not supported.",
                "Currency is not supported.", '4.00'
                ]
            ]
        template = Template("squares_mini", self.public_key, self.secret_key)
        for i in range(0, len(tests[0])):
            cost = template.get_cost(tests[0][i])
            self.assertEquals(cost, tests[1][i])
        cost = template.get_cost()
        self.assertEquals(cost, '4.00')
    
    def test_get_defaults_polaroids_mini(self):
        template = Template("polaroids_mini", self.public_key, self.secret_key)
        defaults = template.get_defaults()
        self.assertEquals(defaults, {
            "address_code_index": 20, "border": 11.9055118,
            "bottom_grip": 28.3464567, "colors": [],
            "group_gutter": 0, "groups_x": 1,
            "groups_y": 1, "gutter_bleed": 8.50393701,
            "image_replacements": {}, "is_image_grid": True,
            "left_grip": 14.173228, "nx": 4,
            "ny": 6, "pages": [{
                "frames": [], "images": [],
                "name": "second", "strings": []
                }],
            "paragraph_styles": [], "polaroid_grip": 22.67716536,
            "unit_height": 176.0314960629, "unit_width": 153.354331
            })
    def test_get_defaults_polaroids(self):
        template = Template("polaroids", self.public_key, self.secret_key)
        defaults = template.get_defaults()
        self.assertEquals(defaults, {
            "address_code_index": 9, "border": 17.007874,
            "bottom_grip": 28.3464567, "colors": [],
            "group_gutter": 0, "groups_x": 1,
            "groups_y": 1, "gutter_bleed": 8.50393701,
            "image_replacements": {}, "is_image_grid": True,
            "left_grip": 14.173228, "nx": 3,
            "ny": 4, "pages": [{
                "frames": [], "images": [], "name": "second", "strings": []
                }],
            "paragraph_styles": [], "polaroid_grip": 39.68503938,
            "unit_height": 252.2834645668, "unit_width": 212.598425
            })
    def test_get_defaults_default_postcard(self):
        template = Template(
            "default_postcard", self.public_key, self.secret_key
            )
        defaults = template.get_defaults()
        self.assertEquals(defaults, {
            "colors": [
                {"name": "BLACK", "value": "#1a1919"},
                {"name": "NAVY", "value": "#000F55"}
                ],
            "page_height": 306.14173236, "page_width": 429.448819005,
            "pages": [
                {
                    "frames": [],
                    "images": [
                        {
                            "default_id": "1",
                            "height": 306.14173236,
                            "name": "photo",
                            "preserve_aspect_ratio": 1,
                            "width": 429.448819005,
                            "x": 0,
                            "y": 0
                            },
                        {
                            "default_id": "",
                            "height": 306.14173236,
                            "name": "overlay_image",
                            "preserve_aspect_ratio": 1,
                            "width": 429.448819005,
                            "x": 0,
                            "y": 0
                            }
                        ],
                    "name": "first",
                    "strings": []
                    },
                {
                    "background_pdf_id": "7",
                    "frames": [
                        {
                            "height": 170.28,
                            "image": {
                                "align": "left",
                                "bottom_padding": 0,
                                "default_id": "2",
                                "height": 49.019,
                                "left_padding": 0,
                                "preserve_aspect_ratio": 1,
                                "right_padding": 11,
                                "top_padding": 0,
                                "width": 41.572
                                },
                            "name": "frame1",
                            "on_overflow": "truncate",
                            "width": 194.134,
                            "x": 46.531,
                            "y": 92.32
                            },
                        {
                            "height": 11,
                            "name": "addr1",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 197.365
                            },
                        {
                            "height": 11,
                            "name": "addr2",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 176.873
                            },
                        {
                            "height": 11,
                            "name": "addr3",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 156.381
                            },
                        {
                            "height": 11,
                            "name": "addr4",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 135.889
                            },
                        {
                            "height": 11,
                            "name": "addr5",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 115.397
                            },
                        {
                            "height": 11,
                            "name": "addr6",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 94.905
                            },
                        {
                            "height": 11,
                            "name": "addr7",
                            "on_overflow": "shrink",
                            "width": 102.722,
                            "x": 285.295,
                            "y": 74.411
                            },
                        {
                            "height": 28.17,
                            "name": "location",
                            "on_overflow": "shrink",
                            "width": 85.779,
                            "x": 303.021,
                            "y": 31.141
                            }
                        ],
                    "images": [
                        {
                            "default_id": "3",
                            "height": 50,
                            "name": "ppi",
                            "width": 97.62,
                            "x": 310,
                            "y": 225
                            },
                        {
                            "default_id": "4",
                            "height": 18.9,
                            "name": "airmail",
                            "width": 50,
                            "x": 275,
                            "y": 225
                            },
                        {
                            "height": 2.272,
                            "name": "extra_dots",
                            "width": 104.277,
                            "x": 284.904,
                            "y": 70.357
                            },
                        {
                            "height": 17.287,
                            "name": "location_icon",
                            "preserve_aspect_ratio": 1,
                            "width": 12.193,
                            "x": 284.111,
                            "y": 42.021
                            }
                        ],
                    "name": "second",
                    "strings": [
                        {
                            "align": "center",
                            "color": "#d5d5d5",
                            "default_text": "PS300 - XXXXXXXXXXXXXXXX - J123456",
                            "font_id": "10",
                            "font_size": 5,
                            "name": "job_id",
                            "rotate": 90,
                            "x": 150.314,
                            "y": -266.458
                            }
                        ]
                    }
                ],
            "paragraph_styles": [
                {
                    "align": "left",
                    "font_color": "#000F55",
                    "font_id": "8",
                    "font_size": 9,
                    "leading": 20,
                    "name": "body"
                    },
                {
                    "align": "center",
                    "font_color": "#000F55",
                    "font_id": "8",
                    "font_size": 9,
                    "leading": 9,
                    "name": "body-centered"
                    },
                {
                    "align": "left",
                    "font_color": "#0000000",
                    "font_id": "9",
                    "font_size": 8.5,
                    "leading": 8.5,
                    "name": "location1",
                    "space_after": 4
                    },
                {
                    "align": "left",
                    "font_color": "#000000",
                    "font_id": "10",
                    "font_size": 8.5,
                    "leading": 8.5,
                    "name": "location2"
                    },
                {
                    "align": "center",
                    "font_color": "#000F55",
                    "font_id": "",
                    "font_size": 9,
                    "leading": 9,
                    "name": "postcode-or-country"
                    }
                ]
            })
    def test_get_defaults_magnets(self):
        template = Template("magnets", self.public_key, self.secret_key)
        defaults = template.get_defaults()
        self.assertEquals(defaults, {
            "address_code_index": 20, "border": 9.9216,
            "bottom_grip": 28.3464567, "colors": [],
            "group_gutter": 0, "groups_x": 1,
            "groups_y": 1, "gutter_bleed": 8.50393701,
            "image_replacements": {}, "is_image_grid": True,
            "left_grip": 14.173228, "nx": 4,
            "ny": 6, "pages": [
                {
                    "frames": [],
                    "images": [],
                    "name": "second",
                    "strings": []
                    }
                ],
            "paragraph_styles": [], "polaroid_grip": 0,
            "unit_height": 175.74803154, "unit_width": 175.74803154
            })
    def test_get_defaults_squares(self):
        template = Template("squares", self.public_key, self.secret_key)
        defaults = template.get_defaults()
        self.assertEquals(defaults, {
            "address_code_index": 9, "border": 9.9216,
            "bottom_grip": 28.3464567, "colors": [],
            "group_gutter": 0, "groups_x": 1,
            "groups_y": 1, "gutter_bleed": 8.50393701,
            "image_replacements": {}, "is_image_grid": True,
            "left_grip": 14.173228, "nx": 3,
            "ny": 4, "pages": [
                {
                    "frames": [], "images": [], "name": "second", "strings": []
                    }
                ],
            "paragraph_styles": [], "polaroid_grip": 0,
            "unit_height": 256.535433071, "unit_width": 256.535433071
            })
    def test_get_defaults_squares_mini(self):
        template = Template("squares_mini", self.public_key, self.secret_key)
        defaults = template.get_defaults()
        self.assertEquals(defaults, {
            "address_code_index": 20, "border": 9.9216,
            "bottom_grip": 28.3464567, "colors": [],
            "group_gutter": 0, "groups_x": 1,
            "groups_y": 1, "gutter_bleed": 8.50393701,
            "image_replacements": {}, "is_image_grid": True,
            "left_grip": 14.173228, "nx": 4,
            "ny": 6, "pages": [
                {
                    "frames": [], "images": [], "name": "second", "strings": []
                    }
                ],
            "paragraph_styles": [], "polaroid_grip": 0,
            "unit_height": 172.913385827, "unit_width": 172.913385827
            })

    def test_to_json(self):
        edit = Template('polaroids_mini', self.public_key, self.secret_key)
        self.assertEquals(edit.get_overrides(), (
            'Nothing has been changed.' +
            ' Template "polaroids_mini" is using default settings.'
            ))
        edit.address_code_index = 21
        edit.border = 12.3454321
        edit.bottom_grip = 30.3464567
        edit.colors = [
                {"name": "BLACK", "value": "#1a1919"},
                {"name": "NAVY", "value": "#000F55"}
                ]
        edit.group_gutter = 1
        edit.groups_x = 2
        edit.groups_y = 2
        edit.gutter_bleed = 10.40393702
        edit.image_replacements = {'image1': 3, 'image2': 5}
        edit.is_image_grid = False
        edit.left_grip = 12.125448
        edit.nx = 5
        edit.ny = 5
        edit.pages = [{
                "frames": [4, 3, 2, 1, 0], "images": [21, 4],
                "name": "first", "strings": ['Good', 'Job']
                }, {
                "frames": [9, 8, 7, 6, 5], "images": [22, 6],
                "name": "second", "strings": ['Well', 'Done']
                }]
        edit.paragraph_styles = [
                {
                    "align": "left",
                    "font_color": "#000F55",
                    "font_id": "8",
                    "font_size": 9,
                    "leading": 20,
                    "name": "body"
                    },
                {
                    "align": "center",
                    "font_color": "#000F55",
                    "font_id": "8",
                    "font_size": 9,
                    "leading": 9,
                    "name": "body-centered"
                    }
                ]
        edit.polaroid_grip = 20.53316536
        edit.unit_height = 150.1314161621
        edit.unit_width = 181.354331
        edit._to_json()
        overrides = edit.get_overrides()
        self.assertEquals(overrides, {
                'address_code_index': 21,
                'border': 12.3454321,
                'bottom_grip': 30.3464567,
                'colors': [
                    {
                        "name": "BLACK", "value": "#1a1919"
                        },
                    {
                        "name": "NAVY", "value": "#000F55"
                        }
                    ],
                'group_gutter': 1,
                'groups_x': 2,
                'groups_y': 2,
                'gutter_bleed': 10.40393702,
                'image_replacements': {'image1': 3, 'image2': 5},
                'is_image_grid': False,
                'left_grip': 12.125448,
                'nx': 5,
                'ny': 5,
                'pages': [
                    {
                        "frames": [4, 3, 2, 1, 0], "images": [21, 4],
                        "name": "first", "strings": ['Good', 'Job']
                        },
                    {
                        "frames": [9, 8, 7, 6, 5], "images": [22, 6],
                        "name": "second", "strings": ['Well', 'Done']
                        }
                    ],
                'paragraph_styles': [
                    {
                        "align": "left",
                        "font_color": "#000F55",
                        "font_id": "8",
                        "font_size": 9,
                        "leading": 20,
                        "name": "body"
                        },
                    {
                        "align": "center",
                        "font_color": "#000F55",
                        "font_id": "8",
                        "font_size": 9,
                        "leading": 9,
                        "name": "body-centered"
                        }
                    ],
                'polaroid_grip': 20.53316536,
                'unit_height': 150.1314161621,
                'unit_width': 181.354331
                })

if __name__ == '__main__':
    unittest.main()
