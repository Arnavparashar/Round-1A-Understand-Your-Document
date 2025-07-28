import fitz  
import os
import json
import re
from collections import Counter

INPUT_DIR = "C:/Users/arnav/OneDrive/Desktop/PDFextractor/input"
OUTPUT_DIR = "C:/Users/arnav/OneDrive/Desktop/PDFextractor/output"

def clean_text(text):
    text = text.strip()
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)

def analyze_styles(doc):
    size_counts = Counter()
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block['type'] != 0:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    size = round(span["size"])
                    text = span["text"].strip()
                    if text:
                        size_counts[size] += len(text)
    if not size_counts:
        return {}, 0

    body_size = size_counts.most_common(1)[0][0]
    heading_sizes = sorted([s for s in size_counts if s > body_size], reverse=True)

    style_map = {}
    for idx, size in enumerate(heading_sizes[:3]):
        style_map[size] = f"H{idx+1}"
    return style_map, body_size

def extract_structure(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Failed to open {pdf_path}: {e}")
        return {"title": os.path.basename(pdf_path), "outline": []}

    if doc.page_count == 0:
        return {"title": os.path.basename(pdf_path), "outline": []}

    style_map, body_size = analyze_styles(doc)
    outline = []
    seen = set()

    # Try to find the title from the first page
    title = ""
    max_size = 0
    for block in doc[0].get_text("dict")["blocks"]:
        if block['type'] != 0:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                size = span["size"]
                text = clean_text(span["text"])
                if size > max_size and len(text) > 5:
                    max_size = size
                    title = text.strip()

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block['type'] != 0:
                continue
            for line in block["lines"]:
                line_texts = [clean_text(s["text"]) for s in line["spans"] if s["text"].strip()]
                if not line_texts:
                    continue
                full_text = " ".join(line_texts)
                span = line["spans"][0]
                size = round(span["size"])
                level = style_map.get(size)

                # Additional heuristic if not detected by size
                if not level:
                    font = span["font"].lower()
                    is_bold = "bold" in font
                    is_upper = full_text.isupper()
                    is_short = len(full_text.split()) <= 10
                    if is_bold and is_upper and is_short:
                        level = "H2"

                if level and (level, full_text) not in seen:
                    outline.append({
                        "level": level,
                        "text": full_text,
                        "page": page_num + 1
                    })
                    seen.add((level, full_text))

    doc.close()
    return {"title": title.strip(), "outline": outline}

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"Processing {pdf_path}...")
            try:
                result = extract_structure(pdf_path)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=4, ensure_ascii=False)
                print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
