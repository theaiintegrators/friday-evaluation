# 🧪 Friday Evaluation

*Modular framework for testing and validating AI workflows*

<p align="left">
  <a href="https://github.com/theaiintegrators"><img src="https://img.shields.io/badge/Friday--Ecosystem-4B8BF5" /></a>
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/python-3.9_3.10_3.11-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</p>

------------------------------------------------------------------------

## 🌟 Overview

**Friday Evaluation** is the lightweight evaluation engine for:

-   scoring workflows
-   validating outputs
-   defining tasks & datasets
-   building custom rubrics

No LLMs or proprietary logic included.

------------------------------------------------------------------------

## ✨ Features (Public Edition)

-   JSON-defined tasks
-   Dataset-driven evaluation
-   Simple scoring templates
-   Plug-in evaluator
-   CLI demo runner

------------------------------------------------------------------------

## 🏛 Architecture

    Task → Dataset → Evaluator → Scores → Report

------------------------------------------------------------------------

## 📚 Repository Structure

    friday-evaluation/
      ├── evaluations/
      ├── friday_evaluation/
      ├── examples/
      ├── requirements.txt
      ├── LICENSE
      └── README.md

------------------------------------------------------------------------

## 🚀 Quick Start

``` bash
git clone https://github.com/theaiintegrators/friday-evaluation
cd friday-evaluation

python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows PowerShell

pip install -r requirements.txt
python -m examples.run_demo
```

------------------------------------------------------------------------

## 🧭 Roadmap

-   MCP tool integration
-   Parallel execution patterns
-   Workflow visualizer
-   LangFuse auto-enrichment
-   Built‑in safety evaluators
-   Friday CLI
-   Deployment templates

------------------------------------------------------------------------

## 🔭 Vision

Friday aims to make AI systems:

-   **Predictable**
-   **Testable**
-   **Observable**
-   **Enterprise-ready**

With a code-first, extensible design that scales from prototypes to full
production platforms.

------------------------------------------------------------------------

## 📄 License

MIT License
Copyright © 2025
The AI Integrators

------------------------------------------------------------------------

## 💬 Contact & Contributions

-   Open an Issue or Discussion
-   PRs welcome
-   https://github.com/theaiintegrators
