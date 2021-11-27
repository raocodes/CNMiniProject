import pyshark
cap = pyshark.FileCapture(
    '200722_win_scale_examples_anon.pcapng', display_filter='tcp')

# Flag wise
# Packet wise - Flag - Source - Dest - ACK - SYN

count = 1
for packet in cap:
    # print(packet)
    # for things in dir(packet['tcp']):
    #     if 'flag' in things:
    #         print(things)

    currflag = list()
    tcpflags = {
        'FIN': packet['tcp'].flags_fin,
        'SYN': packet['tcp'].flags_syn,
        'RST': packet['tcp'].flags_reset,
        'PSH': packet['tcp'].flags_push,
        'ACK': packet['tcp'].flags_ack,
        'URG': packet['tcp'].flags_urg
    }

    # print(tcpflags.items())

    for key, value in tcpflags.items():
        if value == '1':
            currflag.append(key)

    print(f'Packet {count}: {currflag}')
    count = count + 1
