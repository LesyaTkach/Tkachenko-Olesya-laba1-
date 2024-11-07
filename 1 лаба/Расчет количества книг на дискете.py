# TODO Найдите количество книг, которое можно разместить на дискете
capacity = 1.44
pages = 100
lines = 50
items = 25
bites = 4
booksize = pages * lines * items * bites
capacityinbites = capacity * 1024 * 1024
books = int(capacityinbites // booksize)
print("Количество книг, помещающихся на дискету:", books)
