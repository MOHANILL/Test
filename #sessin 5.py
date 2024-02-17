#sessin 5
dict_={"country":"Iran", "age":23, "name":"Mohan"}
print(dict_)
dict_.update({"country":"America"})
print(dict_)
dict_["age"]=21
print(dict_)
##
dict_.pop("country")
print(dict_)
dict_.popitem()
print(dict_)
dict_["car price"]=20000000000000
print(dict_)
del dict_["car price"]
print(dict_)
##
dict1={"brand": "Ford","model": "Mustang","year": 1964}
dict2=dict(dict1)
print(dict2)
dict3=dict1.copy()
print(dict3)