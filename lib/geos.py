def area_of_disk(radius):


    return radius * 3.14  ** 2

# print()
def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)
