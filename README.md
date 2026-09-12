# Food Delivery Demand Analytics

## Problem Statement
Food delivery teams often need to understand restaurant demand and delivery activity from
raw operational records. This project demonstrates a small Python data pipeline that cleans
restaurant records, calculates tiered commissions, manages order objects, persists records to
JSON, and fetches mock restaurant data from a public API. The project also demonstrates a
professional Git workflow with branches, commits, and a pull-request-oriented development process.

## Folder Structure

| Path | Purpose |
|---|---|
| `src/` | Python source files for cleaning, fee calculation, persistence, and the console pipeline |
| `data/raw/` | Raw input/sample data |
| `data/processed/` | JSON output produced by the programs |
| `docs/` | Assessment answers and supporting documentation |
| `tests/` | Basic automated tests |
| `.gitignore` | Ignores virtual environments, secrets, compiled files, and logs |
| `README.md` | Project documentation |

## Setup Instructions

1. Install Python 3.10+.
2. Open a terminal in this repository.
3. (Optional) Create a virtual environment:
   `python -m venv venv`
4. Activate it on Windows:
   `venv\Scripts\activate`
5. Install the dependency:
   `pip install requests`
6. Run the programs from the repository root, for example:
   `python src/task2_cleaning.py`
   `python src/task3_fee_calculator.py`
   `python src/task4_record_manager.py`
   `python src/food_delivery_pipeline.py`

## Usage

Run `python src/food_delivery_pipeline.py` for the menu-driven capstone console tool.
Option 1 fetches mock restaurants, option 2 adds a restaurant, option 3 calculates commissions,
and option 4 saves/loads JSON records.

## Git Workflow

Work should be developed on feature branches and merged into `main` only after review.
The `docs/git_commands.txt` file contains the command sequence used for the assessment.
