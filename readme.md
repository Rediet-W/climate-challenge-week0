# Climate Challenge Week 0

This project serves as the foundational setup for the Climate Challenge data science workflow. It includes environment management, version control configurations, and CI/CD pipelines.

## Prerequisites

Before getting started, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Python 3.x](https://www.python.org/)
- An IDE (e.g., [VS Code](https://code.visualstudio.com/))

## Setup Instructions

Follow these steps to set up the development environment locally:

### 1. Clone the repository

```bash
git clone https://github.com/Rediet-W/climate-challenge-week0.git
cd climate-challenge-week0
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Project Structure

- `.github/workflows/`: CI/CD pipeline configurations (GitHub Actions).
- `notebooks/`: Jupyter notebooks for data analysis and exploration.
- `scripts/`: Python scripts for data processing and automation.
- `src/`: Source code modules and packages.
- `tests/`: Unit tests to ensure code quality.

## Continuous Integration (CI)

This repository uses GitHub Actions to automate environment checks. Every time you push to the `main` branch, the CI pipeline will verify the project requirements and Python version.

```

```
