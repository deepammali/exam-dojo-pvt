**Objective:** Capture the flag from traffic between two other hosts.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. Once every second, the host `10.0.0.2` sends the flag to the host `10.0.0.3` on UDP port `5309`.
3. That traffic is not addressed to you, and the network will not deliver it to you on its own. Get the flag on `10.0.0.1`.
