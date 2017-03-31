init:
	sudo pip install -r requirements.txt

test:
	nosetests tests

clean:
	find . -type f -name "*.pyc" -delete
