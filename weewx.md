# Weewx

## USB Connection

[You mustn't use usbhid, so it needs to be blacklisted](http://iadetout.free.fr/joomla/index.php?option=com_content&view=article&id=76:wview-sur-ubuntu-1204&catid=4:ubuntu)

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

## Install

Use the [Debian package](http://www.weewx.com/docs/usersguide.htm)

The default configuration file will be located in `/etc/weewx`

## Upgrading

See [doc](http://www.weewx.com/docs/upgrading.htm#Upgrading_using_setup.py)

## Configuration

This is important to set to test your configuration and generate debug information: `debug = 1`

The root path of weewx is essential
```
# Root directory of the weewx data file hierarchy for this station.
WEEWX_ROOT = /home/weewx/
```

Set up information about your weather station:

```
[Station]
    # This section is for information about your station
    
    # Description of the station location.
    location = Bla bla
    
    # Latitude, longitude in decimal degrees
    latitude = 41.10
    longitude = 7.07611
    
    # Altitude of the station, with unit it is in. This is downloaded from
    # from the station if the hardware supports it.
    altitude = 100, meter    # Choose 'foot' or 'meter' for unit
```

The location, latitude, longitude, altitude will then be available in HTML templates as $station.location, $station.latitude, $station.longitude and $station.altitude.

Specify the URL for your weather station's website:

```
    # If you have a website, you may optionally specify an URL for
    # its HTML server.
    #station_url = http://www.example.com
```

Specify the type of weather station:

```
    # Set to type of station hardware.  Supported stations include:
    #  Vantage   FineOffsetUSB  Ultimeter
    #  WMR100    WS28xx         WS1
    #  WMR200    WS23xx         CC3000
    #  WMR9x8    TE923          Simulator
    station_type = WMR200

[WMR200]
    # This section is for the Oregon Scientific WMR200
    
    # The station model, e.g., WMR200, WMR200A, Radio Shack W200
    model = WMR200
    
    # The driver to use:
    driver = weewx.drivers.wmr200

    archive_interval = 300
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

### Generating websites

Websites are known as 'reports'. You can set up several websites.

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

In the configuration above, I am creating two websites. One goes in public_html.
And the other one, with bigger images, goes in external_html.

The look of the website is configured in `skin.conf`.




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

### Metric units

```
[StdConvert]

    # should use US since that is what the wview database contains.
    
    # DO NOT MODIFY THIS VALUE UNLESS YOU KNOW WHAT YOU ARE DOING!
    target_unit = METRIC    # Options are 'US', 'METRICWX', or 'METRIC'
```

### Skins (look of websites)

In `skin.conf`:

```
[Extras]
  radar_img = http://www.infoclimat.fr/api/AH4EMQcrAzhVYQQtVWdXNFw2BXhQOAEpDm0PZAc1AC8AYQIzVGcHNFFlVWIFNAdjAW9RM1EzBzNWNg5n/radar/sud_est?c6efb45b781de49d57c2c0aa20e8057c
  storm_img = http://www.meteorologic.net/map/radar/your_radar.php?lat=43.37
  radar_url = http://www.infoclimat.fr

```

#### Specifying Units

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

#### Customized labels

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

#### HTML files to generate

```
   [[ToDate]]
        # Reports that show statistics "to date", such as day-to-date,
        # week-to-date, month-to-date, etc.
	[[[about]]]
	    template = about.html.tmpl

	[[[almanac]]]
	    template = almanac.html.tmpl
```

The HTML templates are to be located in the same directory as the skin.
For example, to display the UV  index:

```html
#if $day.UV.has_data
    <tr>
    <td>UV</td>
    <td>$current.UV</td>
    </tr>
#end if
```

To display particular values, you can use variables such as:

- $current.inTemp
- $current.outTemp
- $current.windSpeed
- $day.inTemp.max
- `$day.inTemp.maxtime.format("%H:%M")`
- $yesterday.inTemp.avg
- `$span($hour_delta=24).rain.sum`
- `$month($months_ago=1).rain.sum`

Or even some form of logic:

```
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


#### Charts to generate

```
	[[[dayhumidity]]]
            [[[[outHumidity]]]]
```

or

```
[[[dayinouttemp]]]
            [[[[outTemp]]]]
            [[[[inTemp]]]]
```


Be sure to put the appropriate number of brackets.

To generate a UV graph, in `skin.conf`:
```
[[day_images]]
 [[[dayuv]]]
            yscale = 0, 16, 1
            [[[[UV]]]]
```

and in the HTML template:

```html
<a href="dayuv.png"><img src="dayuv.png" alt="UV index" title="UV index" width="30%" />
```



#### Optimization

To optimize uploads to an external website, some resources need not be copied at each upload.
This is handled by the copy_once directive in skin.conf:

```
copy_once = backgrounds/*, weewx.css, mobile.css, favicon.ico, smartphone/i\
cons/*, smartphone/custom.js
```





## Operating 

To start / stop, use `service weewx start` or stop.

To generate a report: `./bin/wee_reports`

To reload the configuration: `service weewx reload`

To test your configuration: `sudo ./bin/weewxd weewx.conf`


## Redirecting the logs

By default, weewx logs are in /var/log/syslog.
To redirect to another location, create a file in /etc/rsyslog.d, for example weewxlog.conf.

```
:programname,isequal,"weewx" /var/tmp/log/weewx.log
:programname,isequal,"weewx" ~
```

You need to restart rsyslog: service rsyslog restart.

## Sending date to Twitter account

Download the [extension](http://sourceforge.net/p/weewx/wiki/twitter/") and follow the configuration steps. In particular,

```
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install twython
sudo setup.py install --extension weewx-twitter.x.y.tgz
```

In WEEWX_ROOT/bin/usr/twitter.py, modify to only send tweets at given time:
<pre>
 ts = time.localtime()
        if (ts.tm_hour != 7 and ts.tm_hour != 14 and ts.tm_hour != 18):
            logdbg("This is not hour to tweet: %d" % ts.tm_hour)
            return
</pre>



In weewx.conf,

- configure Twitter service:
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
- add twitter as a RESTful service:
```
[Engines]
    # This section configures the internal weewx engines.
    # It is for advanced customization.
    
    [[WxEngine]]
    restful_services = weewx.restx.StdStationRegistry, weewx.restx.StdWunderground, weewx.restx.StdPWSweather, weewx.restx.StdCWOP, weewx.restx.StdWOW, weewx.restx.StdAWEKAS, user.twitter.Twitter
```

### Database tweeks

The database that holds data is archive/weewx.sdb (unless you changed the name in the configuration file).
To retrieve the format of the archive database:
```
.schema archive
CREATE TABLE archive (`dateTime` INTEGER NOT NULL UNIQUE PRIMARY KEY, `usUnits` INTEGER NOT NULL, `interval` INTEGER NOT NULL, `barometer` REAL, `pressure` REAL, `altimeter` REAL, `inTemp` REAL, `outTemp` REAL, `inHumidity` REAL, `outHumidity` REAL, `windSpeed` REAL, `windDir` REAL, `windGust` REAL, `windGustDir` REAL, `rainRate` REAL, `rain` REAL, `dewpoint` REAL, `windchill` REAL, `heatindex` REAL, `ET` REAL, `radiation` REAL, `UV` REAL, `extraTemp1` REAL, `extraTemp2` REAL, `extraTemp3` REAL, `soilTemp1` REAL, `soilTemp2` REAL, `soilTemp3` REAL, `soilTemp4` REAL, `leafTemp1` REAL, `leafTemp2` REAL, `extraHumid1` REAL, `extraHumid2` REAL, `soilMoist1` REAL, `soilMoist2` REAL, `soilMoist3` REAL, `soilMoist4` REAL, `leafWet1` REAL, `leafWet2` REAL, `rxCheckPercent` REAL, `txBatteryStatus` REAL, `consBatteryVoltage` REAL, `hail` REAL, `hailRate` REAL, `heatingTemp` REAL, `heatingVoltage` REAL, `supplyVoltage` REAL, `referenceVoltage` REAL, `windBatteryStatus` REAL, `rainBatteryStatus` REAL, `outTempBatteryStatus` REAL, `inTempBatteryStatus` REAL);

sqlite> .schema archive_day_rain
CREATE TABLE archive_day_rain (dateTime INTEGER NOT NULL UNIQUE PRIMARY KEY, min REAL, mintime INTEGER, max REAL, maxtime INTEGER, sum REAL, count INTEGER, wsum REAL, sumtime INTEGER);
```


## Troubleshooting

[User group](http://groups.google.com/group/weewx-user)

Viewing the interesting part of the logs: `tail -f weewx.log | grep -v genLoop | grep -v Queuing`

### Fixing an incorrect value in the database

- stop weewx: sudo service weewx stop
- backup weewx.sdb (just in case, but safe!
- update the rows as desired:
```
update archive set rain=0.02 where dateTime=XXX;
```
- [drop the daily summaries](http://www.weewx.com/docs/customizing.htm#Dropping_and_rebuilding_the_daily_summaries)
```
wee_config_database weewx.conf --drop-daily
```
- If necessary, delete the NOAA for the affected month and year (in public_html/NOAA/)
- The rows will rebuild correctly when weewx is restarted. If you don't want to wait, you can do it offline:
```
wee_database weewx.conf --backfill-daily
```
- restart weewx: sudo service weewx start. 




