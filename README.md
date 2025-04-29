# Facial Image-Based Nationality Classification

This project aims to classify facial images based on nationality using deep learning techniques. The project includes tools for dataset collection, preprocessing, and model training.

## Project Structure

```
.
├── datasets/           # Directory for storing datasets
├── models/            # Directory for trained models
├── scripts/           # Project scripts
│   ├── preprocessing/ # Data preprocessing scripts
│   │   ├── face_dataset_cleaner.ipynb
│   │   ├── face_extractor_mtcnn.ipynb
│   │   └── chia_data-.py
│   └── crawler/       # Web scraping scripts
└── venv/              # Virtual environment
```

## Features

- Web scraping tools for dataset collection
- Face detection and extraction using MTCNN
- Dataset preprocessing and cleaning
- Deep learning model for nationality classification

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Facial-Image-Based-Nationality-Classification.git
cd Facial-Image-Based-Nationality-Classification
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Note: If you need to use dlib, you'll need to install CMake first and then uncomment it in requirements.txt.

## Usage

### Dataset Collection

The crawler scripts in `scripts/crawler/` can be used to collect facial images from various sources.

### Preprocessing

1. Use `face_dataset_cleaner.ipynb` to clean and organize the dataset
2. Run `face_extractor_mtcnn.ipynb` to extract faces from images
3. Use `chia_data-.py` to split the dataset into training and validation sets

### Model Training

Instructions for model training will be added as the project progresses.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

- MTCNN for face detection
- TensorFlow for deep learning framework
- OpenCV for image processing
