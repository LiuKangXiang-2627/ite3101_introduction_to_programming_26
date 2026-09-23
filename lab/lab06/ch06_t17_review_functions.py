def shut_down(s):
    if s():
        print("Shutting down")
    elif s == "no":
        print("Shutdown aborted")
    else:
        print("Sorry")
