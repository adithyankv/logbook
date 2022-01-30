# Logbook
Utility for viewing systemd logs

## Building, Testing and Installation
You'll need the following dependencies
- meson
- python3
- python3-gi
- python3-systemd
- libgranite-dev

Download or clone the repository
```
git clone https://github.com/adithyankv/logbook.git
cd logbook
```
Run `meson` to configure the build environment and run `ninja` to build
```
meson build --prefix=/usr
cd build
ninja
```
To install use `ninja install`, then execute with `com.github.adithyankv.logbook`

## Thanks/Credits
- [ElementaryPython](https://github.com/mirkobrombin/ElementaryPython) and 
[QuickWord](https://github.com/hezral/quickword) for code reference
