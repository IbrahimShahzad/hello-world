# DECODING PACKET LAYERS

- We can take the raw packet and essentially try to cast it to known formats. 
  - It is compatible with different layers so we can access ethernet, IP, and TCP layers easily. 
  - The layers package is something new in the Go library that is not available in the underlying pcap library. 
  - This is an incredibly useful package that is part of the gopacket library. 
  - It allows us to easily identify if a packet contains a specific type of layer. 
  - This code example will show how to use the layers package to see if the packet is ethernet, IP, and TCP and to access the elements in those headers easily.

- Finding the payload depends on all the layers involved. 
  - Each protocol is different and has to be calculated accordingly. 
  - This is where the power of the layers package comes in to play. 
  - The authors of gopacket took the time to create types for many known layers like ethernet, IP, UDP and TCP. 
  - The payload is part of the application layer. 