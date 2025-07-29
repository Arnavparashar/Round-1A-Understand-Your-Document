# 📘 Adobe India Hackathon - Round 1B: Persona-Driven Document Intelligence

## 🧠 Overview

This project is a local solution for **Round 1B** of the Adobe India Hackathon 2025. The goal is to build an intelligent document analyst that extracts and ranks the most relevant sections from a collection of PDFs based on:

- A given **persona**
- A **job-to-be-done**

It supports **any kind of documents**, **diverse personas**, and is built to generalize across use-cases.

---

## ✅ Sample Use-Case

**Persona**: Travel Planner  
**Job**: "Plan a trip of 4 days for a group of 10 college friends."  
**Input**: 7 PDFs related to travel in the South of France  
**Output**: A JSON file containing prioritized sections from the PDFs that are relevant to the job.

---

## 🛠️ Tech Stack

| Layer               | Tools Used                     |
|--------------------|---------------------------------|
| Language            | Python 3.10+                   |
| PDF Processing      | `PyMuPDF` (fitz)               |
| NLP & Relevance     | `scikit-learn`, `nltk`         |
| Ranking             | `TF-IDF` & `cosine similarity` |
| Output Format       | JSON                           |

---

## 📁 Folder Structure

```bash
Challenge_1b/
├── data/
│   ├── challenge1b_input.json     # Persona + job + doc list
│   └── PDFs/                      # All input PDFs here
│       ├── South of France - Cities.pdf
│       └── ...
├── output/
│   └── challenge1b_output.json    # Final extracted output
├── main.py                        # Core logic
├── README.md                      # Documentation
├── requirements.txt               # Python dependencies


