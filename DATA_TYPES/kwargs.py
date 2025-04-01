# def show_details(**details):
#     for key, value in details.items():
#         print(f"{key}:{value}")

# show_details(name="dennis ", city="ongate rongai", age=21)
    
    
#uing args
def show_names(*args):
    for name in args:
        print(f"name of the individuals are:{name}")
show_names("alice","metro","trappa rappa")