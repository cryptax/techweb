# Arduino

## Serial connection

- `screen /dev/ttyUSB0 115200`
- `picocom /dev/ttyUSB0 -b 115200`
- `microcom -p /dev/ttyUSB0 -s 115200`


## Arduino Nano v3

To program it, choose arduino board with ATmega328

## NodeMCU

[French tutorial to use it with Arduino](https://www.fais-le-toi-meme.fr/fr/electronique/tutoriel/programmes-arduino-executes-sur-esp8266-arduino-ide)

- Select the appropriate port (eg. /dev/ttyUSB0)
- Select the appropriate board: NodeMCU 1.0 ESP-12E (that's what I have)

- [Deep Sleep](https://www.losant.com/blog/making-the-esp8266-low-powered-with-deep-sleep) or [here](http://www.jerome-bernard.com/blog/2015/10/04/wifi-temperature-sensor-with-nodemcu-esp8266/)

```
Serial.print("Entering deep sleep");
ESP.deepSleep(60 * 1000000, WAKE_RF_DEFAULT);
delay(2000);
```


- [Getting a MicroPython prompt](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html)

### DHT22

Install [Adafruit Unified Sensor](https://github.com/adafruit/Adafruit_Sensor) and [DHT Sensor](https://github.com/adafruit/DHT-sensor-library) librairies in Arduino IDE.

```
#include <DHT.h>
#define DHTTYPE DHT22
uint8_t DHTPIN = D4;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
     ...
     dht.begin();
     ...
}

void loop() {
     float temperatureC = dht.readTemperature();
     float humidity = dht.readHumidity();
     if (isnan(temperatureC) || isnan(humidity)) {
     	Serial.println(F("Failed to read from DHT sensor"));
     }
}
```

| NodeMCU board | Micropython |
| ------------- | ----------- |
| D6 | `machine.Pin(12)` |
| D4 | `machine.Pin(2)` |

```python
>>> import dht
>>> import machine
>>> d = dht.DHT22(machine.Pin(2))
>>> d.measure()
>>> d.temperature()
19.3
>>> d.humidity()
53.1
```

Micropython | Board
----------- | ------
0|D3
2|D4 
4|D2
5|D1
9|SD2
10|SD3
12|D6
13|D7
14|D5
15|D8
16|D0
