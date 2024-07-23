data = {
    "aalu" : 30,
    "gaajar" : 67,
    0 : "karayla",
    1 : "teenda",
}

# print(data.items())
# print(data.values())
# print(data.keys())
# print(data.get("aalu"))
# print(data["aalu"])
# data.update({2:"kheera"})
# print(data)
data.pop("gaajar")
print(data)
data.popitem()
print(data)