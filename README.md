<h3 align="center">EXTERNAL-SOURCE-TRANSFORM</h3>

  <p align="center">
    <a href="https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-TRANSFORM/wiki"><strong>Explore the docs</strong></a>
    <br />
  </p>
</div>

## About The Service

This service aims to transform data from an external source to a desired format.

### Built With

[![Python][Python]][Python-url]
[![Pipenv][Pipenv]][Pipenv-url]
[![FastAPI][FastAPI]][FastAPI-url]
[![PyTest][PyTest]][PyTest-url]

## Getting Started

### Prerequisites

You firstly have to install Python and PipEnv on your machine.

To do so, you can follow the instructions on the [official Python website][Python-url] and on the [official pipenv website][Pipenv-url].

### Installation

#### Install Python

[follow this documentation for install Python][Python-url-download]

#### Install Pip

[follow this documentation for install Pip][Pip-url-download]

#### Install PipEnv

```sh
pip install pipenv
```

#### Development

1. Clone the repository

    ```sh
    git clone https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/EXTERNAL-SOURCE-TRANSFORM.git
    ```

2. Install the dependencies

    ```sh
    pipenv shell
    pipenv install --dev
    ```
   
3. Setup environment variables

    ```sh
    cp .env.example .env
    # Edit the `.env` file and fill in the required variables.
    ```

4. Run the service

    ```sh
    faststapi dev
    ```

#### Production

1. Clone the repository

    ```sh
    git clone https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/EXTERNAL-SOURCE-TRANSFORM.git
    ```

2. Install the dependencies

    ```sh
    pipenv shell
    pipenv install
    ```

3. Run the service

    ```sh
    faststapi run
    ```

## API Documentation

FastAPI provides an interactive API documentation based on OpenAPI that can be accessed on the route `/docs`.
You'll be able to see all the available endpoints and test them there.

## Collaborate

To collaborate on the project, the following conventions must be followed:
- git management is based on [gitflow](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow) conventions
- each story must be created in a dedicated feature with the following naming: `feature/name-of-the-feature`.
- commits must respect the following conventions:
  - `feat: implementation about something new in a feature`
  - `fix: fix a bug`
  - `refactor: refactor code`
  - `style: change style`
  - `docs: change documentation`
  - `test: add tests`
  - `chore: change configuration and update readme/.gitignore`
- Issues will be displayed on the purpose github issue page
- The discussion about the on working are being conducted in our personal Discord (access can be requested by contact)

### Convention

The project uses the [Python coding conventions][PEP8-url].

#### Workflow

The project uses [Gitflow][GitFlow-url]. The branches used are: `main`, `develop`, `feature`, `release`, `hotfix`. The branches are named with the following pattern: `type/short-description` eg.(feature/awsome-feature).

#### file naming

The project uses [PEP8](https://peps.python.org/pep-0008) naming convention.

## Directory Structure

```sh
┣ app/
┃ ┣ errors/
┃ ┣ models/
┃ ┣ routes/
┃ ┣ schemas/
┃ ┃ ┣ requests/                     // API requests validator
┃ ┃ ┗ responses/                    // API responses validator
┃ ┗ services/
┣ tests/
┃ ┗ mocks/
┗ docs/

```

## License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/EXTERNAL-SOURCE-TRANSFORM/blob/develop/LICENSE.txt) for more information.

## Contact

You can contact any member of the team via discord on the class server([SI-T2a][Discord-url]).

[Python]: https://img.shields.io/badge/Python%203.12-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Python-url-download]: https://www.python.org/downloads/
[FastAPI]: https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Pipenv]: https://img.shields.io/badge/PipEnv%202023.12.1-000000?style=for-the-badge&logo=python&logoColor=white
[Pipenv-url]: https://pipenv.pypa.io/en/latest/
[GitFlow-url]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
[Commit-url]: https://www.conventionalcommits.org/
[Pip-url-download]: https://pip.pypa.io/en/stable/installation/
[PyTest]: https://img.shields.io/badge/PyTest-000000?style=for-the-badge&logo=python&logoColor=white
[PyTest-url]: https://docs.pytest.org/en/stable/
[PEP8-url]: https://peps.python.org/pep-0008/
[Discord-url]: https://discord.com/channels/1146349744822693899/1303407014122360943
