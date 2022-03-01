## Before Starting

Make sure you have the following pre-requisites:
```bash
# Get the gopacket package from GitHub
go get github.com/google/gopacket
# Pcap dev headers might be necessary
sudo apt-get install libpcap-dev
```
## Topics

|Sr|Topic                             |Readme                               |
|:-|:---------------------------------|:------------------------------------|
|1 |Find devices                      |[test1/README.md](test1/README.md)   | 
|2 |Open Device for Live Capture      |[test2/README.md](test2/README.md)   |
|3 |Write Pcap File                   |[test3/README.md](test3/README.md)   |
|4 |Open Pcap File                    |[test4/README.md](test4/README.md)   |
|5 |Setting Filters                   |[test5/README.md](test5/README.md)   |
|6 |Decoding Packet Layers            |[test6/README.md](test6/README.md)   |
|7 |Creating and Sending Packets      |[test7/README.md](test7/README.md)   |
|8 |More on Creating/Decoding Packets |[test8/README.md](test8/README.md)   |
|9 |Custom Layers                     |[test9/README.md](test9/README.md)   |
|10|Decoding Packets Faster           |[test10/README.md](test10/README.md) |
|11|TCP Stream Reassembly             |Check gopacket Documentation         |


References: 
- [gopacket github](https://github.com/google/gopacket)
- [Blog](https://www.devdungeon.com/content/packet-capture-injection-and-analysis-gopacket)
- [youtube-gophercon](https://www.youtube.com/watch?v=APDnbmTKjgM)