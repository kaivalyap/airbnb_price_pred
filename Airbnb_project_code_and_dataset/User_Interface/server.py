from flask import Flask, request,render_template
import pickle

# load the model from pickle file
file = open('./price_predict_model_rf.pkl', 'rb')
model = pickle.load(file)
file.close()

app = Flask(__name__)
@app.route("/", methods=["GET"])
def root():
    return render_template('main.html')

@app.route("/predict", methods=["POST"])
def predict_price():
    # value is in str so convert it into float
    property_type = int(request.form.get("property_type"))
    print(f"property_type = {property_type}, type = {type(property_type)}")

    room_type = int(request.form.get("room_type"))
    print(f"room_type = {room_type}, type = {type(room_type)}")


    accommodates = int(request.form.get("accommodates"))
    print(f"accommodates = {accommodates}, type = {type(accommodates)}")

    bathrooms = float(request.form.get("bathrooms"))
    print(f"bathrooms = {bathrooms}, type = {type(bathrooms)}")


    cancellation_policy = int(request.form.get("cancellation_policy"))
    print(f"cancellation_policy = {cancellation_policy}, type = {type(cancellation_policy)}")


    bedrooms = int(request.form.get("bedrooms"))
    print(f"bedrooms = {bedrooms}, type = {type(bedrooms)}")

    beds = int(request.form.get("beds"))
    print(f"beds = {beds}, type = {type(beds)}")

    log_price = model.predict([[property_type, room_type, accommodates, bathrooms, cancellation_policy, bedrooms, beds]])
    price = "{:.2f}".format(pow(2.718281828459045,log_price[0]))
    # return f"<h1>The price of you property is $ {price}</h1>"
    return render_template('result.html',predicted_price=price)


# run the server
app.run(port=5000)