<h1><strong>Day 5 Dictionaries (Hash Maps)</strong></h1>
<h3><strong>Theory: Hash Tables</strong></h3>
<p>A Dictionary is a Key-Value store. It is optimized for O(1) Lookup. When you search a List, Python scans left-to-right (O(N)). When you search a Dictionary, Python uses a "Hash Function" to calculate exactly where the data is in memory. It is instant, even with 1 million items.
</p>
''''bash
user = {"id" : 1, "name" : "Admin"}
# Safe Access (.get) 
# Returns None if key missing, prevents crash 
email = user.get("email","No Email Found")

# Iteration
for key, val in user.items(): 
    print (f"{key}: {val}") 

''''

    
<h3><strong> Goals: </strong></h3>
<p>
1.List Search (O(N)): Python must scan one element at a time from start to end. Dict/Set Search (O(1)): Python use hash table, gets a memory address, and looks only at that spot. No need for scanning.</p>
<p>
2.Direct access user ["key"] raises a KeyError if the key is missing, crashing the script. The method user.get("key", "Default") checks the Hash Table. If the bucket is empty. </p>
<p>
3.Create a dictionary that counts the frequency of each letter.
</p>
<p>
4.Marge teo dictionary using the update operator | or .update()
</p>
