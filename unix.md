# Unix / Linux

## Fail2ban

`sudo fail2ban-client start`


### Status

- Status of fail2ban service: `sudo systemctl status fail2ban`
- Status of fail2ban: `sudo fail2ban-client status sshd`

### Banned IP addresses

To manually ban an IP address:

`sudo fail2ban-client -vvv set JAIL banip IPADDR`

where:

- `JAIL` is the name of the jail to  use (get list with `sudo fail2ban-client status`)
- `IPADDR` is the IP address to ban


- List banned IP addressed: `sudo zgrep 'Ban' /var/log/fail2ban.log*` or `sudo fail2ban-client banned`

- Get banned IP with time: `sudo fail2ban-client get sshd banip --with-time`
