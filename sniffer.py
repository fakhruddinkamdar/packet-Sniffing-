from scapy.all import sniff, wrpcap

# Capture 50 packets from the default interface
packets = sniff(count=50)

# Save them to a .pcap file in correct format
wrpcap("captured_packets.pcap", packets)

print("✅ Packets saved to captured_packets.pcap")
