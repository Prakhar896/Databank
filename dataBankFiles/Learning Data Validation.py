def email(address):
    if not "@" in address:
        return "Invalid email keyed. Try again."
    if address[-3] != "n" or address[-2] != 'e' or address[-1] != 't':
        return "Invalid email keyed. Try again."
    return "Valid email."
    
#### SUGGESTED ANSWER ####
def email(x):
    if x.endswith('@ngeeannsec.net') and len(x) > 15:
        # Ensure that x will stop with "@ngeeannsec.net"
        # Length check ensures that "@ngeannsec.net" is not accepted
        return "Valid email"
    else:
        return "Invalid email keyed. Try again."
    
