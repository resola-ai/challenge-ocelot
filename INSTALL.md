# Installing project for developing on local PC

You have to have the following tools installed prior initializing the project:

- [docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

# Prepare python env using virtualenv
1. Create separate python virtual environment if you are going to run it in
local:

```bash

pyenv install 3.10.4
pyenv virtualenv 3.10.4 ocelot
pyenv local ocelot
pyenv shell ocelot
``````

2. Set up packages for using `invoke`

```bash
pip install -r requirements/local_build.txt
```

3. Start project initialization that will set up docker containers,
python/system env:

```bash
inv project.init
```

4. Run the project and go to `localhost:8000` page in browser to check whether
it was started:

```bash
$ inv django.run
```

That's it. After these steps, the project will be successfully set up.

Once you run `project.init` initially you can start web server with
`inv django.run` command without executing `project.init` call.
