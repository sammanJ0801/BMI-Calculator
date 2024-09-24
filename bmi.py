import eel

# Initialize the eel app
eel.init(".")

@eel.expose
def bmi_calculator(height, weight):
    if height.strip() == "":
        return "Height is empty!"
    
    if weight.strip() == "":
        return "Weight is empty!"
    
    try:
        # Convert height and weight to float
        height = float(height)
        weight = float(weight)
        
        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            return "Your BMI is " + format(bmi, ".1f") + " (underweight)"
        elif 18.5 <= bmi < 24.9:
            return "Your BMI is " + format(bmi, ".1f") + " (normal)"
        else:
            return "Your BMI is " + format(bmi, ".1f") + " (overweight)"
    
    except ValueError:
        return "Invalid input! Please enter numeric values."

# Start the eel app
eel.start("main.html", size=(800, 600))
