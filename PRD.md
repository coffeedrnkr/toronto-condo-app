# Product Requirements Document (PRD): Toronto Condo Investment Assistant

<!-- AI_CONTEXT: HIGH_FIDELITY_INSTRUCTION
This document is the SOURCE OF TRUTH for Business goals.
-->

## 1. Executive Summary
A specialized application for analyzing Toronto condo investments. Unlike standard real estate apps that focus on "finding a home," this app focuses on "finding a return." It automates the retrieval of hard-to-get data (HouseSigma) and calculates investment viability (Cash Flow, Cap Rate) to filter the noise.

## 2. Business Intent & Objectives
*   **Problem Statement**: Investors waste time manually looking up rental history and calculating cash flow for hundreds of listings.
*   **Strategic Goal**: Leverage Agentic AI to automate data gathering and analysis.
*   **Key Features**:
    *   Find under-valued properties.
    *   Estimate accurate rental income based on *actual* leased data.
    *   Automate HouseSigma interaction (Login, Search, Scrape).

## 3. Functional Capabilities
| Feature Name | Description | Priority |
| :--- | :--- | :--- |
| **HouseSigma Scraper** | Browser agent navigates HouseSigma, handles login, and scrapes Sold/Leased data. | P0 |
| **Cash Flow Calculator** | Auto-calculate Monthly Cashflow (Rent - Expenses). | P0 |
| **Cap Rate Analyzer** | Calculate NOI / Purchase Price. Visualize heatmaps of high-yield areas. | P1 |
| **Agent Manager** | User dashboard to trigger scraping tasks and view "Agent Activity" (videos/logs). | P2 |

## 4. Cash Flow Logic (To Be Decided)
> [!WARNING]
> **Pending Decision**: Which formula to use?
> *   **Option A (Conservative)**: `Rent*0.95` (Vacancy) - `Mortgage` - `Tax` - `Maint*1.1` (Buffer) - `MgmtFee(8%)`
> *   **Option B (Simple)**: `Rent` - `Mortgage` - `Tax` - `Maint`

## 5. HouseSigma Integration (Browser Agent)
*   The system will use a **Browser Subagent** to interact with `housesigma.com`.
*   **Trigger**: User defines criteria (e.g., "Liberty Village, 1BR, <$600k") or schedules a "Daily Morning Scan".
*   **Output**: Structured JSON of listings linked to their rental history.

## 6. Non-Functional Requirements
*   **Bot Evasion**: Scraper must act human-like to avoid IP bans.
*   **Artifacts**: All scraping runs must produce a video artifact for verification.
