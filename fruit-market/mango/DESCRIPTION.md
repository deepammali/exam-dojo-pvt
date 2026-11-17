**Objective:** Stop incoming traffic to a port so that the flag is printed.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. A service on `10.0.0.1` listens on TCP port `6081`. The host `10.0.0.2` connects to it every second.
3. Make sure no traffic from the network reaches TCP port `6081` on `10.0.0.1`. Once the service sees no connection for about 2 seconds, the flag is printed in this terminal.

**Rules:** Do not stop, kill, or change the service listening on port `6081`. The block must be applied on `10.0.0.1`.
