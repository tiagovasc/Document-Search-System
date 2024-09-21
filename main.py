!pip install EbookLib
!pip install BeautifulSoup4

import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re  # Import the regex module for improved keyword matching

# Define your list of keywords separated by commas
keywords = "Music, Art, Pitch, Concert, Jazz, Symphony, Instrument, Melody".split(", ")

def check_file_path(epub_path):
    if os.path.exists(epub_path):
        print("File found: Proceeding with processing...")
    else:
        print("File not found. Check the file path and try again.")
        return False  # Stop further execution if file is not found
    return True

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    texts = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            for p in soup.find_all('p'):
                texts.append(p.text)
    return texts

def find_relevant_sections(texts, keywords):
    collected_texts = {}
    text_counts = {}
    combined_counts = {}
    for keyword in keywords:
        collected_texts[keyword] = []
        text_counts[keyword] = 0
        combined_counts[keyword] = 0
        keyword_pattern = r'\b' + re.escape(keyword) + r'\b'  # Use regex to match only full words

        for i, text in enumerate(texts):
            if re.search(keyword_pattern, text, re.IGNORECASE):  # Use regex search with case-insensitive match
                previous_paragraph = texts[i - 1] if i > 0 else ""
                target_paragraph = text
                next_paragraph = texts[i + 1] if i + 1 < len(texts) else ""
                combined_text = " ".join([previous_paragraph, target_paragraph, next_paragraph])
                combined_text = " ".join(combined_text.split())

                if len(combined_text.split()) > 20:
                    if not collected_texts[keyword] or not combined_text in collected_texts[keyword]:
                        collected_texts[keyword].append(combined_text)
                        text_counts[keyword] += 1
                    else:
                        combined_counts[keyword] += 1

    return collected_texts, text_counts, combined_counts

# Define the path to your EPUB file
epub_path = '/content/meaning.co.epub'

# Check if the file exists at the specified path
if check_file_path(epub_path):
    texts = extract_text_from_epub(epub_path)
    relevant_sections, text_counts, combined_counts = find_relevant_sections(texts, keywords)

    # Print the counts for each keyword first
    print("Extraction Summary:")
    for keyword in keywords:
        print(f"Keyword: {keyword}")
        print(f"Total extracted sections: {text_counts[keyword]}")
        print(f"Sections combined due to overlap: {combined_counts[keyword]}")
        print("-" * 80)

    # Print each relevant section separated by a line for each keyword
    for keyword in keywords:
        print(f"\nSections for '{keyword}':")
        for section in relevant_sections[keyword]:
            print(section)
            print("\n" + "-"*80 + "\n")
else:
    print("File not found. Please check the file path and try again.")
