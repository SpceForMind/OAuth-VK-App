from setuptools import setup, find_packages

setup(
    name="OAuth-VK-App",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "Flask==1.1.1",
        "Flask-SQLAlchemy==2.4.0",
        "Flask-Migrate==2.5.2",
        "Flask-Login==0.4.1",
        "rauth==0.7.3"
    ]
)