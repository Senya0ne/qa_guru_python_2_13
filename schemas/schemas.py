from voluptuous import Schema, PREVENT_EXTRA

get_single_user = Schema(
    {'data': {'id': int,
              'email': str,
              'first_name': str,
              'last_name': str,
              'avatar': str},
     'support': {'url': str,
                 'text': str}}, required=True, extra=PREVENT_EXTRA)

post_create_user = Schema({'name': str,
                           'job': str,
                           'id': str,
                           'createdAt': str},
                          required=True, extra=PREVENT_EXTRA)

update_user = Schema({'name': str,
                      'job': str,
                      'id': str,
                      'updatedAt': str},
                     required=True, extra=PREVENT_EXTRA)
