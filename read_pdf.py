import sys
import subprocess

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('PyPDF2')

try:
    reader = PyPDF2.PdfReader('d:/Me/Portfolio-main/resume.pdf')
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open('d:/Me/Portfolio-main/resume_text.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Success")
except Exception as e:
    print("Error:", e)
