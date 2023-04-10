<p align="center">
  <img width="18%" align="center" src="https://raw.githubusercontent.com/zhiyiYo/PyQt-Fluent-Widgets/master/docs/source/_static/logo.png" alt="logo">
</p>
  <h1 align="center">
  QtPy-Fluent-Widgets
</h1>
<p align="center">
  A fluent design widgets library based on QtPy
</p>

<p align="center">
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=#4ec820" alt="Platform Win32 | Linux | macOS"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://static.pepy.tech/personalized-badge/qtpy-fluent-widgets?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Download"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/License-GPLv3-blue?color=#4ec820" alt="GPLv3"/>
  </a>
</p>

![Interface](https://raw.githubusercontent.com/zhiyiYo/PyQt-Fluent-Widgets/master/docs/source/_static/Interface.jpg)


## Install
To install lite version (`AcrylicLabel` is not available):
```shell
pip install QtPy-Fluent-Widgets -i https://pypi.org/simple/
```
Or install full-featured version:
```shell
pip install "QtPy-Fluent-Widgets[full]" -i https://pypi.org/simple/
```

If you are using PySide2, PySide6 or PyQt6, you can download the code in [PySide2](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide2), [PySide6](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6) or [PyQt6](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6) branch.


## Run Example
After installing PyQt-Fluent-Widgets package using pip, you can run any demo in the examples directory, for example:
```sh
cd examples/gallery
python demo.py
```
```python
# you can specify qt api through
python demo.py --api pyside6
# or specify qt api in the beginning of program through
from qtfluentwidgets import set_qt_api
set_qt_api("pyside6")
```

## Documentation
Want to know more about PyQt-Fluent-Widgets? Please read the [help document](https://pyqt-fluent-widgets.readthedocs.io/) 👈

## Video Demonstration
Check out this [▶ example video](https://www.bilibili.com/video/BV12c411L73q) that shows off what PyQt-Fluent-Widgets are capable of 🎉

## See Also
Here are some projects that use PyQt-Fluent-Widgets:
* [**zhiyiYo/Groove**: A cross-platform music player based on PyQt5](https://github.com/zhiyiYo/Groove)
* [**zhiyiYo/Alpha-Gobang-Zero**: A gobang robot based on reinforcement learning](https://github.com/zhiyiYo/Alpha-Gobang-Zero)

## Reference
* [**Windows design**: Design guidelines and toolkits for creating native app experiences](https://learn.microsoft.com/zh-cn/windows/apps/design/)
* [**Microsoft/WinUI-Gallery**: An app demonstrates the controls available in WinUI and the Fluent Design System](https://github.com/microsoft/WinUI-Gallery)

## License
PyQt-Fluent-Widgets is licensed under [GPLv3](./LICENSE).

Copyright © 2021 by zhiyiYo.
