"""Setup configuration."""


from setuptools import setup


setup(
    name="http-server",
    description="HTTP Server",
    version=0.1,
    author="Avery Pratt and Ben Shields",
    author_email="apratt91@gmail.com, bshields23@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["client", "server"],
    extras_require={
        "test": ["pytest"]
    },
)
