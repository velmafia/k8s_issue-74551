#!/usr/bin/env python3

import urllib.request

URL="http://localhost:8080/files/512KiB.base64"

### download completed
handler = urllib.request.urlopen(URL)
# download part of file
handler.read(4096)
# download rest of file
handler.read()
handler.close()
print("first download complete")

### Every cancel durring downloading trigger "broken-pipe" log
### if canceled a few times, then "Timeout occured"
for i in range(10):
    handler = urllib.request.urlopen(URL)
    # download part of file
    handler.read(4096)
    # cancel downloading
    handler.close()
    print(f"cancel of {i} downloading completed")

### This will never executed
handler = urllib.request.urlopen(URL)
handler.read()
handler.close()
print("last downloads hangs")
