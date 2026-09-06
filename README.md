# Know Yellowknife · Backend API

A Django REST Framework development backend for a community-learning platform.

**Python · Django · Django REST Framework**

[Getting started](#getting-started) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

## What you can explore

- Member profiles, posts, comments, likes and following.
- Quiz-related models and endpoints.
- Authentication, origin configuration and Cloudinary media settings.

> **Project notes:** This is a separate backend project. The currently deployed static Know Yellowknife quiz does not need this API to run.

## Getting started

Requires Git, Python, pip and a virtual environment. Dependency pins in older projects may need a compatible Python environment; this README does not upgrade them.

```bash
git clone https://github.com/SamOBrienOlinger/backend-know-yellowknife.git
cd backend-know-yellowknife
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` instead.

After resolving the project notes and configuring the local environment, use:

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000). Stop the server with **Ctrl+C**. Use `python manage.py createsuperuser` in the same project directory if you need access to Django admin.

## Configuration

Settings are defined in [backend/settings.py](backend/settings.py). Set the values used by your chosen local configuration before running Django. A `.env` file is only read when the project explicitly loads it; most of these projects read the process environment or an optional `env.py`.

| Variable | Purpose |
| --- | --- |
| `ALLOWED_HOSTS` | Comma-separated hostnames accepted by Django. |
| `CLIENT_ORIGIN` | Frontend origin allowed by the backend, including scheme and port. |
| `CLIENT_ORIGIN_DEV` | Development frontend origin; check the settings logic before using a cloud-workspace URL. |
| `CLOUDINARY_URL` | Cloudinary connection URL used for media storage. Keep the value private. |
| `DATABASE_URL` | Connection URL for your own development database. Required where settings parse it without a fallback. |
| `DEBUG` | Debug-mode switch. Inspect the settings for the expected value. |
| `GITPOD_WORKSPACE_URL` | Workspace URL used when constructing cloud-development origins. |
| `SECRET_KEY` | Django signing key. Use a locally generated value and keep it out of Git. |

Use a disposable development database for migrations and tests. Keep service credentials and local configuration out of commits.

## Repository guide

| Path | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Python dependency versions |
| [manage.py](manage.py) | Django management commands |
| [backend/settings.py](backend/settings.py) | Django configuration |

## Checks and review

From the directory containing `manage.py`, run `python manage.py check` and `python manage.py test` after configuring an isolated development database. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

No current hosted endpoint is established by this README. A backend deployment needs a configured runtime and its own service settings; GitHub Pages cannot execute the server-side application.

## Credits and reuse

Reuse terms are recorded in [LICENSE](LICENSE). Third-party assets and dependencies retain their own terms.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). For a problem or suggested improvement, [open an issue](https://github.com/SamOBrienOlinger/backend-know-yellowknife/issues) with the affected page or command, steps to reproduce, and expected behaviour.

[Back to top](#know-yellowknife--backend-api)
