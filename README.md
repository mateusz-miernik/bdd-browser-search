# Search Automation Tests (Google & Bing)

This project contains **BDD test cases** for searching on Google and Bing,  
implemented in **Python + Behave + Playwright** using the Page Object Model (POM).

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/mateusz-miernik/bdd-browser-search.git
cd bdd-browser-search
```

### 2. Install dependencies
Make sure you are using **Python 3.9+** and have a virtual environment activated.

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers
Playwright requires browser binaries (Chromium, Firefox, WebKit).

```bash
playwright install
```

---

## Running Tests

### Run all tests
```bash
behave
```

### Run only Google tests
```bash
behave features/google_search.feature
```

### Run only Bing tests
```bash
behave features/bing_search.feature
```

---

## Tech Stack
- **Python** – Programming language
- **Behave** – BDD framework
- **Playwright** – Browser automation
- **Page Object Model (POM)** – Test design pattern

---

## Notes
- Default browser is **Firefox** (headless).  
- Update `environment.py` if you want to run tests in **headed mode** or with **Chrominium/WebKit**.  
- Reports can be generated using **Allure** or other plugins if needed.
