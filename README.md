# README

Simple demo for Bosch BME68x / BSEC2 datalogging, BLE and inference

## Summary
- A PlatformIO-based demo integrating Bosch BME680/BME688 sensors with the BSEC2 library for IAQ/gas estimation, SD-card datalogging, BLE control/streaming, and optional classification/regression using BSEC configuration strings.

## Quick Start / Prerequisites
- Platform: PlatformIO (VS Code PlatformIO extension) on ESP32/ESP8266 toolchain.
- Required libraries: BSEC2 library (from Bosch — proprietary), SdFat, RTClib, ArduinoJson, BLE libs (ESP32 BLEDevice / BLEServer), base64, and Arduino core libraries referenced in `platformio.ini`.
- Hardware: BME680 / BME688 sensor(s), SD card (SPI), and a BLE-capable board (e.g., ESP32). Sensors should be conditioned (hours) for stable BSEC outputs.

## Repository layout
- [platformio.ini](platformio.ini): Build environments and targets.
- [src](src/):
  - [src/main_basic.cpp](src/main_basic.cpp) — Minimal BSEC integration and serial output.
  - [src/main_full.cpp](src/main_full.cpp) — Full demo: SD logging, BLE control, multi-sensor support, BSEC integration.
  - [src/main_inference.cpp](src/main_inference.cpp) — Inference-focused example using BSEC config strings.
- [lib/project_lib/src](lib/project_lib/src): Core modules
  - [lib/project_lib/src/ble_controller.h](lib/project_lib/src/ble_controller.h) — BLE command parsing, queueing, notifications.
  - [lib/project_lib/src/bme68x_datalogger.h](lib/project_lib/src/bme68x_datalogger.h) — Raw sensor datalogging to SD.
  - [lib/project_lib/src/bsec_datalogger.h](lib/project_lib/src/bsec_datalogger.h) — BSEC outputs datalogging and AI config handling.
  - [lib/project_lib/src/label_provider.h](lib/project_lib/src/label_provider.h) — Label storage/lookup.
  - [lib/project_lib/src/led_controller.h](lib/project_lib/src/led_controller.h) — Status LEDs.
  - [lib/project_lib/src/sensor_manager_custom.h](lib/project_lib/src/sensor_manager_custom.h) — Sensor scheduling.
  - [lib/project_lib/src/utils.h](lib/project_lib/src/utils.h) — SD/RTC/file helpers.
  - [lib/project_lib/src/demo_app.h](lib/project_lib/src/demo_app.h) — App modes, return codes, shared types.
- [config](config/): BSEC configuration strings and CSVs for different sensors and AI models (e.g., FieldAir_HandSanitizer).
- [include](include/): Board/specific pin definitions.

How it works (high level)
- Example mains initialize peripherals (SD, RTC, BLE), configure BME sensors, load BSEC config (optional), subscribe to outputs, and either log raw sensor data or run BSEC processing.
- `ble_controller` exposes BLE commands to control streaming, request files, set labels/ground-truth, and query firmware/app mode.
- Dataloggers write JSON-like records to SD, manage label files and AI config headers.

Notes & gotchas
- The BSEC2 library and some config blobs are proprietary — obtain and place the correct BSEC2 package and config strings (see `config/`) before building.
- Sensor conditioning: run sensors for long periods (hours) to stabilize BSEC outputs.
- SD card CS pin and board-specific wiring may need adapting — check `include/custom_pins.h` and [lib/project_lib/src/utils.h](lib/project_lib/src/utils.h) (`PIN_SD_CS`).

Where to start
- Quick test: build and upload [src/main_basic.cpp](src/main_basic.cpp) and monitor serial.
- Full features (BLE + logging + multi-sensor): build [src/main_full.cpp](src/main_full.cpp).
- AI/inference experiments: inspect `config/` for `*.config` / `bsec_selectivity.txt` blobs and use [src/main_inference.cpp](src/main_inference.cpp).
'@



## Useful links:

- Bosch page: https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/
- BME Ai studio docs: https://www.bosch-sensortec.com/software/bme/docs/overview/getting-started.html
- BME68x lib: https://github.com/boschsensortec/Bosch-BME68x-Library
- BSEC 2 lib: https://github.com/boschsensortec/Bosch-BSEC2-Library

## Learning videos (BME AI-Studio):

- Get started: https://youtu.be/w-gjhBDn404?si=iI1nBctkQi6j6CFe
- Project setup: https://youtu.be/NMeq722qaVA?si=CnptIfdL70_tgy3a
- Import data: https://youtu.be/JS46gXtL3e0?si=R4XQFrts7fsdm_nz
- Label specimen: https://youtu.be/_Qi7dAUjmgw?si=8f4RLqyG8JRYAhM_