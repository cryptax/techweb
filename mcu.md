# Raspberry Pico

Flashing a firmware:

- Hold Bootsel white button while you connect USB

## Temperature measurement

The Raspberry Pico includes a temperature sensor.
See [code](here)

## I2C LCD

https://microcontrollerslab.com/i2c-lcd-raspberry-pi-pico-micropython-tutorial/
https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico
https://www.instructables.com/Beginner-Projects-for-Raspberry-Pi-Pico/
https://github.com/T-622/RPI-PICO-I2C-LCD
https://microcontrollerslab.com/getting-started-raspberry-pi-pico-thonny-ide/

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