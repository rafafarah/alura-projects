# aboutMe = "My name is Jorge and I'm 49 years old"
# # slicing aboutMe to get only the age
# substrig = aboutMe[25:28]
# print(substrig)


# # finding index for arguments
# url = "https:://www.bytebank.com.br/exchange?src=brl&dest=usd&value=1500"
# src_idx = url.find("src=")
# dest_idx = url.find("dest=")
# src = url[src_idx+4:dest_idx-1]
# print(src)


# spliting string using a separator
url = "https:://www.bytebank.com.br/exchange?src=brl&dest=usd&value=1500"
listArg = url.split("=")
print(listArg)