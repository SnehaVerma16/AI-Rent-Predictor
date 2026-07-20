from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np


app = Flask(__name__)

model = joblib.load("rent_prediction_model.pkl")


# BHK-wise Q1 property size
minimum_recommended_size = {
    1: 390,
    2: 680,
    3: 1100,
    4: 1617,
    5: 2090,
    6: 2250
}


# Maximum bathrooms observed for each BHK
maximum_bathrooms = {
    1: 3,
    2: 4,
    3: 6,
    4: 7,
    5: 6,
    6: 7
}


# Maximum floors observed city-wise
city_floor_limits = {
    "Bangalore": {
        "current": 26,
        "total": 40
    },
    "Chennai": {
        "current": 28,
        "total": 32
    },
    "Delhi": {
        "current": 10,
        "total": 24
    },
    "Hyderabad": {
        "current": 25,
        "total": 35
    },
    "Kolkata": {
        "current": 11,
        "total": 19
    },
    "Mumbai": {
        "current": 76,
        "total": 89
    }
}


# Maximum rent observed city-wise
city_max_rent = {
    "Bangalore": 3500000,
    "Chennai": 600000,
    "Delhi": 530000,
    "Hyderabad": 400000,
    "Kolkata": 180000,
    "Mumbai": 1200000
}


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    form_data = None
    error = None
    warning = None

    if request.method == "POST":

        form_data = request.form

        try:

            bhk = int(form_data["bhk"])
            size = int(form_data["size"])
            bathroom = int(form_data["bathroom"])
            current_floor = int(form_data["current_floor"])
            total_floors = int(form_data["total_floors"])

            area_type = form_data["area_type"]
            city = form_data["city"]
            furnishing_status = form_data["furnishing_status"]


            # Basic range validation

            if not 1 <= bhk <= 6:

                error = "BHK must be between 1 and 6."


            elif not 10 <= size <= 8000:

                error = (
                    "Property size must be between "
                    "10 and 8000 sq ft."
                )


            elif not 1 <= bathroom <= 10:

                error = "Bathrooms must be between 1 and 10."


            elif not -1 <= current_floor <= 76:

                error = (
                    "Current floor must be between "
                    "-1 and 76."
                )


            elif not 0 <= total_floors <= 89:

                error = (
                    "Total floors must be between "
                    "0 and 89."
                )


            elif current_floor > total_floors:

                error = (
                    "Current floor cannot be greater "
                    "than total floors."
                )


            # BHK-Size logical validation

            elif size < minimum_recommended_size[bhk]:

                warning = (
                    f"Prediction unavailable for this unusual "
                    f"property combination. Based on the training "
                    f"data, {bhk} BHK properties are typically "
                    f"around {minimum_recommended_size[bhk]} "
                    f"sq ft or larger."
                )


            # BHK-Bathroom validation

            elif bathroom > maximum_bathrooms[bhk]:

                warning = (
                    f"Prediction unavailable. The training data "
                    f"contains at most "
                    f"{maximum_bathrooms[bhk]} bathrooms "
                    f"for {bhk} BHK properties."
                )


            # City-Current Floor validation

            elif current_floor > city_floor_limits[city]["current"]:

                warning = (
                    f"Prediction unavailable. The training data "
                    f"contains properties only up to floor "
                    f"{city_floor_limits[city]['current']} "
                    f"in {city}."
                )


            # City-Total Floors validation

            elif total_floors > city_floor_limits[city]["total"]:

                warning = (
                    f"Prediction unavailable. Buildings in the "
                    f"training data for {city} contain at most "
                    f"{city_floor_limits[city]['total']} floors."
                )


            else:

                input_data = pd.DataFrame([{

                    "BHK": bhk,
                    "Size": size,
                    "Area Type": area_type,
                    "City": city,
                    "Furnishing Status": furnishing_status,
                    "Bathroom": bathroom,
                    "Current Floor": current_floor,
                    "Total Floors": total_floors

                }])


                log_prediction = model.predict(
                    input_data
                )[0]


                predicted_rent = np.expm1(
                    log_prediction
                )


                # Post-prediction city sanity check

                if predicted_rent > city_max_rent[city] * 1.05:

                    warning = (
                        f"The model generated a rent estimate outside "
                        f"the observed training range for {city}. "
                        f"Prediction has been withheld because it may "
                        f"be unreliable."
                    )

                else:

                    prediction = round(predicted_rent)


        except ValueError:
            error = "Please enter valid numeric values."

        except KeyError:
            error = "Some required fields are missing."

    return render_template(

        "index.html",

        prediction=prediction,

        form_data=form_data,

        error=error,

        warning=warning

    )


if __name__ == "__main__":
    app.run()