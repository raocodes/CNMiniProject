def printallpacketinfo(data):
    for packet in data:
        print(f"Packet {packet['count']}: {packet['flags']}")
        print(f"src: {packet['src']}")
        print(f"dst: {packet['dst']}")
        print()
