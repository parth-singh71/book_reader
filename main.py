from google_speech import Speech
import speech_recognition as sr
import PyPDF2 as Pdf
import argparse

# python main.py --pdf 'pdf_name.pdf' --single --page 0
# python main.py --pdf 'pdf_name.pdf' --multi --from_page 8

class BookReader:
    def __init__(self, filename, from_page=0):
        self.filename = filename
        self.from_page = from_page

    def speak(self, text, language="en"):
        speech = Speech(text, language)
        speech.play()

    def listen(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                return text
        except sr.RequestError as e:
            return e
        except sr.UnknownValueError as e:
            return e

    def get_page_text(self, file, reader, page_no):
        page = reader.getPage(page_no)
        result = page.extractText()
        return result

    def play_page(self, page):
        file = open(self.filename, "rb")
        pdf_reader = Pdf.PdfFileReader(file)
        self.speak(self.get_page_text(file, pdf_reader, page))
        self.speak(
            f". Congratulations you have successfully listened to Page number {page}.")
        self.speak("Thankyou for using me! Bye and have a good day.")

    def play_pdf(self):
        file = open(self.filename, "rb")
        pdf_reader = Pdf.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for i in range(self.from_page, num_pages):
            self.speak(self.get_page_text(file, pdf_reader, i))
            if (i + 1) is not num_pages:
                self.speak(
                    f". Page {i} is over. Do you wat me to continue to Page {i+1}?")
                user_input = self.listen()
                if user_input in ['yeah', 'yes', 'yup', 'ofcourse', 'sure']:
                    continue
                elif user_input in ['no', 'never', 'nope', 'nah']:
                    self.speak(
                        "Thankyou for using me! Bye and have a good day.")
                    break
            else:
                self.speak(
                    f". Congratulations you have listened to the whole book.")
        file.close()


parser = argparse.ArgumentParser(description='Listen to your books in style!')
parser.add_argument('--pdf', dest='pdf', type=str,
                    help='PDF File Path', required=True)
parser.add_argument('--from_page', dest='from_page',
                    type=int, help='From which page number')
parser.add_argument('--page', dest='page', type=int, help='Read sinple page')
parser.add_argument('-single', '--single', action='store_true')
parser.add_argument('-multi', '--multi', action='store_true')

args = parser.parse_args()
filepath = args.pdf
from_page = args.from_page
read_single_page = args.single
read_multiple_page = args.multi
page = args.page

book_reader = BookReader(filepath, from_page if from_page else 0)
if read_single_page:
    book_reader.play_page(page=page)
elif read_multiple_page:
    book_reader.play_pdf()
