from flask import Flask
import sys
sys.path.append('../service')
from service.hand_sensor import HandSensor

app = Flask(__name__)

@app.route("/")
def hs_driver():
    ts = [0.091, 0.165, 0.223, 0.318, 0.373, 0.429, 0.481, 0.559, 0.638, 0.734]
    lh = [275, 272, 271, 268, 19, 265, 260, 261, 262, 260]
    rh = [-100, 201, 202, 210, 222, 220, 199, -100, 195, 189]
    
    h  = HandSensor(ts, lh, rh) 
    h.avgPressure()
    
    ts = [2.057, 2.114, 2.208, 2.304, 2.338, 2.428, 2.523, 2.595, 2.659, 2.738]
    lh = [-100, -100, -100, -100, 300, -100, 299, -100, -100, 299]
    rh = [177, 164, 158, 151, 153, 147, 145, -100, -100, 1]

    h  = HandSensor(ts, lh, rh)
    h.avgPressure()
    
    all_avg_values, ts_records, avg_of_all_avg = h.print_all_avg()

    result = "Avg of hand heights at diff timestamp: " + str(all_avg_values) + '<br>'
    result = result + "Timestamp records: " + str(ts_records)+ '<br>'
    result = result + "Final average detail: " + str(avg_of_all_avg)

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(3000),debug=True)
    # app.run()