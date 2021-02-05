#!/usr/bin/python

my_token = 'blah-blah-blah'

def list_my_deposits_files(sandbox=False):
    from zenodolib import ZenodoHandler
    print("TOKEN USED: " + str(my_token))
    api = ZenodoHandler(access_token=my_token, proxies={}, test=sandbox)
    r_list = api.deposition_list()
    result = r_list.json()
    # print(result)
    for record in result:
        print('{}: "{}" [{}]'.format(record['doi'], record['metadata']['title'],
                              record['metadata']['access_right']))
        for file in record['files']:
            print(" - ",file["filename"])
    return

list_my_deposits_files(sandbox=True)
