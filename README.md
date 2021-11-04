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

</br>

**Development exercise:** Mood sensing app </br>

**Time allotted:** 1 day </br>

The camera on your shiny new phone can sense a user’s mood based on their facial features, where
mood can be characterized as either happy, sad or neutral to start with. 

We like you to design and implement a back-end application that leverages the phone’s mood-sensing
capability to collect mood data and provide insights:

- Upload a mood capture for a given user and location 
- Return the mood frequency distribution for a given user
- Return the proximity to locations (home, office, shopping center,…) where a given user is
happy.
  

Specifically, create skeleton code to implement REST service cloud backend APIs for the application.

Preferably in Python or Java, but you are free to use any framework that you are comfortable with.

Feel free to make any reasonable assumptions about the scope of your implementation (e.g. a 3rd
party library for obtaining location characteristics, given a set of GPS coordinates)

It is not necessary for the code to be runnable, but you should have at least identified any 3rd party
libraries and components that you intend to use and we would like to see at least some code skeleton
and pseudo code.

Try to cover as much detail as necessary to articulate the application design and implementation for
the following.

**Implementation Aspects:**
- Define API
- Create dev project
- Layout code structure
- Design data model and key data structures
- Define data persistence using any data store of your choice.
- Define Implementation of operations
- Input validation
- Authentication
- Authorization
- Unit test
- Last but not least, provide a README for your design, implementation and assumptions.


We request you to zip up your project and send it back to us (i.e. do not upload it to GitHub or any
other public repository)

Once we received your project, we will review it with you!
