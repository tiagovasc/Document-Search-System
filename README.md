# Document-Search-System

## Overview

This system is engineered to retrieve relevant textual content from vast content databases, using EPUB and PDF documents as sources. It performs this retrieval through traditional keyword searches, ideal for users who need to efficiently navigate through large volumes of text to extract contextually relevant information. This tool is particularly useful for academic researchers, data scientists, and professionals managing large databases of digital books and documents. It should be noted that the method for identifying paragraphs in PDFs may not perform optimally, which could impact the accuracy of the retrieved content.

The system is designed not only to locate paragraphs containing specified keywords but also to include the surrounding context. This methodology ensures the extracted text is meaningful and retains the context necessary for subsequent content analysis or processing. The project employs advanced keyword search techniques, which are straightforward yet refined to maximize relevance and accuracy, addressing common issues encountered with generalized content retrieval systems like RAG (Retrieval-Augmented Generation).

## How It Works

The process consists of several steps, each ensuring the precise and relevant retrieval of text:

1. **Keyword Definition**:
   - Users define keywords relevant to their research needs, adjustable to suit various topics or focus areas.

2. **Document Parsing**:
   - The script reads through EPUB or PDF files, using libraries such as `ebooklib`, `PyPDF2`, and `BeautifulSoup` to parse the content, preparing it for detailed analysis.

3. **Keyword Search and Context Extraction**:
   - The script identifies all occurrences of each keyword within the documents, extracting not just the specific paragraphs but also the preceding and following paragraphs to maintain the textual context.

4. **Relevance Filtering**:
   - Extracts are evaluated against a minimum word count to ensure they provide ample context. Sections not meeting this criterion are excluded.

5. **Combination and Deduplication**:
   - Adjacent or overlapping extracts are merged to ensure the output is concise and free from redundancy.

6. **Output**:
   - The findings are summarized, detailing the counts of extracted sections for each keyword to provide an overview of the content's relevance and density.

## Motivation

This project was initiated as an alternative to the commonly used Retrieval-Augmented Generation (RAG), which can struggle with large datasets and often overlooks significant content. This system begins by selecting content based on word selection and currently outputs the relevant sections of text directly.

## Future Plans

While the system successfully extracts text where keywords are mentioned, it occasionally includes sections that are not entirely relevant. The next development phase involves integrating a Language Model (LLM) to assess the relevance of each text section more accurately. This enhancement aims to refine the content database, ensuring it contains only pertinent sections. Given the potential volume of outputs—approximately 100 relevant sections from 1000 pages—the processing might become costly and slow. To mitigate this, plans include using cost-effective models and batching several sections into a single API call to enhance efficiency and reduce costs.

## Limitations & Solutions

The main challenge is the method’s tendency to include irrelevant information based solely on the presence of keywords or to miss essential data if the keyword is absent. This will be addressed by expanding the synonym list to refine search accuracy. Moreover, the strategy involves employing lighter models for initial filtering and consolidating content into fewer, larger batches for processing. This approach is expected to keep costs below $1 for extensive searches, making it economically feasible even for large datasets.

## Conclusion

The aim is to establish a retrieval system that is not only more accurate but also more efficient than RAG, focusing on precision and cost-effectiveness. As lightweight LLMs advance, querying vast datasets for minimal costs will likely become more feasible, transforming content retrieval into a more accessible and practical resource across various sectors.
