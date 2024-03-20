import keyword
from django.db.models import Q
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query)<=5:
        return Products.objects.filter(id=int(query))
    keyword=[word for word in query.split() if len(word)>2]
    q_object=Q()
    for tokn in keyword:
        q_object |=Q(description__icontains=tokn)
        q_object |=Q(name__icontains=tokn)

    return Products.objects.filter(q_object)