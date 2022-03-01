# Open PCAP file

- Instead of opening a device for live capture we can also open a pcap file for inspection offline. 

- You can use tcpdump to create a test file to use.

```sh
# Capture packets to test.pcap file
sudo tcpdump -w test.pcap
```

- Then open the file and go through the packets with this code.

