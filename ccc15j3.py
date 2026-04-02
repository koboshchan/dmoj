tran={
    "a":"a","b":"bac","c":"cad","d":"def","e":"e",
    "f":"feg", "g":"geh","h":"hij","i":"i","j":"jik","k":"kil","l":"lim",
    "m":"mon","n":"nop","o":"o","p":"poq","q":"qor","r":"ros","s":"sut",
    "t":"tuv","u":"u","v":"vuw","w":"wux","x":"xuy","y":"yuz","z":"zuz"
}
letters,out=input(),""
for letter in letters:out+=tran[letter]
print(out)