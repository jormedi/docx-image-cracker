# Docx image cracker

This is a simple script to extract images from docx files using [doc2txt](https://pypi.python.org/pypi/docx2txt/)
Also is an extension of the work already done by [nezhar](https://github.com/nezhar/docx-image-extractor)

## Usage

Create a *virtualenv* and install the package using the requirements.txt, yo only need to do it first time:
```
viertualenv venv && source venv/bin/activate
```

```
pip install -r requirements.txt && deactivate
```

Place the '.docx' document in the **input-file** folder named **word-file.docx**

Place template as **Upper.png** in template-file folder

run the script as many times as you want:
```
sh program.sh
```

## Result
1. The images will be extracted in the **images** folder
2. Layer **Upper.png** will be applied to ALL files and pasted them **out** folder
3. **result.zip** will be created in root with all images

## Example
There is an example ready inside, there is a **.docx** file ready to be cracked with an **Upper.png** layer

It has 4 pictures, when run program.sh it adds a transparent layer with date cracking
