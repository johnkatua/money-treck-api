install-dep:
	pip install fastapi[all] fastapi-mail fastapi-jwt-auth[asymmetric] passlib[bcrypt] pymongo black

start:
	uvicorn app.main: app --reload