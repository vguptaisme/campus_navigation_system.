# 🗺️ TIET Campus Navigation System

A lightweight, offline Python CLI tool that helps freshers at Thapar Institute of Engineering & Technology (TIET), Patiala navigate the sprawling campus with ease.

The system models the TIET campus as a weighted undirected graph with 35+ locations, academic blocks, hostels, food courts, and sports facilities. It uses Dijkstra's Algorithm to compute the shortest walking route between any two points.

## Features

- Offline CLI navigation tool
- Shortest path calculation using Dijkstra's algorithm
- Step-by-step directions with estimated walking time
- Simple numbered menu for start/destination selection

## Setup

From the repository root:

```bash
python campus_navigation_system/main.py
```

Or run it from the package folder:

```bash
cd campus_navigation_system
python main.py
```

## Notes

- The data file `data/tiet_campus_map.csv` is created automatically when needed.
- No external dependencies are required beyond the Python standard library.
- Tested with Python 3.11+.

## Usage

1. Run the script.
2. Enter the number for your start location.
3. Enter the number for your destination.
4. Review the route and repeat if needed.

Happy navigating! 🎓
