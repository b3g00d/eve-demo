MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'eve_admin'
MONGO_PASSWORD = 'eve_admin'
MONGO_DBNAME = 'eve_demo'


speakers = {
    'item_title': 'speaker',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },
    'schema': {
        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10
        },
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'blogs': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'blogs',
                    'field': '_id',
                    'embeddable': True,
                }
            },
        }
    }
}

blogs = {
    'item_title': 'blog',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10
        },
        'content': {
            'type': 'string',
            'minlength': 1,
        }
    }
}
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH']

DOMAIN = {'speakers': speakers, 'blogs': blogs}
