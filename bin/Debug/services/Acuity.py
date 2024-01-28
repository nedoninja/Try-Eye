import speech_recognition
import webbrowser

def responseF():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    with speech_recognition.Microphone() as mk:
        sr.adjust_for_ambient_noise(source=mk, duration=0.5)
        audio = sr.listen(source = mk)
        responce = sr.recognize_google(audio_data=audio, language="ru-RU")
    return list(str(responce).replace(" ", ""))

def run_brows(path):
    webbrowser.open(path,new=2)

def main():
    run_brows("services\\Doc\\table.pdf")
    res = responseF()
    ostr = {
        0.4 : "бынкм", #5, 1-5
        0.5 : "иншмк", #5 6 - 10
        0.6 : "ншыикб", #6 11 - 16
        0.7 : "шинбкы", #6 17 - 22
        0.8 : "кншмыби", #7 23 - 29
        0.9 : "бкшмиын", #7 30 - 36
        1.0 : "нкибмшыб", #8 37 - 44
        1.5 : "шинкмиыб", #8 45 - 52
    } #52 + 12 = 64

    opt = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5]
    c = 0
    error = 0
    st = ""
    for key in ostr.keys():
        st += ostr[key]

    for i in range(len(res)):
        if res[i] == "н" and res[i+1] == 'е':
            break

        if res[i] != st[i]:
            error += 1

        if i in [5, 10, 16, 22, 29, 36, 44]:
            c += 1
    s = ""
    if opt[c] == 1.0 and error <= 4:
        s = "perfectly"
    elif opt[c] == 1.0 and error >= 4:
        s = "myopia"
    elif opt[c] > 1.5:
        s = "farsightedness"
    elif opt[c] < 1:
        s = "myopia"

    f = open("services\\acuity.txt", "w", encoding="utf")
    f.write(f"{s}, { opt[c]} - acuity")
    f.close()
    print("значение записано в acuity.txt")

if __name__ == "__main__":
    main()