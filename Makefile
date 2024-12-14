install-dep:
	pip install fastapi[all] fastapi-mail fastapi-jwt-auth[asymmetric] passlib[bcrypt] pymongo

start:
	uvicorn app.main: app --reload