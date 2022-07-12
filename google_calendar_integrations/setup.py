from setuptools import setup

setup(
    name='google_calendar_integrations',
    version='0.1.0',
    description='Google Calendar Integrations Package',
    author='Forrest Herman',
    author_email='forrestherman13@gmail.com',
    # list folders, not files
    packages=['google_calendar_integrations', 'google_calendar_integrations.tests'],
    scripts=['bin/script1', 'bin/script2'],
    # url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    install_requires=[
        "google-auth-oauthlib",
        "google-api-python-client",
    ],
)
