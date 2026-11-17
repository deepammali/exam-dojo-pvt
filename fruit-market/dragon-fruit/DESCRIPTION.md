**Objective:** Capture the flag from traffic between two other hosts.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. Once every second, the host `10.0.0.2` opens a TCP connection to `10.0.0.3` on port `5309` and sends the flag.
3. That traffic is not addressed to you. Get the flag on `10.0.0.1`.
