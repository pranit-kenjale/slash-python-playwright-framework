# slash-python-playwright-framework

# SETUP STEPS
Use $x() -> XPATH and $$() -> CSS in chrome console panel.

1. Create virtual environment
`python3 -m venv .venv`

2. Activate virtual environment
`source .venv/bin/activate`

3. Confirm the virtual environment is activated, check the location of your Python interpreter
`which python`

4. To deactivate virtual environment
`deactivate`

5. Install dependencies
`pip3 install -r requirements.txt`


# PLAYWRIGHT SPECIFICS

1. Install playwright deps and essentials
- `pip3 install playwright`
- `playwright install`

2. Dynamic run and code gen
- `playwright codegen www.google.com`

3. View Trace
- `playwright show-trace trace.zip`

