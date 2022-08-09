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
	poetry run flake8 tests
test: #проверяет программу на работоспособность
	poetry run pytest -vv
test-coverage: #проверяет покрытие тестами
	poetry run pytest --cov=gendiff --cov-report xml
