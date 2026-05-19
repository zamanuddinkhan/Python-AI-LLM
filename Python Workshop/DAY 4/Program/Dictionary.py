mydict={"name": "Raj", "age":20, "city": "Indore"}
print(mydict.get("name"))
print(mydict.keys())#in tuple format
print(mydict.values())#in tuple format
print(mydict.items())#in tuple format
print(mydict.update({"post":"Developer"}))
print(mydict)
print(mydict.fromkeys(["a","b"],0))
data=print(mydict.pop("age"))
print(data)