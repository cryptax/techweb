# Unix / Linux

## Fail2ban

`sudo fail2ban-client start`

To manually ban an IP address:

`sudo fail2ban-client -vvv set JAIL banip IPADDR`

where:

- `JAIL` is the name of the jail to  use (get list with `sudo fail2ban-client status`)
- `IPADDR` is the IP address to ban
