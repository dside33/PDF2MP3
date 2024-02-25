import pdfplumber
import os
from gtts import gTTS
from art import *
import asyncio


LANG = ("ru", "en")


async def convert_text_2_mp3(pdf_path, lang="ru")-> bool:
    if os.path.isfile(pdf_path) == False:
        return False
    
    pdf_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text()

    pdf_text = pdf_text.replace('\n', '')

    tprint("PDF2MP3", font="bulbhead")
    print("[+]...loading...")

    audio = gTTS(text=pdf_text, lang=lang, slow=False)
    audio.save("example.mp3")

    print("[+] success!")

    return True


async def main():
    file_path = input("Enter file path: ")
    language = input(f"Enter lang ({', '.join(LANG)}): ")

    await convert_text_2_mp3(file_path, language)

if __name__ == "__main__":
    asyncio.run(main())
    # convert_text_2_mp3("Iskusstvo_Geymdizayna_Shell-1-2.pdf")
