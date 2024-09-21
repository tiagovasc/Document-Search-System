# Document-Search-System

## Overview

This project extracts textual content from EPUB and PDF documents using specific keyword searches. It is designed for academic researchers, data scientists, and professionals who manage large digital document databases. Note: the current method for recognizing paragraphs in PDFs may not be fully optimal, potentially affecting content precision.

The system identifies and extracts paragraphs containing specified keywords and their surrounding context, ensuring the usefulness of the text for further analysis or processing. The solution employs enhanced keyword search techniques to achieve targeted and relevant text retrieval, improving upon general content retrieval systems like RAG (Retrieval-Augmented Generation).

## How It Works

The process involves several steps to ensure text accuracy and relevance:

1. **Keyword Definition**:
   - Users specify keywords relevant to their research or analysis, adjustable for different focus areas.

2. **Document Parsing**:
   - The script processes EPUB or PDF files using `ebooklib`, `PyPDF2`, and `BeautifulSoup`, structuring the content for searching.

3. **Keyword Search and Context Extraction**:
   - The script locates all instances of each keyword, extracting the paragraph it appears in along with preceding and following paragraphs to maintain context.

4. **Relevance Filtering**:
   - Extracts undergo a minimum word count check to ensure they provide sufficient context; those that do not meet this threshold are excluded.

5. **Combination and Deduplication**:
   - Overlapping or contiguous extracts are merged to maintain output conciseness and avoid redundancy.

6. **Output**:
   - The script provides a summary of findings, including counts of total and combined extracts per keyword, offering an overview of content relevance and density.

## Motivation

This system was developed as an alternative to Retrieval-Augmented Generation (RAG), which struggles with large datasets and often misses key information. By focusing on specific keywords, this project enhances the precision of content retrieval.

## Future Plans

The current system outputs directly relevant text sections but may include irrelevant ones. Future development will incorporate a Language Model (LLM) to evaluate text section relevance more precisely. Challenges include managing the volume of outputs, with plans to use cost-effective models and batch processing to reduce expenses and increase efficiency.

## Limitations & Solutions

A primary limitation is the retrieval method's tendency to include irrelevant content based on keyword presence or to overlook necessary data if the keyword is absent. This will be addressed by expanding the synonym list to reduce false positives and negatives, and by using lighter models for initial filtering.

## Conclusion

This project aims to establish a precise and efficient retrieval system, distinct from and potentially superior to RAG. As lightweight LLMs advance, the cost-effectiveness of querying large datasets will enhance the accessibility and utility of content retrieval across various fields.
