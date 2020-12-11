import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pycontraptions-jwinternet",  # Replace with your own username
	version="0.0.1",
	author="Jared Winter",
	author_email="jwinternet@outlook.com",
	description="Various tools to make your life easier.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jwinternet/pycontraptions",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3.0",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
