# DATA WRANGLERS
a collection of parsers converting raw data into csv


#### intel_gpu_top.py
```
Freq MHz      IRQ RC6 Power     IMC MiB/s           RCS/0           BCS/0           VCS/0          VECS/0
 req  act       /s   %     W     rd     wr       %  se  wa       %  se  wa       %  se  wa       %  se  wa
   0    0        0   0  0.00    170     48    0.00   0   0    0.00   0   0    0.00   0   0    0.00   0   0
   6    6       12  99  0.01    545    134    0.81   0   0    0.00   0   0    0.00   0   0    0.00   0   0
   9    9       14  98  0.01    411     78    1.14   0   0    0.00   0   0    0.00   0   0    0.00   0   0
   5    5       10  99  0.01    436     74    0.72   0   0    0.00   0   0    0.00   0   0    0.00   0   0
  12   12       21  98  0.01    431    100    0.76   0   0    0.00   0   0    0.00   0   0    0.00   0   0
   3    3        8 100  0.00    391     52    0.16   0   0    0.00   0   0    0.00   0   0    0.00   0   0
```


#### webrtc2csv.py
```
   },
    "CIT01_111_minptime=10;useinbandfec=1-mimeType": {
     "values": "[\"audio/opus\",\"audio/opus\",\"audio/opus\",\"audio/opus\"]"
     
    "IA5506-[jitterBufferDelay/jitterBufferEmittedCount_in_ms]": {
     "values": "[16.764705882351517,25.454545454549866,25.454545454538838,80.00000000000807]"
   }
```
```
CIT01_111_minptime=10;useinbandfec=1-mimeType,audio/opus
IA5506-[jitterBufferDelay/jitterBufferEmittedCount_in_ms],16.8,25.5,25.5,80.0
```
