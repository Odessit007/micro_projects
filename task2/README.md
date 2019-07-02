Current assumptions:
* there is files.txt
* all the files in the dataset are listed in files.txt
* all the files listed in files.txt are part of the dataset
* dataset's server is available and connection is fine

If any of these assumptions could be false then exception 
handling should be added.

* * *

Possible future enhancements:
* It might be faster or at least more memory efficient (no need to keep 
all Counters) to use multiprocessing.Manager().dict() instead of 
collections.Counter
* It might be more memory efficient to somehow rewrite the multiprocess part
 with imap (it's lazy)
