# Workhours

Menu bar app that just counts for 8 hours straight.

## To install:
1. Clone the repo into a directory of your choice.
2. `cd` into the directory.
3. Make sure `virtualenv` is installed (`pip3 install virtualenv`).
4. Create a new virtual environment in the root directory: `python3 -m venv .`.
5. Activate the virtual environment: `source ./bin/activate`.
6. Install the dependencies: `pip3 install rumps py2app`.
7. Create the standalone app binary: `python3 setup.py py2app`.
8. To deactivate the virtual environment, type `deactivate`.
9. Copy the `Workhours.app` folder inside `dist` to your `Applications` folder.
10. Run the app.
