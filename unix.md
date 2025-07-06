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

## Mega

To synchronize directories with Mega.io, there are several options :

1. [Megasync aka Mega Desktop app](https://mega.io/syncing). This is a GUI. The issue is that the app loses the sync of the directories you want to sync between reboots, so you have to waste time syncing at each run.
2. [MegaCMD](https://mega.io/cmd#download) or `apt install megacmd` which is a bunch of CLI commands. The sync is saved between reboots in `~/.megaCmd`


- To add a new directory to sync: `mega-sync localdir remotemegadir`
- View current status: `mega-sync`. Sync means it's scanning directories. Pending means transfers are potentially happening.
- View current transfers: `mega-transfers`
- Switch debug level: `mega-log -sc info` sets command and SDK level to info

