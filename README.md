# Stem - moody

## Tools
- Python
- Django Rest Framework
- GeoDjango
- PostgreSQL with Postgis
- fer package with OpenCV and Tensorflow

I've started up with `Flask` as framework but then I realised that I would need a 
`spatial DB`, so I came across `DRF` with `GeoDjango` and `PostGIS` 
that seemed to be the best choice even if it's maybe a bit cumbersome.
Also I used `fer` package for analyzing the picture.

### Future work:
Dockerize the project and deploying it to AWS, use a load balancer for it and 
also store pictures in S3 in order to have more data to further improve an ML model on detecting moods.

> **_NOTE:_**   All this was made in regard to the time that I had.