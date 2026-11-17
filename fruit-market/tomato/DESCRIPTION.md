**Objective:** Get the flag from a web server that only gives it to the admin.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. A web server runs at `http://10.0.0.2`. `GET /flag` returns the flag only to a logged-in `admin` session. Anyone else gets `403`.
3. A client on your host (`10.0.0.1`) is logged in to that server as `admin` and keeps talking to it over HTTP.
4. You do not know the admin password. Get the flag from `http://10.0.0.2/flag`.

Run every command for this challenge from the `10.0.0.1` terminal.
