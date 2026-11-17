**Objective:** Read the contents of `/flag` and submit it.

1. Run `/challenge/run`. It sets the SETUID bit on one program already installed on this system. It is a program that helps to read files
2. `/flag` stays readable only by `root`. Read it as the `hacker` user.
