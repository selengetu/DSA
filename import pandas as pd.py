import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
train_df = pd.read_csv('training_data.csv')
test_df = pd.read_csv('test_data.csv')

# Preprocess text data
tfidf = TfidfVectorizer(stop_words='english')
X_train_text = tfidf.fit_transform(train_df['full_text'])
X_test_text = tfidf.transform(test_df['full_text'])

# Feature Engineering
train_df['hashtags'] = train_df['hashtags'].astype('category').cat.codes
test_df['hashtags'] = test_df['hashtags'].astype('category').cat.codes

# Prepare features and target
X_train = pd.concat([pd.DataFrame(X_train_text.toarray()), train_df[['favorite_count', 'retweet_count', 'hashtags', 'year']]], axis=1)
y_train_dim1 = train_df['dim1_nominate']
y_train_dim2 = train_df['dim2_nominate']

X_test = pd.concat([pd.DataFrame(X_test_text.toarray()), test_df[['favorite_count', 'retweet_count', 'hashtags', 'year']]], axis=1)

# Initialize and train model
model_dim1 = RandomForestRegressor()
model_dim2 = RandomForestRegressor()

model_dim1.fit(X_train, y_train_dim1)
model_dim2.fit(X_train, y_train_dim2)

# Predict and evaluate
pred_dim1 = model_dim1.predict(X_test)
pred_dim2 = model_dim2.predict(X_test)
