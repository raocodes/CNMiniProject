from createpacketinfo import createpacketinfo


def printallpacketinfo():
    data = createpacketinfo()

    for packet in data:
        print(f"Packet {packet['count']}: {packet['flags']}")
        print(f"src: {packet['src']}")
        print(f"dst: {packet['dst']}")
        print()


if __name__ == '__main__':
    printallpacketinfo()
