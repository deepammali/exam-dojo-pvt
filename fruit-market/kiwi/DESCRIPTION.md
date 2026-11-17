**Objective:** Receive the flag over the network and submit it.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. The host `10.0.0.2` tries, once every second, to open a TCP connection to `10.0.0.1` on port `4417`. When a connection succeeds, it sends the flag over it.
3. Receive the flag on `10.0.0.1`.
