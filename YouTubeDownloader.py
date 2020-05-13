import pafy 

prompt = "\t>> "

def main():
    print("Welcome to YouTubeDownloder !!")

    url = input("\n[+] Please enter your url: " + prompt)
    video = pafy.new(url)
    print(video.title)
    
    choice = input("\n[+] Download as: (vid | audio | vidPly\n" + prompt)

    if choice == "vid":
        vid(url)
    elif choice == "audio":
        audio(url)
    elif choice == "vidPly":
        vid_pl(url)
    else:
        print("[-] Please specify one the available options !!!")


def vid(url):
    video = pafy.new(url)
    best = video.getbest()
    best.download(filepath=".", quiet=False)

def audio(url):
    audio = pafy.new(url)
    best = audio.getbestaudio()
    best.download(filepath=".", quiet=False)

def vid_pl(url):
    playlist = pafy.get_playlist(url)
    for i in playlist["items"]:
        best_v = i["pafy"].getbest()
        best_v.download(filepath=".", quiet=False)

main()
