def printallpacketinfo(data):
    for packet in data:
        message = {
            'SYN': f"Connection request from {packet['src']} to {packet['dst']}",
            'SYNACK': 'Connection request accepted from source and connection request from destination sent',
            'PSH': 'Indicates that packet needs to be pushed up to application layer immediately in destination',
            'URG': 'Informs the transport layer of the receiving end that the data is urgent and it should be prioritized',
            'FIN': 'Connection closed from the sender side',
            'ACK': f"Acknowledges that message till {packet['ack'] - 1} is received, expecting {packet['ack']}"
        }

        if 'SYN' in packet['flags'] and 'ACK' in packet['flags']:
            relevance = message['SYNACK']
        elif 'PSH' in packet['flags'] and 'ACK' in packet['flags']:
            relevance = message['PSH'] + ' and ' + message['ACK'].lower()
        elif 'URG' in packet['flags'] and 'ACK' in packet['flags']:
            relevance = message['URG'] + ' and ' + message['ACK'].lower()
        else:
            relevance = message[packet['flags'][0]]

        print(f"Packet {packet['count']}: {packet['flags']}")
        print(f"src: {packet['src']}")
        print(f"dst: {packet['dst']}")
        print(f"ack: {packet['ack']}")
        print(f"seq: {packet['seq']}")
        print(f"Flag relevance: {relevance}")
        print()

def printflaginfo(data, flag):
    for packet in data:
        # message = {
        #     'SYN': f"Connection request from {packet['src']} to {packet['dst']}",
        #     'SYNACK': 'Connection request accepted from source and connection request from destination sent',
        #     'PSH': 'Indicates that packet needs to be pushed up to application layer immediately in destination',
        #     'URG': 'Informs the transport layer of the receiving end that the data is urgent and it should be prioritized',
        #     'FIN': 'Connection closed from the sender side',
        #     'ACK': f"Acknowledges that message till {packet['ack'] - 1} is received, expecting {packet['ack']}"
        # }

        # if 'SYN' in packet['flags'] and 'ACK' in packet['flags']:
        #     relevance = message['SYNACK']
        # elif 'PSH' in packet['flags'] and 'ACK' in packet['flags']:
        #     relevance = message['PSH'] + ' and ' + message['ACK'].lower()
        # elif 'URG' in packet['flags'] and 'ACK' in packet['flags']:
        #     relevance = message['URG'] + ' and ' + message['ACK'].lower()
        # else:
        #     relevance = message[packet['flags'][0]]

        # print(f"Packet {packet['count']}: {packet['flags']}")
        # print(f"src: {packet['src']}")
        # print(f"dst: {packet['dst']}")
        # print(f"ack: {packet['ack']}")
        # print(f"seq: {packet['seq']}")
        # print(f"Flag relevance: {relevance}")
        # print()
        print(packet['flags'])
