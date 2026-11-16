import json

def load_ytd(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # Strip the JavaScript assignment: "window.YTD.block.part0 = "
    start = text.index('=') + 1
    return json.loads(text[start:].strip())

dms = load_ytd("C:/Users/Kaushal/Desktop/coding-cafe/twitter-archive-class/twitter-archive-class/data/direct-messages.js")
following = load_ytd("C:/Users/Kaushal/Desktop/coding-cafe/twitter-archive-class/twitter-archive-class/data/following.js")
followers = load_ytd("C:/Users/Kaushal/Desktop/coding-cafe/twitter-archive-class/twitter-archive-class/data/follower.js")

print(len(dms), len(following), len(followers))

print(dms[0].keys())
print(dms[0]["dmConversation"].keys())
print(following[0])
print(followers[0])

target = "988531805904097284"

matches = []
for item in dms:
    conv = item["dmConversation"]
    cid = conv["conversationId"]
    if target in cid.split("-"):
        matches.append(conv)

print(len(matches))
for conv in matches:
    print(conv["conversationId"], len(conv["messages"]))

messages = []
skipped = 0
for conv in matches:
    for m in conv["messages"]:
        try:
            messages.append(m["messageCreate"])
        except KeyError:
            skipped += 1      # e.g. other event types that aren't real messages

print(len(messages), skipped)

print(len(messages))    

sent_by_owner = 0
sent_by_target = 0
for m in messages:
    if m["senderId"] == target:
        sent_by_target += 1
    else:
        sent_by_owner += 1

print(sent_by_owner, sent_by_target)
print(sent_by_owner + sent_by_target == len(messages))   # should be True

following_ids = set()
for item in following:
    following_ids.add(item["following"]["accountId"])

follower_ids = set()
for item in followers:
    follower_ids.add(item["follower"]["accountId"])

owner_follows = target in following_ids
they_follow = target in follower_ids
print(owner_follows, they_follow)
print(owner_follows and they_follow)