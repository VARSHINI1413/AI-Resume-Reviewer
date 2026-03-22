# Step 2: Import libraries
import PyPDF2
from sentence_transformers import SentenceTransformer, util
import gradio as gr

# Step 3: Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight, fast

# Step 4: Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text

# Step 5: Function to extract skills from job description
def extract_skills(job_text):
    # Very simple: split by commas and newlines
    skills = [skill.strip() for skill in job_text.replace("\n",",").split(",") if skill.strip()]
    return skills

# Step 6: Function to compare resume with job skills
def check_resume(resume_text, job_skills):
    resume_text = resume_text.lower()
    missing_skills = []

    for skill in job_skills:
        score = util.cos_sim(model.encode(skill.lower()), model.encode(resume_text))
        if score.item() < 0.4:  # threshold for missing skill
            missing_skills.append(skill)

    match_score = round((1 - len(missing_skills)/len(job_skills)) * 100, 2)
    result = f"Match Score: {match_score}%\nMissing Skills: {', '.join(missing_skills) if missing_skills else 'None'}"
    return result

# Step 7: Function for Gradio UI
def analyze_resume(resume_file, job_file):
    resume_text = extract_text_from_pdf(resume_file.name)
    job_text = extract_text_from_pdf(job_file.name)
    job_skills = extract_skills(job_text)
    return check_resume(resume_text, job_skills)

# Step 8: Build interactive Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## AI Resume Reviewer\nUpload your Resume and Job Description (PDF)")
    with gr.Row():
        resume_upload = gr.File(label="Upload Resume (PDF)")
        job_upload = gr.File(label="Upload Job Description (PDF)")
    output = gr.Textbox(label="Analysis Result", lines=5)
    btn = gr.Button("Check Resume")
    btn.click(analyze_resume, inputs=[resume_upload, job_upload], outputs=output)

demo.launch()
