install-dep:
	pip install fastapi[all] fastapi-mail fastapi-jwt-auth[asymmetric] passlib[bcrypt] pymongo black pylint

start:
	uvicorn app.main: app --reload