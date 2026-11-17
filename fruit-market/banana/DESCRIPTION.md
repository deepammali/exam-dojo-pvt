**Objective:** Read the contents of `/flag` and submit it.

1. Run `/challenge/run`. It installs a copy of a file-reading program with the SETUID bit set so that the program runs as `root`. The challenge prints the exact path where it was installed.
2. `/flag` is readable only by `root`. Run that installed program to read `/flag`.

HINT: Can same program have multiple binaries? (like cat has 9 lives)
