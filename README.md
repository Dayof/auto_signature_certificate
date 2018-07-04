# Certificate auto generate 

Insert list of names in a certicate image.

## Usage

- Install (python3+):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

- Create json with the name "names.json" with a list of names:

```json
[
 name1,
 name2,
]
```

- Create folder image and certiticates and copy your certificate image inside:

```bash
mkdir image && mkdir certificates
cp [CERTIFICATE_IMAGE] image/
```

- Run with the name of your certificate file:

```bash
python insert_name.py "cert.png"
```

- Press F7 to take pictures, every event will get the next name on the list and save a file at certificates folder.
