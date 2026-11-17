**Objective:** Retrieve the flag stored in a DNS record, and submit it.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. The host `10.0.0.2` is a DNS server. The flag is stored in the TXT record for the name `flag.lab.test`.
3. Query that TXT record from the DNS server at `10.0.0.2` and read the flag.
