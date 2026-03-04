from PyPDF2 import PdfReader
import docx
from io import BytesIO

async def extract_text_from_upload(file) -> str:
    filename = file.filename.lower()
    file_bytes = await file.read()

    # TXT
    if filename.endswith(".txt"):
        return file_bytes.decode("utf-8")

    # PDF
    elif filename.endswith(".pdf"):
        reader = PdfReader(BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    # DOCX
    elif filename.endswith(".docx"):
        document = docx.Document(BytesIO(file_bytes))
        return "\n".join([para.text for para in document.paragraphs])

    else:
        raise Exception("Unsupported file type. Only TXT, PDF, DOCX allowed.")