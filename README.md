# DevSecOps Pipeline

Конвейер DevSecOps использует GitLab CI/CD, интегрируя методы обеспечения безопасности и проверки соответствия на каждом этапе конвейера. 

## Technologies used

- GitLab
- Docker
- SonarQube
- Safety (Python dependency scanner)
- Bandit

## Project structure

- `app/`: Содержит исходный код и файл настройки для примера веб-приложения
- `.gitlab-ci.yml`: Определяет конфигурацию конвейера GitLab CI/CD.

## How it works

1. Конвейер GitLab CI/CD запускается при нажатии на код или запросе на слияние.
2. Конвейер создает образ Docker для веб-приложения, используя файл Docker в каталоге `app/`.
3. Конвейер запускает статическое тестирование безопасности приложений (SAST) с использованием SonarQube для сканирования исходного кода на наличие уязвимостей.
4. Конвейер выполняет автоматическое сканирование зависимостей с использованием Safety для выявления уязвимостей в зависимостях и библиотеках приложения.
5. Конвейер коммитит чистый код в основную ветку проекта




