import json

def load_ytd(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # Strip the JavaScript assignment: "window.YTD.block.part0 = "
    start = text.index('=') + 1
    return json.loads(text[start:].strip())

tweets = load_ytd(r"C:/Users/Kaushal/Desktop/coding-cafe/twitter-archive-class/twitter-archive-class/data/tweets.js")
print(type(tweets), len(tweets))
print(tweets[0].keys())   

print(type(tweets), len(tweets))
first = tweets[0]["tweet"]
print(first.keys())

years = set()
for item in tweets:
    years.add(item["tweet"]["created_at"].split()[5])
print(sorted(years))

july = []
for item in tweets:
    t = item["tweet"]
    parts = t["created_at"].split()
    if parts[1] == "Jul" and parts[5] == "2020":
        july.append(t)

print(len(july))

rt_count = 0
for t in july:
    if t["full_text"].startswith("RT @"):
        rt_count += 1
print(rt_count)

day_counts = {}
for t in july:
    day = t["created_at"].split()[2]      # e.g. '15'
    if day in day_counts:
        day_counts[day] += 1
    else:
        day_counts[day] = 1

best_day = None
best_count = 0
for day in day_counts:
    if day_counts[day] > best_count:
        best_count = day_counts[day]
        best_day = day

print(best_day, best_count)

print(len(day_counts))                     # at most 31
print(sum(day_counts.values()) == len(july))   # should print True
# parts = first["created_at"].split()
# print(parts)
# # ['Wed', 'Jul', '15', '12:34:56', '+0000', '2020']

# july = []
# for item in tweets:
#     t = item["tweet"]
#     parts = t["created_at"].split()
#     if parts[1] == "Jul" and parts[5] == "2020":
#         july.append(t)