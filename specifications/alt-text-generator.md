# alt text generator specifications

[//]: # (Written by Ian Lurie, November 2025, but use at your own risk. I'm not responsible for API overspending, lousy ALt text, or accidental missile launches. If you've got questions, though, find me at ianlurie.com or on LinkedIn at https://www.linkedin.com/in/ianlurie/)

[//]: # (Hey, humans: I'm not a developer. I'm sure you can write a better spec. But feed this into Claude Code and you'll have a solid start on your very own ALT text generator.)

## Purpose

Generate quality, relevant ALT text for images provided in a CSV.

## General guidelines

- Build this tool in Python 3
- Build it to run in pipenv
- Use the Claude API for image analysis
- Use Haiku 4.5 as your model

## Inputs

There are multiple inputs:

### The CSV

I'll provide a CSV that contains:

- A list of images (called the "Destination" from now on)
- The pages on which those images are included (called the "Source" from here on)
- The size, in bytes, of each image
- An empty column called "ALT text."
- There may be other columns. You can ignore those unless the instructions.md says otherwise

Most often, there will be many instances of each source, since these pages will have multiple images.

### Scraped data

You will generate another a scrape of the source page, including:

- the page title tag
- the H1 on the page (if there is one)
- the H2, H3, or H4 closest to the image in the HTML structure
- any caption immediately adjacent to the image

### Instructions.md

I will provide a set of instructions contained in a Markdown file. ALWAYS use this file to adjust the Claude Vision analysis. For example:

- Overall subject matter of the analyzed site and images
- Criteria for ALT text such as length and vocabulary

## How It Works

1. Run command line
2. Command includes -i and -o flags for input and output file names, respectively
3. Command includes flags for continuing or restarting analysis, minimum and maximum image size (in bytes) for analysis

### First, load page data

1. In the input CSV, add three columns to the sheet: "title tag," "H1 tag," and "caption"
2. Read the csv.
	1. Obtain the title tag for each page and inserting that into every row that has relevant including page.
	2. Obtain the H1 tag for each page (if there is one) and inserting that into every row that has the relevant including page.
	3. Obtaining adjacent caption and/or H2, H3, or H4 inserting that into the sheet for that specific image.

### Next, examine images

1. Use Claude vision via the API and load 100 rows at a time so that you can process 20 images in a batch, per Claude API specifications. This should reduce cost.
2. Load the first row on the sheet.
3. Look at the title tag, H1, and other adjacent text.
4. Load the image from the site and examine the content of the image.
5. Generate ALT text using the instructions provided in the instructions Markdown file.
6. Write that ALT text to the "ALT text" column in the relevant row.
7. Go to the next 100 rows and repeat the process.

By default: If an image is larger than 2000 X 2000 px, leave it out of that 100 row batch and submit the image to Claude Vision API individually. Generate ALT text for that image after you generate the other images in that batch.

If an image is larger than 8000 x 8000 px, enter "image too large" in the "message" column for that image and don't submit.

### IMPORTANT - duplicate handling

Never submit multiple copies of the same image for analysis. 

The site may include one image on many pages, resulting in multiple entries in the input CSV. In this case, insert the same ALT text for all instances of the image.

[//]: # (Hey, humans: You may want to delete this part. I added it because I work on a lot of Wordpress sites with auto-generated responsive images. I didn't want to spend a gazillion dollars on duplicate copies of one image.)

If the site uses responsive image sizes, image filenames will end with -WIDTHxHEIGHT. For example, myimage-300x300.jpg for the 300x300 pixels version of myimage.jpg. To avoid this, check the base filename and copy the ALT attribute to all dimensions for that base filename.

### Output

Generate two files:

1. A standard output file that is a copy of the input file plus an ALT text column.
2. A smaller, deduplicated file that has one instance of each image URL and ALT text.


## Folder structure

./alt-text-generator
├── thething
├── files 
	├──input-file.csv
	├──output-file.csv
	├──instructions.md

thething is all necessary Python code.

## Other features

1. Show progress.
2. If the process has to pause or stop, indicate the last image processed so that I can easily resume later.
3. Skip rows where the images already have ALT text.
4. Create a github repository for this project.
5. .gitignore should ignore all .env files, as well as all files in the files folder