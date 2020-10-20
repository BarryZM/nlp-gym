from setuptools import setup, find_packages

setup(name="nlp_gym",
      version="0.0.1",
      description="NLPGym - A toolkit for evaluating RL agents on Natural Language Processing Tasks",
      author="Rajkumar Ramamurthy",
      author_email="raj1514@gmail.com",
      packages=find_packages(),
      install_requires=["numpy", "torch", "nltk", "flair", "pandas", "matplotlib",
                        "seaborn", "sklearn", "tqdm", "edit_distance", "rich",
                        "tensorflow==1.15.0",  "gym", "pytorch-nlp",
                        "tensorflow-datasets", "tfds-nightly",
                        "datasets"])