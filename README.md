# Word Count Analysis Project

A comprehensive word count analysis implementation using multiple technologies and parallel processing approaches for large-scale text data processing.

## Project Overview

This project implements word count analysis - a fundamental big data benchmark - on a ~500MB text dataset using multiple approaches:
- **Multi-processing** (Python)
- **Multi-threading** (Python) 
- **Golang** implementation & concurrency
- **Apache Hadoop** Map-Reduce

### Dataset
- **Source**: [Shakespeare Dataset](https://huggingface.co/datasets/flwrlabs/shakespeare)
- **Size**: ~500MB, 4,226,158 rows
- **Description**: Part of the LEAF benchmark, built from [The Complete Works of William Shakespeare](https://www.gutenberg.org/ebooks/100) for next character prediction tasks.

## Installation

### Prerequisites
- Python 3.7+
- Golang 1.16+
- Java 8+ (for Hadoop)
- Apache Hadoop

### Hadoop Installation
For Hadoop setup on Ubuntu, follow this tutorial:
[Install Hadoop on Ubuntu](https://youtu.be/Slbi-uzPtnw?si=sSQ8en3bHuhh9NM-)

### Project Setup
```bash
# Clone the repository
git clone https://github.com/Trodyy/word-count.git
cd word count

# Install Python dependencies (if any)
pip install -r requirements.txt