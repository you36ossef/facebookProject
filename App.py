from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import mysql.connector

my_dp = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="facebook"
)
cursor = my_dp.cursor()

def get_window():
    window = Tk()
    window.title("facebook lite")
    window.iconbitmap("res\\facebook_icon.ico")
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    window.geometry(f"{screen_width - 10}x{screen_height - 80}+0+0")
    window.minsize(500, 500)
    # window.state("zoomed")
    # window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    window.withdraw()
    return window

def startWindow():
    start_window = get_window()
    start_window.configure(bg="darkblue")
    welcome = Label(start_window,text="Welcome to facebook lite.", bg="darkblue", fg="white", font=("Helvetica", 20) )
    welcome.place(x=600 - 50, y=100)

    def c1():
        login_window.deiconify()
        start_window.withdraw()

    sign_in = Button(start_window, command = c1, text="Sign in", bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    sign_in.place(x=630, y=200)

    def c2():
        register_window.deiconify()
        start_window.withdraw()

    sign_up = Button(start_window, text="Sign up", command=c2, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    sign_up.place(x=630, y=250)
    return start_window


def loginWindow():
    login_window = get_window()
    login_window.configure(bg="darkblue")
    welcome = Label(login_window, text="facebook lite", bg="darkblue", fg="white", font=("Helvetica", 20))
    welcome.place(x=600, y=100)
    
    username = Label(login_window, text="username:", bg="darkblue", fg="white", font=("Helvetica", 16))
    username.place(x=500 - 50, y=150)
    password = Label(login_window, text="password:", bg="darkblue", fg="white", font=("Helvetica", 16))
    password.place(x=500 - 50, y=200)
    
    usernametb = Entry(login_window, font=("Helvetica", 16))
    usernametb.place(x=600 - 10, y=150)
    passwordtb = Entry(login_window, font=("Helvetica", 16))
    passwordtb.place(x=600 - 10, y=200)
    
    def c1():
        profile_window.deiconify()
        login_window.withdraw()

    sign_in = Button(login_window, text="Sign in", command=c1, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    sign_in.place(x=630 + 50, y=300)

    def c2():
        start_window.deiconify()
        login_window.withdraw()
        
    back = Button(login_window, text="back", command=c2, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    back.place(x=530 - 50, y=300)
    return login_window

def registerWindow():
    register_window = get_window()
    register_window.configure(bg="darkblue")
    welcome = Label(register_window, text="facebook lite", bg="darkblue", fg="white", font=("Helvetica", 20))
    welcome.place(x=600, y=100)
    
    username = Label(register_window, text="username:", bg="darkblue", fg="white", font=("Helvetica", 16))
    username.place(x=500 - 100, y=150)
    gmail = Label(register_window, text="gmail:", bg="darkblue", fg="white", font=("Helvetica", 16))
    gmail.place(x=500 - 100, y=200)
    password = Label(register_window, text="password:", bg="darkblue", fg="white", font=("Helvetica", 16))
    password.place(x=500 - 100, y=250)
    comfirm = Label(register_window, text="confirm password:", bg="darkblue", fg="white", font=("Helvetica", 16))
    comfirm.place(x=500 - 100, y=300)
    
    usernametb = Entry(register_window, font=("Helvetica", 16))
    usernametb.place(x=600, y=150)
    gmailtb = Entry(register_window, font=("Helvetica", 16))
    gmailtb.place(x=600, y=200)
    passwordtb = Entry(register_window, font=("Helvetica", 16))
    passwordtb.place(x=600, y=250)
    confirmtb = Entry(register_window, font=("Helvetica", 16))
    confirmtb.place(x=600, y=300)

    def c1():
        verify_window.deiconify()
        register_window.withdraw()
        
    sign_up = Button(register_window, text="Sign up", command=c1, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    sign_up.place(x=630 + 50, y=380)

    def c2():
        start_window.deiconify()
        register_window.withdraw()
    back = Button(register_window, text="back", command=c2, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    back.place(x=530 - 50 - 40, y=380)
    return register_window

def verifyWindow():
    verify_window = get_window()
    verify_window.configure(bg="darkblue")
    
    verify = Label(verify_window, text="enter the verification code sent to your email:", bg="darkblue", fg="white", font=("Helvetica", 20))
    verify.place(x=100, y=100)
    
    verfytb = Entry(verify_window, font=("Helvetica", 16))
    verfytb.place(x=700, y=100)

    def c1():
        profile_window.deiconify()
        verify_window.withdraw()
    verifyb = Button(verify_window, text="verify", command=c1, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    verifyb.place(x=600, y=200)

    return verify_window

def profileWindow(Pstate):
    profile_window = get_window()
    profile_window.configure(bg="darkblue")

    # Create a canvas
    canvas = Canvas(profile_window, bg="darkblue")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar
    scrollbar = Scrollbar(profile_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas
    frame = Frame(canvas, bg="darkblue")
    canvas.create_window((0, 0), window=frame, anchor="nw")
    
    # Scroll function
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Bind the mouse wheel event to the scroll function
    profile_window.bind_all("<MouseWheel>", on_mousewheel)

    def c1():
        profile_window.withdraw()
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()

    profileb = Button(frame, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()
        profile_window.withdraw()

    timelineb = Button(frame, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        profile_window.withdraw()

    searchb = Button(frame, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        profile_window.withdraw()

    settingsb = Button(frame, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)

    tk_image = ImageTk.PhotoImage(Image.open("res\\male_pic.png"), master=profile_window)
    pic = Label(frame, height=320, width=320, image=tk_image, bg="darkblue")
    pic.image = tk_image
    pic.grid(row=1, column=0, pady=25, rowspan=4)

    user = Label(frame, text="UserName", bg="darkblue", fg="white", font=("Helvetica", 16))
    user.grid(row=5, column=0, padx=35, pady=20, sticky='w')

    phone = Label(frame, text="Phone Number: 01061349348", bg="darkblue", fg="white", font=("Helvetica", 16))
    phone.grid(row=1, column=1, padx=10, pady=0, sticky='ws')

    gender = Label(frame, text="Gender: mohandes", bg="darkblue", fg="white", font=("Helvetica", 16))
    gender.grid(row=2, column=1, padx=10, pady=0, sticky='ws')

    birthday = Label(frame, text="BirthDay: 16-12-2004", bg="darkblue", fg="white", font=("Helvetica", 16))
    birthday.grid(row=3, column=1, padx=10, pady=0, sticky='ws')

    education = Label(frame, text="Education: Bfci", bg="darkblue", fg="white", font=("Helvetica", 16))
    education.grid(row=4, column=1, padx=10, pady=0, sticky='ws')

    follower = Combobox(frame)
    follower.grid(row=1, column=3, padx=10, pady=10, sticky='w')

    following = Combobox(frame)
    following.grid(row=1, column=2, padx=10, pady=10, sticky='w')

    def c5():
        post_window.deiconify()
        profile_window.withdraw()

    create_post = Button(frame, text=Pstate, command=c5, bg="darkblue", fg="white", height=1, width=20, font=("Helvetica", 16))
    create_post.grid(row=6, column=0, padx=50, pady=0, sticky='nw', columnspan=2)

    for i in range(10):
        usr = Label(frame, text="UserName . 7-29-2024", bg="darkblue", fg="white", font=("Helvetica", 16))
        usr.grid(row=7 + i*3, column=0, padx=400, pady=0, sticky='w', columnspan=4)
        post = Label(frame, text="first post!!", height=10, width=100, bg="lightgray")
        post.grid(row=8 + i*3, column=0, padx=400, pady=0, sticky='w', columnspan=4)
        
        love = Button(frame, text = "Love", bg = "darkblue", fg = "white", height = 1, width = 15, font = ("Helvetica", 7))
        def change_color(e):
            if e.cget('bg') == 'red':
                e.configure(bg='darkblue')
            else:
                e.configure(bg='red')
        love.configure(command=lambda e=love:  change_color(e))
        love.grid(row=9 + i*3, column=0, padx=400, pady=0, sticky='w', columnspan=4)
        
        react = Label(frame, text = "0", bg = "black", fg = "white", font = ("Helvetica", 7))
        react.grid(row=9 + i*3, column=0, padx=500, pady=0, sticky='w', columnspan=4)

    return profile_window

def timelineWindow():
    timeline_window = get_window()
    timeline_window.configure(bg="darkblue")

    # Create a canvas
    canvas = Canvas(timeline_window, bg="darkblue")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar
    scrollbar = Scrollbar(timeline_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas
    frame = Frame(canvas, bg="darkblue")
    canvas.create_window((0, 0), window=frame, anchor="nw")
    
    # Scroll function
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Bind the mouse wheel event to the scroll function
    timeline_window.bind_all("<MouseWheel>", on_mousewheel)

    def c1():
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()
        timeline_window.withdraw()

    profileb = Button(frame, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.withdraw()
        timeline_window.deiconify()       

    timelineb = Button(frame, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        timeline_window.withdraw()

    searchb = Button(frame, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        timeline_window.withdraw()

    settingsb = Button(frame, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)

    for i in range(10):
        usr = Label(frame, text="UserName . 7-29-2024", bg="darkblue", fg="white", font=("Helvetica", 16))
        usr.grid(row=7 + i*3, column=0, padx=400, pady=0, sticky='w', columnspan=4)
        post = Label(frame, text="first post!!", height=10, width=100, bg="lightgray")
        post.grid(row=8 + i*3, column=0, padx=400, pady=0, sticky='w', columnspan=4)
        
        love = Button(frame, text = "Love", bg = "darkblue", fg = "white", height = 1, width = 15, font = ("Helvetica", 7))
        def change_color(e):
            if e.cget('bg') == 'red':
                e.configure(bg='darkblue')
            else:
                e.configure(bg='red')
        love.configure(command=lambda e=love:  change_color(e))
        love.grid(row=9 + i*3, column=0, padx=400, pady=0, sticky='w', columnspan=4)
        react = Label(frame, text = "0", bg = "black", fg = "white", font = ("Helvetica", 7))
        react.grid(row=9 + i*3, column=0, padx=500, pady=0, sticky='w', columnspan=4)

    return timeline_window

def postWindow():
    post_window = get_window()
    post_window.configure(bg="darkblue")

    def c1():
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()
        post_window.withdraw()

    profileb = Button(post_window, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()  
        post_window.withdraw()

    timelineb = Button(post_window, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        post_window.withdraw()

    searchb = Button(post_window, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        post_window.withdraw()

    settingsb = Button(post_window, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)

    posttb = Entry(post_window, font=("Helvetica", 16),width=90)
    posttb.place(x=250, y=150)
    
    postB = Button(post_window, text="post",bg="darkblue",fg="white", font=("Helvetica", 16))
    postB.place(x = 1200, y = 650)
    return post_window

def settingWindow():
    setting_window = get_window()
    setting_window.configure(bg="darkblue")

    def c1():
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()
        setting_window.withdraw()

    profileb = Button(setting_window, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()  
        setting_window.withdraw()

    timelineb = Button(setting_window, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        setting_window.withdraw()

    searchb = Button(setting_window, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.withdraw()
        setting_window.deiconify()

    settingsb = Button(setting_window, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)

    def c5():
        changeUsr_window.deiconify()
        setting_window.withdraw()
        
    changeUser = Button(setting_window,command=c5, text="Change username",bg="darkblue",fg="white",width=31, font=("Helvetica", 16))
    changeUser.place(x=500, y=100)
    
    def c6():
        changeImage_window.deiconify()
        setting_window.withdraw()
    
    changepi = Button(setting_window,  command=c6, text="Change profile image", bg="darkblue", fg="white", width=31, font=("Helvetica", 16))
    changepi.place(x=500, y=200)
    def c7():
        editInfo_window.deiconify()
        setting_window.withdraw()

    editinfo = Button(setting_window,command=c7, text="Edit profile info",bg="darkblue",fg="white",width=31, font=("Helvetica", 16))
    editinfo.place(x=500, y=300)
    
    deleteaccount = Button(setting_window, text="Delete account",bg="darkblue",fg="white",width=31, font=("Helvetica", 16))
    deleteaccount.place(x=500, y=400)
    
    logout = Button(setting_window, text="log out",bg="darkblue",fg="white",width=31, font=("Helvetica", 16))
    logout.place(x=500, y=500)

    return setting_window

def searchWindow():
    search_window = get_window()
    search_window.configure(bg="darkblue")
    
    # Create a canvas
    canvas = Canvas(search_window, bg="darkblue")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar
    scrollbar = Scrollbar(
        search_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas
    frame = Frame(canvas, bg="darkblue")
    canvas.create_window((0, 0), window=frame, anchor="nw")
    
    # Scroll function
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Bind the mouse wheel event to the scroll function
    search_window.bind_all("<MouseWheel>", on_mousewheel)

    def c1():
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()
        search_window.withdraw()

    profileb = Button(frame, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()  
        search_window.withdraw()

    timelineb = Button(frame, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.withdraw()
        search_window.deiconify()

    searchb = Button(frame, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        search_window.withdraw()

    settingsb = Button(frame, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)

    posttb = Entry(frame, font=("Helvetica", 16), width=30)
    posttb.grid(row=1, column=1,pady=50, sticky="se")

    def c5():
        for i in range(30):
            usr = Label(frame, text="UserName", bg="darkblue", fg="white", font=("Helvetica", 16))
            usr.grid(row=7 + i*2, column=0, padx=400, pady=0, sticky='w', columnspan=4)

            profile = Button(frame, text = "View profile", bg = "darkblue", fg = "white", height = 1, width = 15, font = ("Helvetica", 7))
            def c(e):
                # profile_window = profileWindow("Follow")
                profile_window.deiconify()
                search_window.withdraw()

            profile.configure(command=lambda e=profile:  c(e))
            profile.grid(row=7 + i*2, column=1, padx=400, pady=0, sticky='w', columnspan=4)

    postB = Button(frame,command=c5, text="search", bg="darkblue", fg="white", font=("Helvetica", 11))
    postB.grid(row=1, column=2,pady=50,padx=10, sticky="sw")

    return search_window

def changeUsrWindow():
    changeUsr_window = get_window()
    changeUsr_window.configure(bg="darkblue")

    def c1():
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()
        changeUsr_window.withdraw()

    profileb = Button(changeUsr_window, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()  
        changeUsr_window.withdraw()

    timelineb = Button(changeUsr_window, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        changeUsr_window.withdraw()

    searchb = Button(changeUsr_window, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        changeUsr_window.withdraw()

    settingsb = Button(changeUsr_window, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)
    
    changeL = Label(changeUsr_window, text="New username:",bg="darkblue",fg="white", font=("Helvetica", 16))
    changeL.place(x = 200 + 200, y = 150)
    
    changetb = Entry(changeUsr_window, font=("Helvetica", 16))
    changetb.place(x=350 + 200, y=150)
    
    changeB = Button(changeUsr_window, text="Change username",bg="darkblue",fg="white", font=("Helvetica", 11))
    changeB.place(x=600 + 200, y=150)
    return changeUsr_window

def changeImageWindow():
    changeImage_window = get_window()
    changeImage_window.configure(bg="darkblue")

    def c1():
        # profile_window = profileWindow("Create post")
        profile_window.deiconify()
        changeImage_window.withdraw()

    profileb = Button(changeImage_window, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()  
        changeImage_window.withdraw()

    timelineb = Button(changeImage_window, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        changeImage_window.withdraw()

    searchb = Button(changeImage_window, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        changeImage_window.withdraw()

    settingsb = Button(changeImage_window, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)
    
    changeL = Label(changeImage_window, text="choose Image",bg="darkblue",fg="white", font=("Helvetica", 16))
    changeL.place(x = 200 + 200, y = 150)
    
    changetb = Button(changeImage_window, text="Choose",bg="darkblue",fg="white", font=("Helvetica", 11))
    changetb.place(x=350 + 200, y=150)
    
    changeB = Button(changeImage_window, text="Change",bg="darkblue",fg="white", font=("Helvetica", 11))
    changeB.place(x=600 + 50, y=150)
    return changeImage_window


def editInfoWindow():
    editInfo_window = get_window()
    editInfo_window.configure(bg="darkblue")

    def c1():
        profile_window.deiconify()
        editInfo_window.withdraw()

    profileb = Button(editInfo_window, text="Profile", command=c1, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    profileb.grid(row=0, column=0, padx=0, pady=0)

    def c2():
        timeline_window.deiconify()
        editInfo_window.withdraw()

    timelineb = Button(editInfo_window, text="Timeline", command=c2, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    timelineb.grid(row=0, column=1, padx=0, pady=0)

    def c3():
        search_window.deiconify()
        editInfo_window.withdraw()

    searchb = Button(editInfo_window, text="Search", command=c3, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    searchb.grid(row=0, column=2, padx=0, pady=0)

    def c4():
        setting_window.deiconify()
        editInfo_window.withdraw()

    settingsb = Button(editInfo_window, text="Settings", command=c4, bg="darkblue", fg="white", height=1, width=31, font=("Helvetica", 16))
    settingsb.grid(row=0, column=3, padx=0, pady=0)
    welcome = Label(editInfo_window, text="facebook lite", bg="darkblue", fg="white", font=("Helvetica", 20))
    welcome.place(x=600, y=100)
    
    username = Label(editInfo_window, text="username:", bg="darkblue", fg="white", font=("Helvetica", 16))
    username.place(x=500 - 100, y=150)
    gmail = Label(editInfo_window, text="gmail:", bg="darkblue", fg="white", font=("Helvetica", 16))
    gmail.place(x=500 - 100, y=200)
    password = Label(editInfo_window, text="password:", bg="darkblue", fg="white", font=("Helvetica", 16))
    password.place(x=500 - 100, y=250)
    comfirm = Label(editInfo_window, text="confirm password:", bg="darkblue", fg="white", font=("Helvetica", 16))
    comfirm.place(x=500 - 100, y=300)
    
    usernametb = Entry(editInfo_window, font=("Helvetica", 16))
    usernametb.place(x=600, y=150)
    gmailtb = Entry(editInfo_window, font=("Helvetica", 16))
    gmailtb.place(x=600, y=200)
    passwordtb = Entry(editInfo_window, font=("Helvetica", 16))
    passwordtb.place(x=600, y=250)
    confirmtb = Entry(editInfo_window, font=("Helvetica", 16))
    confirmtb.place(x=600, y=300)

    def c1():
        verify_window.deiconify()
        editInfo_window.withdraw()
        
    sign_up = Button(editInfo_window, text="Sign up", command=c1, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    sign_up.place(x=630 + 50, y=380)

    def c2():
        start_window.deiconify()
        editInfo_window.withdraw()
    back = Button(editInfo_window, text="back", command=c2, bg="darkblue", fg="white", height=1, width=15, font=("Helvetica", 16))
    back.place(x=530 - 50 - 40, y=380)
    return editInfo_window

start_window = startWindow()
login_window = loginWindow()
register_window = registerWindow()
verify_window = verifyWindow()
profile_window = profileWindow("Create post")
timeline_window = timelineWindow()
post_window = postWindow()
setting_window = settingWindow()
search_window = searchWindow()
changeUsr_window = changeUsrWindow()
changeImage_window = changeImageWindow()
editInfo_window = editInfoWindow()

start_window.deiconify()
start_window.mainloop()

# profile_window.deiconify()
# profile_window.mainloop()

# timeline_window.deiconify()
# timeline_window.mainloop()
