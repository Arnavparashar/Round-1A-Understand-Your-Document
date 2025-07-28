Adobe India Hackathon – Round 1A: PDF Outline Extractor
This repository contains the solution for Round 1A of Adobe’s “Connecting the Dots” Hackathon. The task is to extract a structured outline from PDF files, including the Title, and heading levels (H1, H2, H3), and return the result in a specific JSON format.

🛠 Tech Stack
Python 3.8+

PyMuPDF (fitz) – for PDF parsing and font metadata

JSON – structured output format

Docker – for containerized deployment (optional)

📁 Project Structure
graphql
Copy
Edit
.
├── input/                # Folder containing input PDFs
├── output/               # Folder where extracted JSONs are saved
├── main.py               # Core logic to extract structure
├── Dockerfile            # (Optional) Docker container setup
🔄 Workflow
Analyze Font Styles:
Parses all pages to determine the most common (body) font size and detect heading styles based on size and boldness.

Identify Heading Levels:
Largest size → H1, next → H2, then H3.

Extract Title:
Largest text block on the first page is selected as the document title.

Build Outline:
Text blocks matching heading criteria are extracted along with their page numbers and structured hierarchically.

Output:
Results are written as JSON files into the output/ folder.

