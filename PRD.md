# Product Requirements Document (PRD): Toronto Condo Investment Assistant

<!-- AI_CONTEXT: HIGH_FIDELITY_INSTRUCTION
This document is the SOURCE OF TRUTH for Business goals.
-->

## 1. Executive Summary
A specialized "Condo Hunter" agent for Toronto investors. It goes beyond basic listings by uncovering "Soft Data" (Views, Renter Ratio), "Future Value" (Transit lines), and "Red Flags" (Status Certificates). Built on **Google Vertex AI Agent Builder**, **Python**, and the **A2A Protocol**.

## 2. Business Intent & Objectives
*   **Strategic Goal**: Automate the due diligence process (Listing -> Deep Dive -> Risk Assessment).
*   **Key Features**:
    *   **Ghost Scraper**: On-demand extraction of Sold History from HouseSigma.
    *   **Status Cert Auditor**: Automated risk detection in PDF status certificates.
    *   **Future Value Mapper**: Proximity analysis to the new Ontario Line.

## 3. Technology Stack
*   **Core**: Python 3.10+
*   **Agent Framework**: Google Vertex AI Agent Development Kit (ADK).
*   **Browser Automation**: `browser-use` / Playwright (for scraping).
*   **PDF Analysis**: `pdfplumber` / `pymupdf`.
*   **Geospatial**: `geopandas` + `folium`.
*   **Models**: Gemini 2.0 Pro.

## 4. Functional Capabilities
| Feature Name | Description | Priority |
| :--- | :--- | :--- |
| **Tool A: Ghost Scraper** | "The Harvester". Visits listing URLs, extracts basic data + rental history. Human-like navigation. | P0 |
| **Tool B: Page Analyst** | "The Deep Dive". Extracts "Soft Criteria" (View, Exposure, Parking) using LLM reasoning on the DOM. | P0 |
| **Tool C: Status Cert Auditor** | "The Risk Checker". Scans uploaded PDFs for keywords (Special Assessment, Kitec, Lawsuit). | P1 |
| **Tool D: Future Value Mapper** | "The Locator". Calculates distance to Ontario Line, **Bike Trails, and Kayak Launch points**. | P1 |

## 5. Data Schema (Pydantic)
The Agent will output data adhering to strict schemas.
*   **Hard Criteria**: `price`, `sqft`, `fees`, `parking_included`.
*   **Soft Criteria**: `exposure` (N/S/E/W), `view_quality` (Lake vs Wall), `renter_ratio_risk`.
*   **Lifestyle**: `dist_to_trail`, `dist_to_water` (Kayak access).
*   **Investment**: `cash_flow_scenario` (Rental), `appreciation_scenario` (Hold).

## 6. Financial Modeling (Dual Scenarios)
*   **Scenario A (Investment/Hold)**: Focus on YoY Appreciation (Assumption: 5%).
*   **Scenario B (Rental)**: Focus on Cash Flow.
    *   *Revenue*: Estimated Rent.
    *   *Expenses*: Mortgage + Tax + Maintenance.

## 7. Non-Functional Requirements
*   **Bot Evasion**: Critical. Scraper must use visual strategies to avoid detection.
*   **Safety**: Agent must perform "Red Flag" checks before recommending any unit.
