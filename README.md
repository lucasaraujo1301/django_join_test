# This project is dedicated to a company challenge
## Tech used for this work.
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Django Rest Framework](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Action](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## To run this project, you will need only of Docker and docker-compose. After you installed these two program, just follow theses commands to run the project.
`cp .env.example .env`

> **Note:** You will need to get a API Key from https://console.cloud.google.com/google/maps-apis/start?utm_source=Docs_GS_Button&ref=https:%2F%2Fdevelopers.google.com%2Fmaps%2F to be able to run this project correctly.

After creating the .env and fill the variable `GOOGLE_MAPS_API_KEY` with your api Key, and run:
```
docker-compose build
docker-compose up -d db
docker-compose up app
```
And now just open your browser in `http://localhost:8000` and start to use it.
