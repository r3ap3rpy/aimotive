from flask import Flask
from redis import Redis
app = Flask(__name__)

redis = Redis(host='10.100.51.62', port=6379)

@app.route("/healthz")
def healthz():
	return "ok"

@app.route("/alert")
def alert():
	if not redis.get('counter'):
		redis.set('counter',0)
	redis.incr('counter')
	return "counter increase"

@app.route("/counter")
def counter():
	if not redis.get('counter'):
		redis.set('counter',0)
	return redis.get('counter')

@app.route("/version")
def version():
	return "Short git commit!"

if __name__ == '__main__':
	app.run(host='0.0.0.0',port = 5000, debug = True)
