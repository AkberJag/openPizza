# openPizza

This is a :construction: work in progress :construction: side project

## instructions to build and run this project

- ⚠️ Make sure you can run 'make' 🐃 commands ⚠️

Clone the project 🧬👨‍💻

```bash
  git clone https://github.com/AkberJag/openPizza.git
```

Go to the project directory 📂

```bash
  cd openPizza
```

Run the Docker 🐳 containers

```bash
make build
```

When the containers are running, do the alembic migration 🚀

```bash
make migrate
```

Populate the DB with fake data (Optional) 🌐📊

```bash
make addfake
```

run the VueJs frontend > http://localhost:8080
run the Swagger UI > http://localhost:5000/docs
