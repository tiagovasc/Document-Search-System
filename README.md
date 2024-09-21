## Overview

This project is designed to meticulously extract relevant textual content from Epub documents based on specific keyword searches. It caters to users needing to sift through large volumes of text and retrieve contextually relevant information efficiently. This solution is particularly suited for academic researchers, data scientists, and professionals who manage large databases of digital books and documents.

The core functionality revolves around the ability to identify and extract not just the paragraphs containing specific keywords but also the contextual surroundings of those paragraphs. This approach ensures that the extracted text is meaningful and retains the necessary context, making it immediately useful for content analysis or further processing.

The method leverages traditional keyword search techniques, which, while straightforward, are enhanced by strategic processing to ensure that the text retrieval is as relevant as possible. This project stands out by focusing on creating a highly targeted retrieval system that prioritizes precision and relevance over sheer data volume processing, addressing common pitfalls found in more generalized content retrieval systems like RAG (Retrieval-Augmented Generation).

## How It Works

The project operates through several sequential steps, each designed to ensure the accuracy and relevance of the text retrieved from Epub documents:

1. **Keyword Definition**:
   - Users start by defining a set of keywords that are of interest to their research or analysis needs. These keywords can be easily adjusted in the script to accommodate different topics or areas of focus.

2. **Document Parsing**:
   - The script reads an Epub file, leveraging `ebooklib` and `BeautifulSoup` to parse its HTML content. This parsing step is crucial as it structures the content into a format that can be easily searched.

3. **Keyword Search and Context Extraction**:
   - For each keyword, the script searches through the structured text to find all instances where the keyword appears.
   - It doesn’t just extract the paragraph containing the keyword but also the paragraphs immediately before and after it. This inclusion of adjacent paragraphs helps preserve the context, making the retrieved information more useful.

4. **Relevance Filtering**:
   - To enhance the relevance of the extracted text, the script applies a minimum word count threshold. Sections that do not meet this threshold are considered too brief to provide valuable context and are thus excluded.

5. **Combination and Deduplication**:
   - If consecutive text extracts overlap or are contiguous, they are combined into a single section to avoid redundancy. This step ensures that the output is concise and non-repetitive.

6. **Output**:
   - Finally, the script summarizes the findings before displaying the extracted text. It provides counts of the total extracted sections and those combined due to overlap for each keyword. This summary gives a quick overview of the content size and density related to each keyword.

By following these steps, the script ensures that only the most relevant and contextually rich sections are retrieved from vast amounts of Epub content, addressing common challenges in large-scale text analysis.

## Motivation
This project was developed as an alternative to Retrieval-Augmented Generation (RAG), which, despite its widespread use, is imperfect for large-scale data retrieval. RAG often struggles with extensive datasets, typically missing crucial information. This project enhances precision by initiating content selection based on specific keywords. Currently, it outputs relevant text sections directly without further processing.

## Future Plans
The project's current stage successfully extracts text where keywords are mentioned but may include sections not entirely pertinent to the search intent. The next development phase will integrate a Language Model (LLM) to assess the relevance of each text section. This will refine the content database to include only those sections that are truly relevant, which can then be used for detailed analysis or further processed for summaries, categorization, or organization. This approach faces challenges, particularly with the potential volume of outputs—around 100 desired outputs from 1000 pages can result. Addressing this, I plan to utilize more cost-effective models and batch several sections into a single API call to reduce expenses and processing times.

## Limitations & Solutions
The primary limitation lies in the retrieval method's tendency to fetch non-relevant information solely based on keyword presence or to miss crucial data if the keyword is absent. This will be mitigated by expanding the synonym list, although this may initially increase noise. To manage the cost and efficiency, the approach involves using cheaper, lighter models for preliminary filtering and aggregating content into fewer, larger batches for processing. This strategy should keep costs under $1 for extensive searches, making it economically viable even for large datasets.

## Conclusion
This project aims to establish a highly accurate retrieval system that fundamentally differs from and potentially outperforms RAG by focusing on efficiency and precision. As lightweight LLMs improve, the feasibility of querying vast datasets for minimal costs will transform content retrieval into a more accessible and practical tool across various sectors.

