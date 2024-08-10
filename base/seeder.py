from .models import Type


def seeder_func():
    types = ['Clothing', 'Books', 'Ceramics', 'Art', 'Jewellery', 'Bags']

    for type in types:
        if not Type.objects.filter(name=type):
            new_type = Type(name=type)
            new_type.save()


