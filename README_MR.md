

## **FINDER Tool (शोध Tool)**

**FINDER** (शोध) हे Javascrript फायलींमधून संवेदनशील माहिती जसे की API कीज, टोकन्स आणि गुप्त माहिती शोधण्यासाठी डिझाइन केलेले एक पायथन आधारित साधन आहे. हे दिलेल्या URL वरून जावास्क्रिप्ट फायली काढते, त्यांचे विश्लेषण करते आणि सविस्तर अहवाल तयार करते.

---

### **वैशिष्ट्ये**

1. **संवेदनशील माहितीचा शोध**:
   - API कीज, टोकन्स आणि गुप्त माहिती शोधण्यासाठी regex पॅटर्न वापरते.
   - Google API कीज, Firebase टोकन्स, CAPTCHA कीज शोधण्यासाठी समर्थन.

2. **संवेदनशील डेटाची पडताळणी**:
   - Gemini API सारख्या बाह्य API च्या मदतीने संवेदनशील डेटाची पडताळणी.
   - योग्य आणि अयोग्य निकाल वेगळे करून तपशीलवार माहिती प्रदान.

3. **डायनॅमिक अहवाल**:
   - **Raw Output**: सर्व शोध, वैध आणि अयोग्य निकाल श्रेणीबद्ध.
   - **Structured Reports**: परिणाम सोप्या स्वरूपात, फाइल स्रोतांसह आणि AI द्वारे स्पष्टीकरण.

4. **टर्मिनलवर परस्पर क्रिया**:
   - झटपट प्रतिसादासाठी परिणाम टर्मिनलवर दर्शवते.
   - त्वरित पुनरावलोकनासाठी पडताळलेल्या गुप्त माहितीचे प्रिंट.

5. **वापरकर्ता-अनुकूल अनुभव**:
   - सुरुवातीस एक आकर्षक साधन बॅनर दाखवते.
   - स्कॅनिंग प्रगती सूचित करण्यासाठी सतत ध्वनी प्रतिक्रिया.

---

### **सेटअप**

1. **आवश्यक सॉफ्टवेअर इन्स्टॉल करा**:
   - Python 3.7+ इन्स्टॉल करा.
   - आवश्यक Python लायब्ररी इन्स्टॉल करा:
     ```bash
     pip install playwright requests google-generativeai cryptography
     ```
   - Playwright साठी dependencies सेट करा:
     ```bash
     playwright install
     ```

2. **साधन चालवा**:
   - स्क्रिप्ट `finder.py` म्हणून सेव्ह करा.
   - साधन चालवा:
     ```bash
     python finder.py 
     ```
   

---

### **कार्य कसे करते**

1. **Javascript files काढणे**:
   - Playwright च्या मदतीने वेबपेज लोड करते आणि जावास्क्रिप्ट फायली काढते.

2. **Regex आधारित गुप्त माहितीचा शोध**:
   - API कीज, टोकन्स, आणि गुप्त माहिती शोधण्यासाठी फायली स्कॅन करते.

3. **पडताळणी**:
   - Gemini API चा वापर करून संवेदनशील डेटाची पडताळणी.
   - "वैध" आणि "अवैध" निकाल वर्गीकृत करते.

4. **अहवाल तयार करणे**:
   - `raw_output.txt` नावाचा फाईल तयार करते ज्यामध्ये सर्व निष्कर्ष समाविष्ट.
   - `structured_report.txt` तयार करते ज्यामध्ये वैध निष्कर्ष आणि स्पष्टीकरण असतात.
   - Eth  tumhi tumachi gemini chi API key use kara, API key free aahe. Only for the sturctured output report.

---

### **उदाहरण report**

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

---

### **परवाना**
हे साधन मुक्त स्रोत आहे .
