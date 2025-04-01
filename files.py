def get_details(**info):
    with open("ovo.txt", "w") as file:
        for key,value in info.items():
            file.write(f"{key}: {value}\n")
            file.write("\n")

get_details(name="dennis muthama", age= "20", car="IMPREZA")





