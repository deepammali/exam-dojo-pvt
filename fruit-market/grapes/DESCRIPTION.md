**Objective:** Find a hidden host and get the flag from it.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. The network is `10.0.0.0/16`. Exactly one other host is on it, at an address you are not told.
3. That host runs a TCP service on port `2785`. It sends the flag to anyone who connects.
4. Find the host's IP address, connect to the service, and get the flag.
