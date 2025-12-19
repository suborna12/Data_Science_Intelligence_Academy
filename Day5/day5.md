<h1><strong>Day 5 Dictionaries (Hash Maps)</strong></h1>
<h3><strong>Theory: Hash Tables</strong></h3>
<p>A Dictionary is a Key-Value store. It is optimized for O(1) Lookup. When you search a List, Python scans left-to-right (O(N)). When you search a Dictionary, Python uses a "Hash Function" to calculate exactly where the data is in memory. It is instant, even with 1 million items.
</p>

```
user = {"id" : 1, "name" : "Admin"}
# Safe Access (.get) 
# Returns None if key missing, prevents crash 
email = user.get("email","No Email Found")

#Iteration
for key, val in user.items(): 
    print (f"{key}: {val}") 
