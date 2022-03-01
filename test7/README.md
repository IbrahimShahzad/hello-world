# CREATING AND SENDING PACKETS

- This example does a couple things. 
  - First it will show how to use the network device to send raw bytes. 
  - In that way, you can use it almost like a serial connection to send data. 
  - That's useful for really low level data transfer, but if you want to interact with an application you probably want to build a packet that other hard and software can recognize.

- The next thing it does is show how to create a a packet with the ethernet, IP, and TCP layers. 
  - Everything is default and empty though so it doesn't really do anything.

- To finish it off we create another packet but actually fill in some MAC addresses for the ethernet layer, some IP addresses for IPv4, and port numbers for the TCP layer. 
  - You should see how you can forge packets and impersonate devices with that.

- The TCP layer struct has boolean SYN, FIN, and ACK flags that can be read or set. 
  - That is good for manipulating and fuzzing TCP handshakes, sessions, and port scanning.

- The pcap library provides an easy way to send bytes, but the layers package in gopacket assists us in creating the byte structure for the many layers.