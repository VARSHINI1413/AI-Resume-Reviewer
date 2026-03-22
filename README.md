# 📄 AI Resume Reviewer

An AI-powered web app that compares your resume against a job description and gives you a **match score** along with the **missing skills** — helping you tailor your resume better for any job!

🚀 **Live Demo:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Varshini1406/AI-Resume-Reviewer)

---

## ✨ Features

- 📤 Upload your **Resume** as a PDF
- 📋 Upload the **Job Description** as a PDF
- 🤖 Uses **Sentence Transformers** (AI) to semantically compare skills
- 📊 Get a **Match Score (%)** instantly
- ❌ See exactly which **skills are missing** from your resume

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Gradio | Web UI |
| Sentence Transformers (`all-MiniLM-L6-v2`) | Semantic similarity |
| PyPDF2 | PDF text extraction |
| Hugging Face Spaces | Deployment |

---

## ⚙️ How It Works

1. Both PDFs are uploaded and text is extracted using **PyPDF2**
2. Skills are parsed from the job description
3. Each skill is compared to the resume using **cosine similarity**
4. A match score is calculated based on how many skills are found

---

## 🚀 Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Reviewer.git
cd AI-Resume-Reviewer
pip install -r requirements.txt
python app.py
```

---

## 🙋‍♀️ Author

**Varshini** — [Hugging Face Profile](https://huggingface.co/Varshini1406)
