

products=["Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor"]

# print(products[1])
# print(products[-1])
products.append("cpu")
products.append("screen")
# print(products)

sample_products=("apple", 35,"fruits")

# print(type(sample_products))

sample_list=list(sample_products)
# print(type(sample_list))

sample_list[1]=55
# print(sample_list)
# print(type(sample_list))

sample_tuple=tuple(sample_list)
# print(type(sample_tuple))


categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics"
]

categories_set=set(categories)
# print(categories_set)

categories_set.add("apple")
# print(categories_set)

categories_set.add("Electronics")
# print(categories_set)

store="apple" in categories_set
# print(store)

unique_element=len(categories_set)
# print(unique_element)