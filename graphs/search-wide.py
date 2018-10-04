# Search wide in graph
# Asymptotic complexity (O) = V + E, where V - count vertex, E - count edges
from collections import deque


def search(name, work):
    """
    :type name: str
    :type work: str
    :rtype None
    """
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        people = search_queue.popleft()
        if not people['name'] in searched:
            if check_work(people, work):
                print(people['name'].upper() + ' is ' + work + '!')
                return True
            else:
                search_queue += graph[people['name']]
                searched.append(people['name'])

    return False


def check_work(people, work):
    """
    :type people: dict
    :type work: str
    :rtype bool
    """
    return people['work'] == work


peoples = {
    1: {'name': 'oleg', 'work': 'soldier'},
    2: {'name': 'boris', 'work': 'writer'},
    3: {'name': 'lena', 'work': 'operator'},
    4: {'name': 'ana', 'work': 'freelancer'},
    5: {'name': 'alex', 'work': 'scenarist'},
    6: {'name': 'bob', 'work': 'actor'},
    7: {'name': 'pasha', 'work': 'seller'}
}

graph = {
    'start': [peoples[1], peoples[3], peoples[7]],
    peoples[1]['name']:  [peoples[2], peoples[4]],
    peoples[3]['name']:  [peoples[5]],
    peoples[7]['name']:  [peoples[5], peoples[6]],
    peoples[2]['name']: [],
    peoples[4]['name']: [],
    peoples[5]['name']: [],
    peoples[6]['name']: [],
}

search('start', 'freelancer')
