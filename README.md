# Susan-LeetCode-Journal
[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://python.org/)
[![Build](https://github.com/SusanLin0426/Susan-LeetCode-Journal/actions/workflows/ci.yml/badge.svg)](https://github.com/SusanLin0426/Susan-LeetCode-Journal/actions)
[![codecov](https://codecov.io/gh/SusanLin0426/Susan-LeetCode-Journal/graph/badge.svg?token=2FMAJRRC1C)](https://codecov.io/gh/SusanLin0426/Susan-LeetCode-Journal)

This repository serves as my daily LeetCode practice journal. It focuses on clean code and quick notes that capture key ideas and pitfalls. Beyond just solutions, it acts as a personal log of problem-solving progress and reflections, documenting both technical growth and learning patterns over time!

## LeetCode Practice in Python

Each problem has:
- Standalone function in `src/lc/...`
- Unit tests in `tests/...`
- Consistent naming: `lc{ID}_{title}.py`

### Run locally
```bash
python -m venv .venv 
source .venv/bin/activate 
pip install -e .
pytest