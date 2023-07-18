from tkinter import *
import pygame


window = Tk()
window.title("Audio_denoising")
window.geometry("1280x1080")
window.resizable(False,False)
pygame.mixer.init()
# func play,freq_denoise,moving_denoise,spectral_denoise use to play the record
def play():
    pygame.mixer.music.load("test_noise.wav")
    pygame.mixer.music.play(loops= 0)
def freq_denoise():
    pygame.mixer.music.load("freq_flitering.wav")
    pygame.mixer.music.play(loops= 0)
def moving_denoise():
    pygame.mixer.music.load("moving_avg_fliter.wav")
    pygame.mixer.music.play(loops= 0)
def spectral_denoise():
    pygame.mixer.music.load("spectral_sub.wav")
    pygame.mixer.music.play(loops= 0)
# import the 3 files
def freq():
    import freq_filter
def moving():
    import moving_average
    
def spectral():
    import spectral_subtraction
    

myFame = Frame(width= 999, height= 999,bg="#fff") # Make a background better to white color
myFame.pack(fill= BOTH, expand= True)
myLabel = Label(window, text="Audio Denoising",height= 1, font=('bold', 30), border= 10,bg="#fff") # A label for the title
myLabel.place(relx= 0.40, rely= 0.05)
myLabel1 = Label(window, text="Input test_noise wave data:",font= 25,bg="#fff") # A label for the input
myLabel1.place(relx= 0.05,rely= 0.15)

play_button = Button(window, text="Test sound", font= 20,bg="#fff",activebackground="#313131",command=play) # A button for play the test noise
play_button.place(relx= 0.1, rely= 0.20, relheight= 0.05,relwidth=0.2)

myLabel2 = Label(window, text="Option: ",font= 25,bg="#fff") # A label for 3 options
myLabel2.place(relx= 0.05,rely= 0.30)

freq_btn = Button(window, text="Freq filter",font= 20,bg="#fff",activebackground="#313131",command=freq) # A button to show the diagram of freq
freq_btn.place(relx= 0.1, rely= 0.35, relheight= 0.05,relwidth=0.2)

moving_btn = Button(window, text="Moving average",font= 20,bg="#fff",activebackground="#313131",command= moving) # A button to show the diagram of avarage
moving_btn.place(relx= 0.4, rely= 0.35, relheight= 0.05,relwidth=0.2)

spectral_btn = Button(window, text="Spectral subtraction",font= 20,bg="#fff",activebackground="#313131",command= spectral) # A button to show the diagram of subtraction
spectral_btn.place(relx= 0.7, rely= 0.35, relheight= 0.05,relwidth=0.2)


freq_button = Button(window, text="Freq filter sound", font= 20,bg="#fff",activebackground="#313131",command=freq_denoise) # A button to show the diagram of freq sound
freq_button.place(relx= 0.1, rely= 0.45, relheight= 0.05,relwidth=0.2)
moving_button = Button(window, text="Moving avarage sound", font= 20,bg="#fff",activebackground="#313131",command=moving_denoise) # A button to show the diagram of avarage sound
moving_button.place(relx= 0.4, rely= 0.45, relheight= 0.05,relwidth=0.2)
spectral_button = Button(window, text="Specreal subtraction sound", font= 20,bg="#fff",activebackground="#313131",command=spectral_denoise) # A button to show the diagram of subtraction sound
spectral_button.place(relx= 0.7, rely= 0.45, relheight= 0.05,relwidth=0.2)

window.mainloop()