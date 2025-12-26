# README

## Setup
- All you need is [platform.io](https://platformio.org/) and an editor, VSCode is recommended.

## Structure overview
- The main code lives in `/src`, you will find 3 files there:
    - `main_basic.cpp` -> Simple environmental data read
    - `main_inference.cpp` -> Can be used to run the inference model generated from AI studio
    - `main_full.cpp` -> For data recording to SD Card
- This repo is based on a modified version of the BME68x and BSEC2 libraries, modifield files are under: `/lib/project_lib`.
- 

## Useful links:

- Bosch page: https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/
- BME Ai studio docs: https://www.bosch-sensortec.com/software/bme/docs/overview/getting-started.html
- BME68x lib: https://github.com/boschsensortec/Bosch-BME68x-Library
- BSEC 2 lib: https://github.com/boschsensortec/Bosch-BSEC2-Library
