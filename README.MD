# PYTEST-Grouping With Python :

![python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

Pytest allows us to use markers on test functions. Markers are used to set various features/attributes to test functions. Pytest provides many inbuilt markers such as xfail, skip and parametrize. Apart from that, users can create their own marker names.

#### Pre Requisites

  - Making the project as :
    ```
    mkdir pytest_grouping-testcase
	cd pytest_grouping-testcase
    ```
  - Web Scraping installation:
     ```
     open command prompt type 
        pip install virtualenv
     create virtualenv
    	>>virtualenv venv
     we need to activate virtualenv for use
    	>>venv\scripts\activate
    ```
  - Run the following command in your command line:
    ```
    pip install -U pytest
    ```
  - You need to register the custom marker. Create a pytest.ini file and place the following inside of it.
    ```
    [pytest]
    markers =
        login: user can login own website.
        signup: user can signup own website.
    ```
  - Way of execute program as below :
     *  pytest
     *  pytest -v -s 
     *  pytest -m login -v -s