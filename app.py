from flask import Flask
from flask_redis import FlaskRedis
REDIS_URL = "redis://localhost:6379/0"
app = Flask(__name__)
redis_client = FlaskRedis(app)

@app.route("/healthz")
def healthz():
	return "ok"

@app.route("/alert")
def alert():
	#increase counter in redis
	if not redis_client.get('counter'):
		redis_client.set('counter',0)
	redis_client.incr('counter')
	return "counter increase"

@app.route("/counter")
def counter():
	if not redis_client.get('counter'):
		redis_client.set('counter',0)
	return redis_client.get('counter')

@app.route("/version")
def version():
	return "Short git commit!"

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000, debug = True)
