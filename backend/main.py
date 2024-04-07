from Analyzer import imageAnalysis
from Drafter_writers import DraftWriter
from mail_sender import GmailSender
def run(img):
    result = imageAnalysis(img).invoke("Analyse customer comments,focus on product comments.")
    with open("vistion.txt", "w") as file:
        file.write(result)
    result = DraftWriter().launcher(result)
    GmailSender(result["Topic"],result["Summary"],result["Rating"])
