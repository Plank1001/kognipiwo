# Use CSS to your project

Continuation of: [this example](https://github.com/mikbuch/django_data_analysis), which in turn was based on [How to Upload Files With Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)

Now there is some additional CSS included.

## Running Locally

```bash
git clone https://github.com/mikbuch/django_css.git
```

```bash
cd django_css
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

### Troubleshooting

```
Git fatal: protocol 'https' is not supported
```

Use right-click paste, instead of crtl+V (see [this answer](https://stackoverflow.com/a/55985462/8877692)).
