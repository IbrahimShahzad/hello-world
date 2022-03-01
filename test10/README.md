# DECODING LAYERS FASTER

- If we know what layers to expect, we can use existing structures to store the packet information instead of creating new structs for every packet which takes time and memory. 
- It is faster to use DecodingLayerParser. 
- It is like marshalling and unmarshalling data. 