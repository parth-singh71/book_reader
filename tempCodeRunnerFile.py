from google_speech import Speech
import speech_recognition as sr
import PyPDF2 as Pdf


class BookReader:
    def __init__(self, filename):
        self.filename = filename

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

    def play_pdf(self):
        file = open(self.filename, "rb")
        pdf_reader = Pdf.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for i in range(0, num_pages):
            speak(get_page_text(file, pdf_reader, i))
            if (i + 1) is not num_pages:
                speak(
                    f". Page {i} is over. Do you wat me to continue to Page {i+1}?")
                user_input = self.listen()
                if user_input in ['yeah', 'yes', 'yup', 'ofcourse', 'sure']:
                    continue
                elif user_input in ['no', 'never', 'nope', 'nah']:
                    speak("Thankyou for using me! Bye and have a good day.")
                    break
            else:
                speak(f". Congratulations you have listened to the whole book.")
        file.close()


book_reader = BookReader("book.pdf")
book_reader.play_pdf()
# play_pdf("book.pdf")
