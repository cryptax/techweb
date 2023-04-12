# Raspberry Pico

Flashing a firmware:

- Hold Bootsel white button while you connect USB

## Temperature measurement

The Raspberry Pico includes a temperature sensor.
See [code](here)

## I2C LCD

This is a 1602 screen with a I2C adapter.

- Download [library I2C LCD for Pico](https://github.com/T-622/RPI-PICO-I2C-LCD)
- Wire SDA, SCL, VCC to VBUS of Pico, and GND. See Pinout.
- Scan I2C devices to get the I2C address of the LCD screen (it's 0x27):

```python
import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
print(i2c.scan())
```

- Drop `lcd_api.py` and `pico_i2c_lcd.py` on the device, as root. `ampy --port /dev/ttyACM0 put filename destination`

- Use the library:

```python
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear()
lcd.putstr("Hello")
```

- Add the program and run it `ampy --port /dev/ttyACM0 run progname`

- [Display Custom characters](https://microcontrollerslab.com/i2c-lcd-raspberry-pi-pico-micropython-tutorial/)
- [LCD + Pico](https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico)
- [Several projects with the Pico](https://www.instructables.com/Beginner-Projects-for-Raspberry-Pi-Pico/)
- [With Thonny](https://microcontrollerslab.com/getting-started-raspberry-pi-pico-thonny-ide/)

## References

- [Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [Getting started with Pico](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf): C/C++ development manual
- [Pinout](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#pinout-and-design-files)
- [Pros & cons on the Pico](https://picockpit.com/raspberry-pi/fr/tout-ce-qui-concerne-le-raspberry-pi-pico) - includes PIO
- [PIO state machine](https://medium.com/geekculture/raspberry-pico-programming-with-pio-state-machines-e4610e6b0f29)
- [ARM Assembly with Pico](https://blog.smittytone.net/2022/06/19/get-started-with-arm-assembly-on-the-pi-pico/)
- [Remote MicroPython Shell](https://github.com/dhylands/rshell)
- [Ampy and TIO](https://bigl.es/tuesday-tooling-pico-mix/)
- [Play a melody](https://electroniqueamateur.blogspot.com/2021/07/jouer-une-melodie-avec-le-raspberry-pi.html)
- [I2C LCD](https://github.com/T-622/RPI-PICO-I2C-LCD)


# Screen

Ctrl-A, Ctrl-D to detach screen

# Ampy

- Install: `pip install adafruit-ampy`
- List files on the device: `ampy --port /dev/ttyACM0 ls`
- Create a directory: `ampy --port /dev/ttyACM0 mkdir /lib`
- Put a file on the device `ampy --port /dev/ttyACM0 put lcd_api.py ./lib/lcd_api.py`
- Run a file: `ampy --port /dev/ttyACM0 run mypython.py`