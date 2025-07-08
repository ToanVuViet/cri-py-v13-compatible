# CRI-Py v13 Compatible

This repository provides a modified version of the original [CRI-Python-Lib](https://github.com/CommonplaceRobotics/CRI-Python-Lib) to support Commonplace Robotics arms running firmware **version 13 or lower**.

## 🔧 Key Modifications

- Adjusted communication protocols to work with older CRI firmware (≤ v13)
- Removed or bypassed features unsupported in legacy versions
- Compatible with basic movement and joint control APIs

## 📂 Structure

```
cri_lib/
├── __init__.py
├── cri_controller.py
├── ... (your adapted files)
```

## 📦 Installation

You can install locally by cloning and using `pip`:

```bash
git clone https://github.com/TengSudo/cri-py-v13-compatible.git
cd cri-py-v13-compatible
pip install .
```

Or copy `cri_lib/` into your Python project directly.

## ⚠️ Notes

- This version is designed specifically for legacy firmware and may not work with newer robots (v14+).
- Tested on firmware v13.

## 📄 License

Based on the original CRI-Python-Lib license. Refer to `LICENSE` for details.
