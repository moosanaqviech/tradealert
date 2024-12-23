from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>TradeNotification!</h1>"
@app.route('/process-data', methods=['GET','POST'])
def process_data():
    # Get the JSON data from the request
    try:
        data = request.json
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400

        # Extract specific fields from the data
        item_id = data.get('id')
        title = data.get('title')
        content = data.get('content')
        created_date = data.get('createdDate')

        # Print the data for debugging (optional)
        print(f"Received data: {data}")
        app.logger.info(f"Received data: {data}")

        # Perform any processing with the data here
        # For now, just logging that the data was received
        print(f"Processing data for item: {item_id}, title: {title}")
        app.logger.info(f"Processing data for item: {item_id}, title: {title}")
        # Respond to Wix to indicate success
        response = {
            "status": "success",
            "message": f"Data for item {item_id} processed successfully"
        }
        return jsonify(response), 200

    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == '__main__':
    # Run the Flask server on port 5000
    # Replace `0.0.0.0` with `127.0.0.1` if you want to restrict access to local
    app.run(host='0.0.0.0', port=10000)
