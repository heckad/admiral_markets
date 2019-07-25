from rest_framework.test import APITestCase


class Test(APITestCase):
    test_input_data = {
        "name": "Category 1",
        "children": [
            {
                "name": "Category 1.1",
                "children": [
                    {
                        "name": "Category 1.1.1",
                        "children": [
                            {
                                "name": "Category 1.1.1.1"
                            },
                            {
                                "name": "Category 1.1.1.2"
                            },
                            {
                                "name": "Category 1.1.1.3"
                            }
                        ]
                    },
                    {
                        "name": "Category 1.1.2",
                        "children": [
                            {
                                "name": "Category 1.1.2.1"
                            },
                            {
                                "name": "Category 1.1.2.2"
                            },
                            {
                                "name": "Category 1.1.2.3"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Category 1.2",
                "children": [
                    {
                        "name": "Category 1.2.1"
                    },
                    {
                        "name": "Category 1.2.2",
                        "children": [
                            {
                                "name": "Category 1.2.2.1"
                            },
                            {
                                "name": "Category 1.2.2.2"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    def test(self):
        res = self.client.post('/categories/', self.test_input_data, format='json')
        self.assertEqual(res.status_code, 201)

        res = self.client.get('/categories/2/')
        self.assertEqual(res.json(), {
            "id": 2,
            "name": "Category 1.1",
            "children": [
                {
                    "id": 3,
                    "name": "Category 1.1.1"
                },
                {
                    "id": 7,
                    "name": "Category 1.1.2"
                }
            ],
            "parents": [
                {
                    "id": 1,
                    "name": "Category 1"
                }
            ],
            "siblings": [
                {
                    "id": 11,
                    "name": "Category 1.2"
                }
            ]
        })
