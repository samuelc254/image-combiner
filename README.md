# image-combiner
A simple python script to combine every possible image from source folder
  
<img src="out/16.png">
  
## How to use
It makes every combination of up to four image groups, so in the out you'll get each image with a feature from each group.

```
image-combiner
│   image combiner.py
│
└───src
│   │
│   └───background
│   │   │   file1.png
│   │   │   file2.png
│   │
│   └───sky
│   │   │   file1.png
│   │   │   file2.png
│   │
│   └───character
│   │   │   file1.png
│   │   │   file2.png
│   │
│   └───miscellaneous
│   │   │   file1.png
│   │   │   file2.png
│   
│   
└───out
    │   1.png
    │   2.png
    |   ...
    |   16.png
```