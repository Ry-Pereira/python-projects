from flask import Flask, render_template, request
from color_data import get_color_hex

# Create Flask application instance
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    background_color = "white"

    instruction = (
        "Instruction: Enter a color name of your choosing, "
        "and hit the button to change the background color."
    )

    if request.method == "POST":

        color = request.form.get("color_name")

        color_hex = get_color_hex(color)

        # Color found
        if color_hex != "No Color of Description":

            background_color = color_hex

        # Color not found
        else:

            instruction = "Instruction: Color not found, try again."

    return render_template(
        "index.html",
        instruction=instruction,
        background_color=background_color
    )


# Run the Flask app only if this file is executed directly
if __name__ == "__main__":

    app.run(debug=True)