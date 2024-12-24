
## Switch Language
- [English](README_EN.md)
- [मराठी](README_MR.md)
## **FINDER Tool**

**FINDER** is a Python-based tool designed to identify sensitive data such as API keys, tokens, and other secrets in JavaScript files of web applications. It extracts JavaScript files from a given URL, scans them using predefined patterns, validates sensitive data, and generates detailed reports for further analysis.

---

### **Features**

1. **Sensitive Information Detection**:
   - Finds API keys, tokens, and other secrets using regex patterns.
   - Supports detection of Google API keys, Firebase tokens, CAPTCHA keys, and more.
   
2. **Validation of Sensitive Data**:
   - Validates sensitive keys using external APIs like the Gemini API.
   - Differentiates between valid and invalid matches for better insights.

3. **Dynamic Reports**:
   - **Raw Output**: Includes all findings, categorized into valid and invalid matches.
   - **Structured Reports**: Summarizes results in an easy-to-read format, including file sources and AI-generated explanations.

4. **Interactive Terminal Output**:
   - Displays results in the terminal for immediate feedback.
   - Prints validated secrets for quick review.

5. **User-Friendly Experience**:
   - Shows a visually appealing tool banner during initialization.
   - Provides continuous sound feedback to indicate scanning progress.

---

### **Setup**

1. **Install Dependencies**:
   - Install Python 3.7+.
   - Install required Python libraries:
     ```bash
     pip install playwright requests google-generativeai cryptography google.generativeai boto3 stripe
     ```
   - Set up Playwright dependencies:
     ```bash
     playwright install
     ```

2. **Run the Tool**:
   - Save the script as `finder.py`.
   - Run the tool:
     ```bash
     python finder.py
     ```
   

---

### **How It Works**

1. **JavaScript File Extraction**:
   - Uses Playwright to dynamically load the webpage and extract JavaScript files.

2. **Regex-Based Secret Detection**:
   - Scans JavaScript files for patterns like API keys, tokens, and secrets.

3. **Validation**:
   - Uses Gemini API (or similar services) to validate sensitive keys.
   - Categorizes matches as "valid" or "invalid."

4. **Reporting**:
   - Generates a `raw_output.txt` file containing all findings.
   - Creates a structured `structured_report.txt` with validated matches and explanations.

---

### **Example Reports**

#### Raw Output (`raw_output.txt`):
```
--- VALID MATCHES ---
AIzaSyExampleValidKey (Source: https://example.com/script.js)

--- INVALID MATCHES ---
InvalidKey12345 (Source: https://example.com/script.js)
```

#### Structured Report (`structured_report.txt`):
```
PENTESTING REPORT
=================
--- Google API Key ---
Status: Valid
Details: Verified as a valid Google API key.
Source Files:
  - https://example.com/script.js
```
You can use your gemini api keys for the structured output , otherwise raw output will be save on your current directory.

---
This tool is open-source. Open for the contribution.
### **License**
This tool is open-source and available under the MIT License.

---

