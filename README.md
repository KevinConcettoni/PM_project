# Process Mining Comparative Analysis 🔍

A comprehensive study comparing process mining tools and algorithms using the Hospital Billing Event Log dataset.

## 📋 Project Overview

This project explores and analyzes different process mining platforms to evaluate their capabilities, performance, and usability. The core objective is to assess how various tools interpret and visualize event logs, and how effectively they support process analysis tasks such as process discovery, conformance checking, and performance analysis.

## 🎯 Objectives

- Compare process mining tools: **Disco** and **PM4PY**
- Evaluate process discovery algorithms: **Alpha Miner** and **Heuristic Miner**
- Analyze tool capabilities for handling real-world event logs
- Provide practical insights for tool selection based on specific requirements

## 📊 Dataset

**Hospital Billing Event Log** - A comprehensive dataset from a regional hospital's ERP system containing:
- ~100,000 traces representing billing processes
- 3 years of temporal coverage
- Anonymized data with preserved relative timing
- Multiple enriched attributes including process states and diagnostic information

The dataset focuses on administrative and financial billing processes rather than clinical procedures, providing a realistic view of healthcare administrative workflows.

## 🛠️ Tools & Technologies

### Disco
- **Type**: Commercial process mining software
- **Algorithm**: Proprietary fuzzy miner
- **Strengths**: 
  - Intuitive user interface
  - Visual process maps with frequency and performance indicators
  - User-friendly for non-technical users
  - Immediate process visualization upon import

### PM4PY
- **Type**: Open-source Python library
- **Algorithms**: Alpha Miner, Heuristic Miner, Inductive Miner
- **Strengths**:
  - Comprehensive algorithmic suite
  - Integration with Python data science ecosystem
  - Extensible and customizable
  - Support for XES and CSV formats

## 🚀 Getting Started

### Prerequisites

- Python
- Pm4py

You can simply install all the requirements:

```bash
pip install requirements.txt
```
### Run the scripts

```bash
python Main.py
```

## 🔍 Analysis Insights

### Disco Analysis
- Excellent for rapid process visualization
- Effective identification of dominant workflows
- Clear bottleneck and deviation detection
- Performance view reveals timing variations (some data quality issues noted)

### PM4PY Analysis
- **Alpha Miner**: Theoretical soundness but limited real-world applicability
- **Heuristic Miner**: Superior handling of complex, noisy data
- Comprehensive conformance checking capabilities
- Flexible algorithmic framework

## 👨‍💼 Author

**Kevin Concettoni**   
University of Camerino - Computer Science (LM-18)  
A.Y. 2024/2025  

## 📚 References

- van der Aalst, W. M. P. (2011). Process Mining: Discovery, Conformance and Enhancement of Business Processes
- Berti, A., van Zelst, S. J., & van der Aalst, W. M. P. (2019). Process Mining for Python (PM4Py)
- Mannhardt, F. (2017). Hospital Billing - Event Log Dataset
- Weijters, A. M. M., van der Aalst, W. M. P., & Weske, M. (2006). Process mining with the heuristic miner

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software in accordance with the terms of the license.

This project is also part of academic coursework at the University of Camerino.  
Please respect academic integrity guidelines when referencing this work.
