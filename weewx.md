# Weewx

## Install

- Use the [Debian package](http://www.weewx.com/docs/usersguide.htm)
- To upgrade, see [doc](http://www.weewx.com/docs/upgrading.htm#Upgrading_using_setup.py) 

By default, the configuration file will be located in `/etc/weewx/weewx.conf`

The root path of weewx, `WEEWX_ROOT`, is essential, because this is where the rest of the configuration will be done.
```
# Root directory of the weewx data file hierarchy for this station.
WEEWX_ROOT = /home/weewx/
```

To test your configuration and generate debug information: 

```
debug = 1
```

## Upgrade

Import the key:
```
curl -sSf 'https://weewx.com/keys.html' | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/weewx.gpg --yes
```

In `/etc/apt/sources.list.d/weewx.list`:

```
deb [arch=all] http://weewx.com/apt/python3 buster main
```

## Configuration


### Initial Station setup

In `weewx.conf`, you'll want to setup in the `[Station]` section:

- location: description of the station location, like the name of your town
- coordinates of your station: `latitude = 41.1`, `longitude = 7.07611`
- `altitude = 100, meter # Choose 'foot' or 'meter' for unit`

The location, latitude, longitude, altitude will then be available in HTML templates as `$station.location, $station.latitude, $station.longitude and $station.altitude`.

- `station_url = http://www.example.com` to specify the beginning of the weather station's website.
Specify the URL for your weather station's website:

- `stationc_type = xxx`: this is an important parameter where you specify the **driver** for your weather station. E.g WMR200, or Interceptor. Your `weewx.conf` will then have a dedicated section for that driver.


To use **Metric** units:

```
[StdConvert]
    target_unit = METRIC    # Options are 'US', 'METRICWX', or 'METRIC'
```

To specify units to use for given labels, do that in `weewx.conf` `Unit` section. Do not do it in the skins (unless you have a reason to).

```
[Units]
    # This section is for managing the selection and formatting of units.
    
    [[Groups]]
    ...
    group_rain         = mm                 # Options are 'inch', 'cm', or '
mm'
    group_rainrate     = mm_per_hour        # Options are 'inch_per_hour', '
cm_per_hour', or 'mm_per_hour'
    group_speed        = km_per_hour        # Options are 'mile_per_hour', '
```

For time format, see ` [[TimeFormats]]`




### WMR200 stations

WMR200 weather stations are no longer natively supported. Their support has been shifted to [an extension)(https://github.com/weewx/weewx-wmr200). Follow installation of this extension [here](https://github.com/weewx/weewx-wmr200)

Basically, you'll get additional extension files, and then you'll need to add a `[WMR200]` section to `weewx.conf`:

```
[WMR200]
    # This section is for the Oregon Scientific WMR200
    
    # The station model, e.g., WMR200, WMR200A, Radio Shack W200
    model = WMR200
    
    # The driver to use:
    driver = user.wmr200

    archive_interval = 300

    loop_interval = 2.5
    erase_archive = False
    sensor_status = True
    archive_threshold = 1512000
    archive_startup = 120
    user_pc_time = True

```

### EcoWitt stations



### Generating websites

Websites where you send weather data to are known as *reports*. 
You can set up several websites, choose what you want to send to each of those, have different templates etc.

In `weewx.conf`, you list all reports to generate in the `[StdReport]` section.
Each report is a sub-section. 
A report is configured from its *skin* directory (`SKIN_ROOT`).
When the report is generated, it is written to `HTML_ROOT`.

In the configuration below, we have 2 reports: Standard Report and External.

The standard report is defined in the default `WEEWX_ROOT/skins/Standard` (in particular by `skin.conf`), and the generated report will be generated in `WEEWX_ROOT/public_html`.

The external report is defined in `WEEWX_ROOT/skins/External` and is generated into `WEEWX_ROOT/external_html`. It uses bigger images.


```
[StdReport]
    # This section specifies what reports, using which skins, to generate.
    
    # Where the skins reside, relative to WEEWX_ROOT:
    SKIN_ROOT = skins
    
    # Where the generated reports should go, relative to WEEWX_ROOT:
    HTML_ROOT = public_html
    
    # Each subsection represents a report you wish to run:
    [[StandardReport]]
        
        # What skin this report should be based on:
        skin = Standard

    [[External]]
	skin = External
	HTML_ROOT = external_html
	[[[ImageGenerator]]]
	     image_width = 600
	     image_height = 360
```

### Uploading pages via FTP

Uploading generated pages and images can be done via FTP, and this is yet another 'special' report.

```
   [[FTP]]
        skin = Ftp
        
        # FTP'ing the results to a webserver is treated as just another report,
        # albeit one with an unusual report generator!
        #
        # If you wish to use FTP, uncomment and fill out the next four lines:
        #user = replace with your username
        #password = replace with your password
        #server = replace with your server name, e.g, www.threefools.org
        #path = replace with the destination directory (e.g., /weather)
        
        # If you wish to upload files from something other than what HTML_ROOT
        # is set to above, then reset it here:
        #HTML_ROOT = public_html
        
        # Most FTP servers use port 21, but if yours is different, you can
        # change it here
        port = 21
        
        # Set to 1 to use passive mode, zero for active mode:
        passive = 1
        
        # How many times to try to transfer a file before giving up:
        max_tries = 2

        # Set to True for a secure FTP (SFTP) connection. Not all servers
        # support this.
        secure_ftp = False
```

### Rsyncing directories

It is possible to *rsync* report directories from one host to another. For example, if you want to copy a weewx website to another host.

Typically, weewx daemon runs as root (unless this has been changed). *You must then ensure that root is able to SSH to the host to Rsync to with a public key* (see SSH authorized_keys and known_hosts).


```
  [[RSYNC]]
        skin = Rsync
        
        # rsync'ing the results to a webserver is treated as just another
        # report, much like the FTP report.
        #
        server = 192.168.0.9
		path = /home/weewx/public_html
        user = weewx
        
        # Rsync can be configured to remove files from the remote server if
        delete = 0
```	



### Sending information remotely to AWEKAS, CWOP etc

Information can be sent to external websites that use RESTful protocols.

```
[StdRESTful]
    # This section is for uploading data to sites using RESTful protocols.
    
    [[StationRegistry]]
        # To register this weather station, set this to True:
        register_this_station = False
```

[To register the station on Weewx](http://weewx.com/stations.html) (optional)

Also, if your weather station is not published on websites such as AWEKAS, CWOP, you can disable those services:

```
  [[AWEKAS]]
  enable = false
  ...
```

### Customized or Localized labels

```
  [[Generic]]
        # Generic labels, keyed by an observation type.
        barometer      = Barometre
        dewpoint       = Point de rosee
        heatindex      = Humidex
        inHumidity     = Humidite interieur
        inTemp         = Temperature interieure
        outHumidity    = Humidite exterieure
        outTemp        = Temperature exterieure
        radiation      = Radiation
        rain           = Precipitations
        rainRate       = Taux de precipitation
        rxCheckPercent = ISS Signal Quality
        windDir        = Direction du vent
        windGust       = Rafales
        windGustDir    = Direction rafales
        windSpeed      = Vitesse du vent
        windchill      = Temperature ressentie
        windgustvec    = Vecteur rafales
        windvec        = Vecteur vent
  ...
  [[Labels]]
  ...
        foot              = " pieds"
  ...

[Almanac]
    # The labels to be used for the phases of the moon:
    moon_phases = Nouvelle, Premier croissant, Premier quartier, Gibbeuse croissante, Pleine, Gibbeuse decroissante, Dernier quartier, Dernier croissant
```

### Humidex: computing it or getting it from the weather station?

Humidex can be read from the weather station if it provides it, or computed from temperature and humidty:

```
[StdWXCalculate]
    [[Calculations]]
	heatindex = prefer_hardware

```


### Skins (look of websites)

In `skin.conf`:

```
[Extras]
  radar_img = http://www.infoclimat.fr/api/AH4EMQcrAzhVYQQtVWdXNFw2BXhQOAEpDm0PZAc1AC8AYQIzVGcHNFFlVWIFNAdjAW9RM1EzBzNWNg5n/radar/sud_est?c6efb45b781de49d57c2c0aa20e8057c
  storm_img = http://www.meteorologic.net/map/radar/your_radar.php?lat=43.37
  radar_url = http://www.infoclimat.fr

```

In the skins, you'll also specify the HTML templates of files to generate. Those files should be located in the *same directory as the skin*.

```
   [[ToDate]]
        # Reports that show statistics "to date", such as day-to-date,
        # week-to-date, month-to-date, etc.
	[[[about]]]
	    template = about.html.tmpl

	[[[almanac]]]
	    template = almanac.html.tmpl
```

The templates understand a few conditions and loops:

```html
#if $day.UV.has_data
    <tr>
    <td>UV</td>
    <td>$current.UV</td>
    </tr>
#end if

#for $month in $year.months
  <tr>
    <td>$month.dateTime.format("%B")</td>
    <td>$month.outTemp.avg ($month.outTemp.min - $month.outTemp.max)</td>
    <td>$month.inTemp.avg ($month.inTemp.min - $month.inTemp.max)</td>
    <td>$month.rain.sum</td>
   </tr>
  </tr>
#end for

```

To display particular values, you can use variables such as:

- `$current.inTemp`
- `$day.outTemp.maxtime.format("%H:%M")`
- `$yesterday.inTemp.avg`
- `$span($hour_delta=24).rain.sum`
- `$month($months_ago=1).rain.sum`

To generate **charts** in a given skins, you specify it in the `skin.conf` section `[ImageGenerator]`

```
	[[[dayhumidity]]]
            [[[[outHumidity]]]]

	[[[dayinouttemp]]]
            [[[[outTemp]]]]
            [[[[inTemp]]]]
			
	[[day_images]]
		    [[[dayuv]]]
				yscale = 0, 16, 1
				[[[[UV]]]]		
			
	[[week_images]]
        x_label_format = %d
        bottom_label_format = %d-%b-%Y %X
        time_length = 604800    # == 7 days
        aggregate_type = avg
        aggregate_interval = 3600
        
        [[[weekbarometer]]]
            [[[[barometer]]]]	
```

Be sure to put the appropriate number of brackets :)
This generates an image named as in the section, e.g `dayuv.png` or `dayhumidity.png`.
The image can then be included in the HTML template:

```html
<a href="dayuv.png"><img src="dayuv.png" alt="UV index" title="UV index" width="30%" />
```

To **optimize uploads** to an external website, some resources need not be copied at each upload.
This is handled by the copy_once directive in `skin.conf`:

```
copy_once = backgrounds/*, weewx.css, mobile.css, favicon.ico, smartphone/i\
cons/*, smartphone/custom.js
```






## Operating 

To start / stop, use `service weewx start` or stop.

To generate a report: `./bin/wee_reports`

To reload the configuration: `service weewx reload`

To test your configuration: `sudo ./bin/weewxd weewx.conf`

It is possible to configure 2 weather stations in parallel. To do so, duplicate the `weewx` script of `/etc/init.d` and have it read a different configuration. Then, start each service with its name like `sudo systemctl start ecowitt`.



## Redirecting the logs

By default, weewx logs are in /var/log/syslog.
To redirect to another location, create a file in /etc/rsyslog.d, for example weewxlog.conf.

```
:programname,isequal,"weewx" /var/tmp/log/weewx.log
:programname,isequal,"weewx" ~
```

You need to restart rsyslog: service rsyslog restart.

## Mastodon / Twitter

It's possible to have the weather station automatically toot values, but for Twitter this now requires a paid subscription to access Twitter APIs.

- [Weewx Twitter extension](https://github.com/matthewwall/weewx-twitter)
- [Weewx Mastodon extension](https://github.com/glennmckechnie/weewx-mastodon)

The installation/update/uninstall is expected to be done using `wee_extension`:

`sudo ./wee_extension --install ~/weewx-twitter-0.12.tgz `

Then, you need to configure `weewx.conf` and specify your API tokens:

### Twitter config

```
[StdRESTful]
    # This section is for uploading data to sites using RESTful protocols.
    
    [[Twitter]]
        app_key = to put here
        app_key_secret = to put here
        oauth_token = to put here
        oauth_token_secret = to put here
	format = {dateTime:%X} Temp: {outTemp:%.1f} C; Humidite: {outHumidity:%.1f}%; Pression: {barometer:%.1f} hPa; Pluie: {dayRain:%.1f} mm; Vent: {windSpeed:%.1f} km/h; Dir: {windDir:%03.0f}; {windGust:%03.0f}
	unit_system = METRIC
	post_interval = 3600 
```

Add twitter as a **RESTful service**:

```
[Engines]
    # This section configures the internal weewx engines.
    # It is for advanced customization.
    
    [[WxEngine]]
    restful_services = weewx.restx.StdStationRegistry, weewx.restx.StdWunderground, weewx.restx.StdPWSweather, weewx.restx.StdCWOP, weewx.restx.StdWOW, weewx.restx.StdAWEKAS, user.twitter.Twitter
```

### Modify the tweeting extension to tweet 3 times per day

In  `/usr/share/weewx/user/twitter.py`, modify to only send tweets at given time:

```
 ts = time.localtime()
        if (ts.tm_hour != 7 and ts.tm_hour != 14 and ts.tm_hour != 18):
            logdbg("This is not hour to tweet: %d" % ts.tm_hour)
            return
```

### Mastodon config

In `weewx.conf`

```
[StdRESTful]
    [[Mastodon]]
	station = NAME OF YOUR STATION
        # from your account under preferences/development/application
        key_access_token =  PUT YOURS
        server_url_mastodon = PUT YOURS
        # Mastodon will rate limit when excessive requests are made
        post_interval = 1000
```

To post images, add the following:

```
image_directory = '/home/weewx/external_html'
images = daytempdew.png,dayrain.png,dayuv.png
```

The images must be in the same directory (`/home/weewx/external_html`). The image names are in `images`. They must be separated by a comma. 

Do **not** put the following. It would be considered as a *single* filename!

```
images = 'daytempdew.png,dayrain.png,dayuv.png'
```

To post default messages to Mastodon, you can use the `simple` or `full` option.

```
format_choice = simple
```

For a more configurable layout, use `template` and specify where the populated template will be.

```
template_file = '/home/weewx/external_html/mastodon.txt'
format_choice = template
```

This means that my Weewx skin will generate `/home/weewx/external_html/mastodon.txt`. For this to happen, you need to configure your skin `/home/weewx/skins/NAME/skin.conf`:

```
    [[ToDate]]
		[[[mastodon]]]
			template = mastodon.txt.tmpl
			encoding = strict_ascii
```

`mastodon.txt.tmpl` is a template *text* file to be created in the skin directory. So, for example, in `/home/weewx/skins/NAME/mastodon.txt.tmpl`:

```
#errorCatcher Echo
## Template file for providing data to weewx-mastodon
## https://github.com/glennmckechnie/weewx-mastodon
##
## Tag information at...
## https://weewx.com/docs/customizing.htm#Tags
Temperature: $current.outTemp (min: $day.outTemp.min, max: $day.outTemp.max)
Humidex   : $current.heatindex (min: $day.heatindex.min, max: $day.heatindex.max)
Humidite  : $current.outHumidity (min: $day.outHumidity.min, max: $day.outHumidity.max)
Pression  : $current.barometer
Pluie
- Aujourd'hui: $day.rain.sum
- Annee: $year.rain.sum
Vent:
- Direction: $current.windDir.ordinal_compass ($current.windDir deg)
- Vitesse: $current.windSpeed (moyenne), $current.windGust (rafale)
$current.dateTime.format("%d-%b-%Y %H:%M")
```

This is a template *text* file, so it understands `\n`, but it does *not* understand `<br>` (html).



## Database tweaks

The database that holds data is `archive/weewx.sdb` (unless you changed the name in the configuration file).
To retrieve the format of the archive database:
```
.schema archive
CREATE TABLE archive (`dateTime` INTEGER NOT NULL UNIQUE PRIMARY KEY, `usUnits` INTEGER NOT NULL, `interval` INTEGER NOT NULL, `barometer` REAL, `pressure` REAL, `altimeter` REAL, `inTemp` REAL, `outTemp` REAL, `inHumidity` REAL, `outHumidity` REAL, `windSpeed` REAL, `windDir` REAL, `windGust` REAL, `windGustDir` REAL, `rainRate` REAL, `rain` REAL, `dewpoint` REAL, `windchill` REAL, `heatindex` REAL, `ET` REAL, `radiation` REAL, `UV` REAL, `extraTemp1` REAL, `extraTemp2` REAL, `extraTemp3` REAL, `soilTemp1` REAL, `soilTemp2` REAL, `soilTemp3` REAL, `soilTemp4` REAL, `leafTemp1` REAL, `leafTemp2` REAL, `extraHumid1` REAL, `extraHumid2` REAL, `soilMoist1` REAL, `soilMoist2` REAL, `soilMoist3` REAL, `soilMoist4` REAL, `leafWet1` REAL, `leafWet2` REAL, `rxCheckPercent` REAL, `txBatteryStatus` REAL, `consBatteryVoltage` REAL, `hail` REAL, `hailRate` REAL, `heatingTemp` REAL, `heatingVoltage` REAL, `supplyVoltage` REAL, `referenceVoltage` REAL, `windBatteryStatus` REAL, `rainBatteryStatus` REAL, `outTempBatteryStatus` REAL, `inTempBatteryStatus` REAL);

sqlite> .schema archive_day_rain
CREATE TABLE archive_day_rain (dateTime INTEGER NOT NULL UNIQUE PRIMARY KEY, min REAL, mintime INTEGER, max REAL, maxtime INTEGER, sum REAL, count INTEGER, wsum REAL, sumtime INTEGER);
```

To show date time:

```
sqlite> select datetime(dateTime,'unixepoch', 'localtime'),... from archive where XYZ;
```

**Fixing an incorrect value in the database:**

- view the database rows: `select datetime(dateTime,'unixepoch', 'localtime'),... from archive where XYZ;`
- stop weewx: `sudo service weewx stop`
- backup weewx.sdb (just in case, but safe!
- update the rows as desired:
```
update archive set rain=0.02 where dateTime=XXX;
```

Note that the rain value is in cm. So, if you have 17.3 mm, you should set `rain=1.73`.


- [drop the daily summaries](http://www.weewx.com/docs/utilities.htm#Action_--drop-daily):
```
wee_database --drop-daily
wee_database --rebuild-daily
```

Rebuilding the daily summaries of an entire database case be quite long. So, if you just need to rebuild part of it, you can use `--from` and `--to`.

```
sudo wee_database --rebuild-daily --from=2024-03-02
```
https://github.com/bellrichm/WeeWX-MQTTSubscribe/archive/refs/tags/v2.3.1.zip
- If necessary, delete the NOAA for the affected month and year (in public_html/NOAA/)
- The rows will rebuild correctly when weewx is restarted. If you don't want to wait, you can do it offline:
```
wee_database weewx.conf --backfill-daily
```
- restart weewx: `sudo service weewx start. `


## Troubleshooting

[User group](http://groups.google.com/group/weewx-user)

Viewing the interesting part of the logs (in /var/tmp/log for example): `tail -f weewx.log | grep -v genLoop | grep -v Queuing`

### USB Connection

[You must not use usbhid, so it needs to be blacklisted](http://iadetout.free.fr/joomla/index.php?option=com_content&view=article&id=76:wview-sur-ubuntu-1204&catid=4:ubuntu)

In `/etc/modprobe.d/wmr200.conf`

```
options usbhid quirks=0x0fde:0xca01:0x4
```

Then restart modprobe:
```
sudo modprobe -r usbhid
sudo modprobe usbhid
```

```
$ lsusb
...
Bus 001 Device 032: ID 0fde:ca01 
```






