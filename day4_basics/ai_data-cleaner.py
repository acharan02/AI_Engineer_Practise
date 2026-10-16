reviews = [
    "This product is excellent",
    "",
    "The delivery was slow",
    "This product is excellent",
    "AMAZING customer service",
    "   ",
    "The delivery was slow"
]
clean_reviews = []
unique_reviews=[]
for i in reviews:
    if i.strip():
        clean_reviews.append(i)
print("Original number of reviews:", len(reviews))
print("Cleaned number of reviews:", len(clean_reviews))
for i in clean_reviews:
    if i not in unique_reviews:
        unique_reviews.append(i)
print("Unique number of reviews:", len(unique_reviews))
print("Unique reviews:", unique_reviews)