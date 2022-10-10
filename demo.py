# some_variable = "1"
# Print(some_variable + str(1))


# def add(rval, lval):
# return rval + lval


# print(add(int('1'), 1))

from datetime import date
dictionary = {}
dictionary['type'] = 'home inventory'
dictionary['date'] = date.today().isoformat()
dictionary['items'] = []

dictionary['items'].append({'item': 'MacBook Pro', 'count': 2})

dictionary['items'][0]

dictionary['items'].append({'item': 'car', 'count': 1})
dictionary['items'].extend([{'item': 'truck', 'count': 1}])
print(dictionary)
print('items in list:' + str(len(dictionary['items'])))


total = 0
for item in dictionary['items']:
    total += item['count']
 print('grand total of items: ' + str(total))
# print(dictionary['items'][0:2])
