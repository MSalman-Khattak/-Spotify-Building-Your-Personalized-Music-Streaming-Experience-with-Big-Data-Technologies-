from flask import Flask, render_template
from kafka import KafkaProducer, KafkaConsumer
import json
import threading

app = Flask(_name_)

# Kafka configuration
bootstrap_servers = ['localhost:9092']
user_activity_topic = 'user_activity'
recommendations_topic = 'recommendations'

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Create Kafka consumer
consumer = KafkaConsumer(recommendations_topic, bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='latest', enable_auto_commit=True,
                         group_id='my-group', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Mock user activity data
def send_user_activity():
    activities = [{'user_id': 1, 'song_id': 101, 'action': 'listen'},
                  {'user_id': 2, 'song_id': 102, 'action': 'listen'},
                  {'user_id': 1, 'song_id': 103, 'action': 'like'}]
    for activity in activities:
        producer.send(user_activity_topic, value=activity)
        producer.flush()

# Background thread for sending user activity data
activity_thread = threading.Thread(target=send_user_activity)
activity_thread.daemon = True
activity_thread.start()

# Store recommendations globally
recommendations = []

# Homepage route
@app.route('/')
def index():
    global recommendations
    for msg in consumer:
        recommendations.append(msg.value)
        if len(recommendations) >= 3:  # Limit recommendations to 3 for demonstration
            break
    rendered_template = render_template('index.html', recommendations=recommendations)
    recommendations.clear()  # Clear the recommendations after rendering the template
    return rendered_template

if _name_ == '_main_':
    app.run(debug=True)
