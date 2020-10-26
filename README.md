# Recommender-System-with-Amazon-review-data
- Dataset: http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Electronics.csv
### Motivation
- to learn about different types of recommender systems.
- to explore Memory based and Model based algortithms for collaborative filtering.
- to build a recommender system

### Aproach
1. Load data into a Pandas dataframe
2. Explore Data with visualization
3. Reduce dimensionality to avoid memory error
4. Split training and test data, run a KNNWithMeans model, tune hyper parameters, test on test data.
5. Run SVD from python surprise package, cross validate the model, create a test set for a particular user and make recommendations.
