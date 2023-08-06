import qrcode as qr   ## importing qrcode library
img=qr.make("https://www.linkedin.com/in/vishnu-m99/")  
#which information to be displayed  with the help of make methods.
img.save("Profile_Info.png")    # saving into png form
