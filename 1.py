synonyms=[]
antonyms = []

synsets = wordnet.synsets('courage')

for s in synsets:
    lemmas = s.lemmas()
    for l in lemmas:
    synonyms.append(l.name())
    maybe_antonyms = l.antonyms()
    if maybe_antonyms:
        antonyms.append(maybe_antonyms[0].name)

print("synonyms")
print(set(synonyms))
print("antonyms")
print(set(antonyms))
