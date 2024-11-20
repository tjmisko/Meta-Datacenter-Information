# Steps to Run

1. Initialize the virtual environment
```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

2. Ensure that you have `jq` installed. Running the command below should give you a path to your installation. If not installed, install it using your package manager (e.g. `brew install jq`)

```bash
$ which jq
```

3. Run the collect script
```bash
$ . collect
```

Data is stored in metaDatcenterInfo.json
