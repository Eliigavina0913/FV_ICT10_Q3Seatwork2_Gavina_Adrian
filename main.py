from pyscript import document


def get_team(e):

    document.getElementById("print").innerHTML = ""
    document.getElementById("image").innerHTML = ""    
    
    onlinergstr = document.querySelector("input[name='onrgstr']:checked").value
    medclr = document.querySelector("input[name='medclr']:checked").value
    gradelvl = int(document.getElementById("lvlslct").value)
    section = document.getElementById("sct").value

    if onlinergstr and medclr == True:
        print("You are eligible to join the Intramurals!")
    else:
        print("You are not eligible to join the Intramurals.")