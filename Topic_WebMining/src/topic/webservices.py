'''
Created on 17 mai 2017

@author: kimtaing
'''

topics=[]
topic={"name" : "Topic 2",
        "keywords" : ["big data", "ice cream"],
        "numberOfResults" : 10}
topics.append(topic)
topic={"name" : "Topic 2",
        "keywords" : ["web mining", "chocolate cookies"],
        "numberOfResults" : 5}
topics.append(topic)
topic={"name" : "Topic 3",
        "keywords" : ["data analytics", "data visualisation"],
        "numberOfResults" : 4}
topics.append(topic)

from topic import topics
topics=topics.get_topics("data analytic")

#[topics for i,topics in enumerate(topics)]

from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

#curl -i http://localhost:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/topics', methods=['GET'])
def get_topics():
    return jsonify({'topics': topics})

if __name__ == '__main__':
    app.run(debug=True)