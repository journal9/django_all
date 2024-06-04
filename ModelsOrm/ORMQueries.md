# ORM queries

## 1. Find the average book price for an author D

qs = Books.objects.filter(author=author).aggregate(Avg('price'))

## 2. Find the average rating for an author D

qs = Books.objects.filter(author=author).aggregate(Avg('rating'))

## 3. Find the average rating of books for reach for an author D

qs = Books.objects.values('reach').annotate(average_rating=Avg("rating"))

## 4. Find the average price and rating of books for reach for an author D

qs = Books.objects.values('reach').annotate(average_rating=Avg("rating"),average_price = Avg("price"))

## 5. Find the count of books by each author for reach D

qs = Books.objects.values('author','reach').annotate(count_books=Count("author"))

## 6. Find the average experience of authors for the different categories of reach D

qs = Books.objects.values('reach').annotate(Average_experience=Avg("author__experience"))

## 7. Find the min experience of authors for the different categories of reach D

qs = Books.objects.values('reach').annotate(Minimum_experience=Min("author__experience"))

## 8. Difference between the average start date and published date for an author

qs = Books.objects.values('author__name').annotate(average_difference = Avg('time_diff'))

## 9. Average rating of books published before a date for every author

qs = Books.objects.values('author__name').filter(published_date__lte="2024-08-22T07:20:20.585Z").annotate(avg_rating=Avg("rating"))

## 10. Difference between the average start date and published date for reach category

qs = Books.objects.values('reach').annotate(average_difference = Avg('time_diff'))

## 11. For each author, find count of different reach of books

qs = Books.objects.values('author__name','reach').annotate(count_books=Count("reach"))
