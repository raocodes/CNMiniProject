import pyshark


def createpacketinfo():
    cap = pyshark.FileCapture(
        'testfiles/200722_win_scale_examples_anon.pcapng', display_filter='tcp')

    packetinfo = []

    count = 1
    for packet in cap:
        currflag = list()
        tcpflags = {
            'FIN': packet['tcp'].flags_fin,
            'SYN': packet['tcp'].flags_syn,
            'RST': packet['tcp'].flags_reset,
            'PSH': packet['tcp'].flags_push,
            'ACK': packet['tcp'].flags_ack,
            'URG': packet['tcp'].flags_urg
        }

        src = packet['ip'].src
        dst = packet['ip'].dst
        ack = packet['tcp'].ack
        seq = packet['tcp'].seq

        for key, value in tcpflags.items():
            if value == '1':
                currflag.append(key)

        packetinfo.append(
            {'count': count, 'flags': currflag, 'src': src, 'dst': dst, 'ack': ack, 'seq': seq})
        count = count + 1

    return packetinfo


if __name__ == '__main__':
    for packet in createpacketinfo():
        print(packet)
