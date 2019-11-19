from setuptools import setup

setup(
    name="HelloWorldTG",
    version="0.2",
    data_files = [('.', ['data-1.csv'])],
    
    # Project uses matplotlib, so ensure that it gets
    # installed or upgraded on the target machine
    install_requires=['matplotlib', 'pandas'],

    # metadata to display on PyPI
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]

    # could also include long_description, download_url, etc.
)
