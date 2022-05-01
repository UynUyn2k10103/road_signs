Cách 1:
## create virtual environment
python -m venv env

## open virtual environment
.\env\Scripts\activate 

## update pip (pip-22.0.4)
python.exe -m pip install --upgrade pip 

pip install -r requirements.txt

## run app
uvicorn main:app --reload


Cách 2:
## create virtual environment
python -m venv env

## open virtual environment
.\env\Scripts\activate 

## update pip (pip-22.0.4)
python.exe -m pip install --upgrade pip 

## install tensorflow
pip install tensorflow

## Built web with Fast-api
pip install starlette

pip install uvicorn

pip install pyyaml

pip install fastapi

python -m pip install --upgrade Pillow

pip install python-multipart
