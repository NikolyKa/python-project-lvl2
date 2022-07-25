install: #установление зависимостей
	poetry install

build: #собирает программу
	poetry build 
publish: #публикует программу
	poetry publish --dry-run
package-install: #устанавливает пакет
	python3 -m pip install --user --force-reinstall dist/*.whl
lint: #проверяет код на чистоту
	poetry run flake8 gendiff
test: 
	poetry run pytest gendiff
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

