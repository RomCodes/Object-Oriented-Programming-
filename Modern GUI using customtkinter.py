#Create a modern GUI Login system with customtkinter


import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
    
root.geometry('600x500') #window size

frame = customtkinter.CTkFrame(master =root)
frame.pack(pady =20, padx =20, fill ='both', expand =True)

Titlelabel =customtkinter.CTkLabel(master =frame, text = 'Login System', font  = ('Ariel', 24))
Titlelabel.pack(pady =12, padx =10)

username = customtkinter.CTkEntry(master =frame, placeholder_text= 'username')
username.pack(pady= 15, padx =10)

password= customtkinter.CTkEntry(master =frame, placeholder_text= 'password', show= '*')
password.pack(pady =20, padx= 10)

submit =  customtkinter.CTkButton(master =frame, text= 'Login')
submit.pack(pady =20, padx =10)

rememberMe =customtkinter.CTkCheckBox(master= frame, text= 'Remember Me')
submit.pack(pady =20, padx =10)


usr = username.get() # get text from line 0 character 0 till the end)
passwrd = password.get() # get text from line 0 character 0 till the end)



root.mainloop()




