import re
from operator import itemgetter

f = open("input.txt", "r")
rooms = f.read().split("\n")
sectorSum = 0
for room in rooms:
    roomNameParts = re.findall(r"\w+", room)

    roomName = "".join(roomNameParts[:-2])
    sector = roomNameParts[-2:-1][0]
    checksum = roomNameParts[-1:][0]

    lookup = {}

    for ch in roomName:
        if ch not in lookup:
            lookup[ch] = {'char': ch, 'value': 1}
        else:
            lookup[ch]['value'] += 1

    sortedChars = sorted(lookup.values(), key=lambda x: (-x['value'], ord(x['char'])))
    checksumCheck = ""
    for ch in sortedChars[:5]:
        checksumCheck += ch['char']

    if checksumCheck == checksum:
        sectorSum += int(sector)

print sectorSum








