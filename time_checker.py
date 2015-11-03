import libs.requests as requests

sites = [
    ['http://github.com',0.02,10.02],
    ['http://google.com',20,2]
]
for site in sites:
    try:
        r = requests.get(site[0], timeout=(site[1],site[2]))

        print site[0] + " in " + str(r.elapsed)
    except requests.exceptions.RequestException as e:
        print(e.message)
        pass