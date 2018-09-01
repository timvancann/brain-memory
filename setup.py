from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="brain-memory",
    version="0.0.1",
    description="A package to train your memory",
    author="Tim van Cann",
    long_description=long_description,
    author_email="timvancann@gmail.com",
    packages=["brain_memory"],
    install_requires=[
        'english-to-ipa==0.1',
        'pyyaml==3.13'
    ],
    extras_require={
        'test': {
            'pytest==3.6.2',
            "flake8==3.5.0"
        },
    },
    include_package_data=True,
    dependency_links=[
        "git+https://github.com/mphilli/English-to-IPA.git@master#egg=english-to-ipa-0.1"
    ],
)
