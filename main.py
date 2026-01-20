from pyscript import document


def get_team(e):
  
    
    onlinergstr = document.getElementById("onrgstr").checked
    medclr = document.getElementById("medclr").checked
    gradelvl = document.getElementById("lvlslct").value
    section = document.getElementById("sct").value

    if onlinergstr and medclr == True:
       document.getElementById("print").innerHTML = f"You are eligible to join the Intramurals!<br>Grade Level: {gradelvl}<br>Section: {section}"
    else:
        document.getElementById("print").innerHTML = "You are not eligible to join the Intramurals."
