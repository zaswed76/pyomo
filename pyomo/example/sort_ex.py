
words = ["a", "b", "c"]
rat = [3, 2, 1]
ac = []
for w, r in zip(words, rat):
    ac.append((w, r))

print(sorted(ac, key=lambda w: w[1], reverse=True))


